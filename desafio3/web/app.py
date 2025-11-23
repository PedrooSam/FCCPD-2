from flask import Flask, jsonify
import os
import psycopg2
import redis
import time

app = Flask(__name__)

#Função para conectar no banco de dados
def connect_db():
    retries = 10

    #Define um número de tentativas, pois o banco demora mais que a aplicação para ficar online
    while retries > 0:
        try:
            conn = psycopg2.connect(
                host=os.getenv("DATABASE_HOST"),
                user=os.getenv("DATABASE_USER"),
                password=os.getenv("DATABASE_PASSWORD"),
                dbname=os.getenv("DATABASE_NAME")
            )
            print("Conectado ao banco!")
            return conn
        except psycopg2.OperationalError:
            retries -= 1
            print("Banco ainda não está pronto, tentando novamente...")
            time.sleep(2)
    raise Exception("Não foi possível conectar ao banco após várias tentativas.")

db_conn = connect_db()

#Redis
cache = redis.Redis(host=os.getenv("REDIS_HOST"), port=6379)

@app.route("/")
def home():
    #Incrementa contador no Redis
    cache.incr("visits")

    #Lê contador
    visits = cache.get("visits").decode()

    #Lê algo do banco de dados
    cursor = db_conn.cursor()
    cursor.execute("SELECT NOW();") 
    timestamp = cursor.fetchone()[0]
    cursor.close()

    #Json de retorno padrão
    return jsonify({
        "message": "Serviço Web funcionando!",
        "visits": visits,
        "database_time": str(timestamp)
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
