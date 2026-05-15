from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="black_clover"
    )



@app.route('/personagens', methods=['GET'])
def listar_personagens():
    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)
    
    sql = """
        SELECT 
            p.id, p.nome, p.tipo_magia, p.eh_portador_demoniaco, 
            e.nome AS nome_esquadrao,
            r.nome AS nome_raca,
            l.nome AS nome_local
        FROM personagens p
        LEFT JOIN esquadroes e ON p.id_esquadrao = e.id
        LEFT JOIN racas r ON p.id_raca = r.id
        LEFT JOIN locais l ON p.id_local_origem = l.id
    """
    
    cursor.execute(sql)
    lista_de_personagens = cursor.fetchall()
    
    cursor.close()
    conexao.close()
    
    return jsonify(lista_de_personagens)

@app.route('/personagens', methods=['POST'])
def criar_personagem():
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

@app.route('/personagens/<int:id>', methods=['PUT'])
def atualizar_personagem(id):
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
    
    sql = """UPDATE personagens 
             SET nome=%s, tipo_magia=%s, id_esquadrao=%s, id_espirito=%s, 
                 id_raca=%s, id_raca_secundaria=%s, id_local_origem=%s, 
                 eh_portador_atual=%s, eh_nobre=%s, eh_portador_demoniaco=%s
             WHERE id=%s"""
             
    valores = (nome, tipo_magia, id_esquadrao, id_espirito, id_raca, 
               id_raca_secundaria, id_local_origem, eh_portador_atual, 
               eh_nobre, eh_portador_demoniaco, id)
    
    cursor.execute(sql, valores)
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return jsonify({"mensagem": "Mago atualizado com sucesso!"}), 200

@app.route('/personagens/<int:id>', methods=['DELETE'])
def deletar_personagem(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    
    sql = "DELETE FROM personagens WHERE id = %s"
    cursor.execute(sql, (id,))
    conexao.commit()
    
    cursor.close()
    conexao.close()
    
    return jsonify({"mensagem": "Mago expulso do grimório com sucesso!"}), 200



if __name__ == '__main__':
    app.run(debug=True)