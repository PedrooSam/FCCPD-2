from flask import Flask, jsonify

app = Flask(__name__)

#Cria a rota /orders que retorna um json mockado com pedidos
@app.route("/orders")
def orders():
    return jsonify([
        {"order_id": 101, "user_id": 1, "produto": "Teclado"},
        {"order_id": 102, "user_id": 2, "produto": "Mouse"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
