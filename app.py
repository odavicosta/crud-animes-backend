from flask import Flask, jsonify, request
from flask_cors import CORS
from functools import wraps
import mysql.connector
import hmac
import os

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 1024 * 1024  # 1 MB

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Sem ADMIN_TOKEN definido, as rotas de escrita recusam tudo (nunca liberam)
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "").strip()
if not ADMIN_TOKEN:
    print("AVISO: ADMIN_TOKEN não definido — POST, PUT e DELETE vão responder 401.")


def requer_token(rota):
    @wraps(rota)
    def verificar(*args, **kwargs):
        recebido = request.headers.get("Authorization", "")
        esperado = f"Bearer {ADMIN_TOKEN}"
        if not ADMIN_TOKEN or not hmac.compare_digest(recebido.encode(), esperado.encode()):
            return jsonify({"erro": "Não autorizado"}), 401
        return rota(*args, **kwargs)
    return verificar


@app.before_request
def limitar_tamanho():
    # Responde 413 antes da rota; senão o except genérico das rotas transformaria em 500
    if request.content_length and request.content_length > app.config["MAX_CONTENT_LENGTH"]:
        return jsonify({"erro": "Requisição grande demais"}), 413


# Configuração do banco só por variável de ambiente; se faltar alguma, a app nem sobe
VARIAVEIS_BANCO = ["DB_HOST", "DB_PORT", "DB_USER", "DB_PASSWORD", "DB_NAME"]
faltando = [nome for nome in VARIAVEIS_BANCO if not os.getenv(nome, "").strip()]
if faltando:
    raise RuntimeError(f"Variáveis de ambiente do banco não definidas: {', '.join(faltando)}")

try:
    porta_banco = int(os.getenv("DB_PORT"))
except ValueError:
    raise RuntimeError(f"DB_PORT precisa ser um número, recebido: {os.getenv('DB_PORT')!r}")

CONFIG_BANCO = {
    "host": os.getenv("DB_HOST").strip(),
    "port": porta_banco,
    "user": os.getenv("DB_USER").strip(),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME").strip(),
}

# Opcional: com DB_SSL_CA, o certificado do servidor é verificado contra a CA do Aiven
caminho_ca = os.getenv("DB_SSL_CA", "").strip()
if caminho_ca:
    if not os.path.isfile(caminho_ca):
        raise RuntimeError(f"DB_SSL_CA aponta para um arquivo que não existe: {caminho_ca}")
    CONFIG_BANCO.update(ssl_ca=caminho_ca, ssl_verify_cert=True)
else:
    print("AVISO: DB_SSL_CA não definido — conexão com o banco sem verificar o certificado.")


def conectar_banco():
    return mysql.connector.connect(**CONFIG_BANCO)


@app.route('/personagens', methods=['GET'])
def listar_personagens():
    try:
        nome = request.args.get('nome', '')
        magia = request.args.get('magia', '')
        local = request.args.get('local', '')
        esquadrao = request.args.get('esquadrao', '')
        
        conexao = conectar_banco()
        cursor = conexao.cursor(dictionary=True)
        
        sql = """
            SELECT 
                p.id, p.nome, p.tipo_magia, 
                p.eh_portador_demoniaco, p.eh_nobre,
                p.id_esquadrao, p.id_espirito, 
                p.id_raca, p.id_raca_secundaria, p.id_local_origem,
                e.nome AS nome_esquadrao,
                r.nome AS nome_raca,
                l.nome AS nome_local,
                esp.nome AS nome_espirito
            FROM personagens p
            LEFT JOIN esquadroes e ON p.id_esquadrao = e.id
            LEFT JOIN racas r ON p.id_raca = r.id
            LEFT JOIN locais l ON p.id_local_origem = l.id
            LEFT JOIN espiritos esp ON p.id_espirito = esp.id
            WHERE p.nome LIKE %s
                AND p.tipo_magia LIKE %s
                AND l.nome LIKE %s
                AND IFNULL(e.nome, '') LIKE %s
            ORDER BY p.nome ASC
        """
        
        cursor.execute(sql, (f"%{nome}%", f"%{magia}%", f"%{local}%", f"%{esquadrao}%"))
        lista_de_personagens = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        
        return jsonify(lista_de_personagens)
    
    except Exception as e:
        print(f"Erro na rota GET: {e}")
        return jsonify({"erro": str(e)}), 500


@app.route('/personagens', methods=['POST'])
@requer_token
def criar_personagem():
    try:
        dados = request.get_json()
        
        nome = dados.get('nome')
        tipo_magia = dados.get('tipo_magia')
        id_esquadrao = dados.get('id_esquadrao')
        id_espirito = dados.get('id_espirito')
        id_raca = dados.get('id_raca')
        id_raca_secundaria = dados.get('id_raca_secundaria')
        id_local_origem = dados.get('id_local_origem')
        
        eh_nobre = dados.get('eh_nobre', False)
        eh_portador_demoniaco = dados.get('eh_portador_demoniaco', False)
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        sql = """INSERT INTO personagens 
                 (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                 id_raca_secundaria, id_local_origem, eh_nobre, eh_portador_demoniaco) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                 
        valores = (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                   id_raca_secundaria, id_local_origem, eh_nobre, eh_portador_demoniaco)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return jsonify({"mensagem": "Novo mago adicionado ao grimório com sucesso!"}), 201
    
    except Exception as e:
        print(f"Erro na rota POST: {e}")
        return jsonify({"erro": str(e)}), 500


@app.route('/personagens/<int:id>', methods=['PUT'])
@requer_token
def atualizar_personagem(id):
    try:
        dados = request.get_json()
        
        nome = dados.get('nome')
        tipo_magia = dados.get('tipo_magia')
        id_esquadrao = dados.get('id_esquadrao')
        id_espirito = dados.get('id_espirito')
        id_raca = dados.get('id_raca')
        id_raca_secundaria = dados.get('id_raca_secundaria')
        id_local_origem = dados.get('id_local_origem')
        eh_nobre = dados.get('eh_nobre', False)
        eh_portador_demoniaco = dados.get('eh_portador_demoniaco', False)
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        sql = """
            UPDATE personagens SET
                nome = %s, tipo_magia = %s, id_esquadrao = %s, id_espirito = %s,
                id_raca = %s, id_raca_secundaria = %s, id_local_origem = %s,
                eh_nobre = %s, eh_portador_demoniaco = %s
            WHERE id = %s
        """
                 
        valores = (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                   id_raca_secundaria, id_local_origem, 
                   eh_nobre, eh_portador_demoniaco, id)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return jsonify({"mensagem": "Mago atualizado com sucesso!"}), 200
    
    except Exception as e:
        print(f"Erro na rota PUT: {e}")
        return jsonify({"erro": str(e)}), 500


@app.route('/personagens/<int:id>', methods=['DELETE'])
@requer_token
def deletar_personagem(id):
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        sql = "DELETE FROM personagens WHERE id = %s"
        cursor.execute(sql, (id,))
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return jsonify({"mensagem": "Mago expulso do grimório com sucesso!"}), 200
    
    except Exception as e:
        print(f"Erro na rota DELETE: {e}")
        return jsonify({"erro": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)