from flask import Flask, jsonify

app = Flask(__name__)

#Cria a rota /users na aplicação web
@app.route("/users")
def users():
    #Retorna um Json mockado com dois usuários 
    return jsonify([
        {"id": 1, "nome": "Pedro", "ativo_desde": "2023"},
        {"id": 2, "nome": "Maria", "ativo_desde": "2021"},
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
