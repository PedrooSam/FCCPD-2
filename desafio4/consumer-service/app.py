from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

#Obter a url através de variáveis de ambiente
USERS_SERVICE_URL = os.getenv("USERS_SERVICE_URL", "http://users-service:5000/users")

#Cria a rota /info
@app.route("/info")
def info():
    try:
        #Faz uma requisição à url
        resp = requests.get(USERS_SERVICE_URL)
        users = resp.json()

        #Processa os dados
        processed = [
            f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
            for u in users
        ]

        #Retorna um json com os dados tratados
        return jsonify({"users": processed})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000)
