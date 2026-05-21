from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import os

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})

def conectar_banco():
    return mysql.connector.connect(
        host="crud-black-clover-crudblackclover.j.aivencloud.com",
        user="avnadmin",
        password=os.getenv("DB_PASSWORD"),
        database="defaultdb",
        port=28790
    )


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
        
        eh_portador_atual = dados.get('eh_portador_atual', False)
        eh_nobre = dados.get('eh_nobre', False)
        eh_portador_demoniaco = dados.get('eh_portador_demoniaco', False)
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        sql = """INSERT INTO personagens 
                 (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                 id_raca_secundaria, id_local_origem, eh_portador_atual, eh_nobre, eh_portador_demoniaco) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                 
        valores = (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                   id_raca_secundaria, id_local_origem, eh_portador_atual, eh_nobre, eh_portador_demoniaco)
        
        cursor.execute(sql, valores)
        conexao.commit()
        
        cursor.close()
        conexao.close()
        
        return jsonify({"mensagem": "Novo mago adicionado ao grimório com sucesso!"}), 201
    
    except Exception as e:
        print(f"Erro na rota POST: {e}")
        return jsonify({"erro": str(e)}), 500


@app.route('/personagens/<int:id>', methods=['PUT'])
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
        eh_portador_atual = dados.get('eh_portador_atual', False)
        eh_nobre = dados.get('eh_nobre', False)
        eh_portador_demoniaco = dados.get('eh_portador_demoniaco', False)
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        
        sql = """
            UPDATE personagens SET
                nome = %s, tipo_magia = %s, id_esquadrao = %s, id_espirito = %s,
                id_raca = %s, id_raca_secundaria = %s, id_local_origem = %s,
                eh_portador_atual = %s, eh_nobre = %s, eh_portador_demoniaco = %s
            WHERE id = %s
        """
                 
        valores = (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
                   id_raca_secundaria, id_local_origem, eh_portador_atual, 
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