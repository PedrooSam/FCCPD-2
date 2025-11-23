from flask import Flask, jsonify

app = Flask(__name__)

#Cria a rota /users
@app.route("/users")
def users():
    #Retorna um json padrão com usuários mockados
    return jsonify([
        {"id": 1, "nome": "Pedro"},
        {"id": 2, "nome": "Maria"}
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
