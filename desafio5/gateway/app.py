from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

#Obtém as urls através de variáveis de ambiente
USERS_URL = os.getenv("USERS_URL", "http://users-service:5001/users")
ORDERS_URL = os.getenv("ORDERS_URL", "http://orders-service:5002/orders")

#Rota /users
#Faz uma requisição ao users-service e retorna os usuários obtidos
@app.route("/users")
def get_users():
    resp = requests.get(USERS_URL)
    return jsonify(resp.json())

#Rota /orders
#Faz uma requisição ao orders-service e retorna os pedidos obtidos
@app.route("/orders")
def get_orders():
    resp = requests.get(ORDERS_URL)
    return jsonify(resp.json())

#Cria a home e documenta as outras rotas mapeadas
@app.route("/")
def home():
    return jsonify({
        "routes": {
            "/users": "Retorna lista de usuários",
            "/orders": "Retorna lista de pedidos"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
