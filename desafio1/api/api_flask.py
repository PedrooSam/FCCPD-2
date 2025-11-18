from flask import Flask, jsonify

#Cria o app flask
app = Flask(__name__)

#Cria uma rota que retorna uma mensagem padrão para as requisições
@app.route('/')
def home():
    return jsonify({"mensagem": "Olá do container Flask!"})

#Roda o app na porta 8080
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)