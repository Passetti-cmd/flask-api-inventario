import os
import sqlite3  
from flask import Flask, request, jsonify
from flask_cors import CORS

from flask import Flask, request, redirect

app = Flask(__name__)

@app.before_request
def force_http():
    """Se a requisição vier por HTTPS, redireciona para HTTP"""
    if request.url.startswith("https://"):
        new_url = request.url.replace("https://", "http://", 1)
        return redirect(new_url, code=301)


CORS(app, origins=["http://flask-env.eba-pimaq7yt.sa-east-1.elasticbeanstalk.com"])




DB_NAME = "inventario.db"


def init_db():
    try:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()  
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS computadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    fabricante TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    serial TEXT UNIQUE NOT NULL,
                    data_aquisicao TEXT NOT NULL,
                    sistema_operacional TEXT,
                    setor TEXT
                )
            """)
            conn.commit()
        print("Banco inicializado com sucesso.")
    except Exception as e:
        print("Erro ao inicializar o banco:", e)


def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  
    return conn

from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")


# Endpoint para listar computadores
@app.route('/computadores', methods=['GET'])
def listar_computadores():
    try:
        busca = request.args.get('busca', '')
        conn = get_db_connection()
        cursor = conn.cursor()  

        if busca:
            wildcard = f"%{busca}%"
            query = """
                SELECT * FROM computadores
                WHERE CAST(id as TEXT) LIKE ?
                   OR nome LIKE ?
                   OR fabricante LIKE ?
                   OR modelo LIKE ?
                   OR serial LIKE ?
                   OR sistema_operacional LIKE ?
                   OR setor LIKE ?
            """
            cursor.execute(query, (wildcard, wildcard, wildcard, wildcard, wildcard, wildcard, wildcard))
        else:
            cursor.execute("SELECT * FROM computadores")

        rows = cursor.fetchall()
        computadores = [dict(row) for row in rows]
        conn.close()
        return jsonify(computadores)
    except Exception as e:
        print("Erro ao listar computadores:", e)
        return jsonify({"erro": str(e)}), 500

# Endpoint para cadastrar um novo computador
@app.route('/computadores', methods=['POST'])
def adicionar_computador():
    try:
        data = request.get_json()
        nome = data.get("nome")
        fabricante = data.get("fabricante")
        modelo = data.get("modelo")
        serial = data.get("serial")
        data_aquisicao = data.get("data_aquisicao")
        sistema_operacional = data.get("sistema_operacional")
        setor = data.get("setor")

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            INSERT INTO computadores (nome, fabricante, modelo, serial, data_aquisicao, sistema_operacional, setor)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """
        values = (nome, fabricante, modelo, serial, data_aquisicao, sistema_operacional, setor)
        cursor.execute(query, values)
        conn.commit()
        novo_id = cursor.lastrowid
        conn.close()
        return jsonify({"id": novo_id, "mensagem": "Computador cadastrado com sucesso"}), 201
    except Exception as e:
        print("Erro ao adicionar computador:", e)
        return jsonify({"erro": str(e)}), 500

# Endpoint para obter um único computador pelo ID
@app.route('/computadores/<int:id>', methods=['GET'])
def obter_computador(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM computadores WHERE id = ?"
        cursor.execute(query, (id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return jsonify(dict(row))
        else:
            return jsonify({"erro": "Computador não encontrado"}), 404
    except Exception as e:
        print("Erro ao obter computador:", e)
        return jsonify({"erro": str(e)}), 500

# Endpoint para editar um computador existente
@app.route('/computadores/<int:id>', methods=['PUT'])
def editar_computador(id):
    try:
        data = request.get_json()
        nome = data.get("nome")
        fabricante = data.get("fabricante")
        modelo = data.get("modelo")
        serial = data.get("serial")
        data_aquisicao = data.get("data_aquisicao")
        sistema_operacional = data.get("sistema_operacional")
        setor = data.get("setor")

        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
            UPDATE computadores
            SET nome = ?, fabricante = ?, modelo = ?, serial = ?, data_aquisicao = ?,
                sistema_operacional = ?, setor = ?
            WHERE id = ?
        """
        values = (nome, fabricante, modelo, serial, data_aquisicao, sistema_operacional, setor, id)
        cursor.execute(query, values)
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Computador atualizado com sucesso"}), 200
    except Exception as e:
        print("Erro ao editar computador:", e)
        return jsonify({"erro": str(e)}), 500

# Endpoint para excluir um computador
@app.route('/computadores/<int:id>', methods=['DELETE'])
def excluir_computador(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "DELETE FROM computadores WHERE id = ?"
        cursor.execute(query, (id,))
        conn.commit()
        conn.close()
        return jsonify({"mensagem": "Computador excluído com sucesso"}), 200
    except Exception as e:
        print("Erro ao excluir computador:", e)
        return jsonify({"erro": str(e)}), 500

import os

if __name__ == "__main__":
    init_db()  # Inicializa o banco ao iniciar o servidor
    app.run(host="0.0.0.0", port=8080)  # FORÇAR A PORTA 8080
