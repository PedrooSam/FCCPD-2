import time
import requests

#Url da API, o nome do container que roda a API deve ser servidor
API_URL = "http://servidor:8080/"

#Loop para fazer as requisições a cada 5 segundos
while True:

    #Faz uma requisição get para a API e printa a mensagem, caso dê erro, printa e continua para a próxima requisição
    try:
        response = requests.get(API_URL)
        print("[CLIENTE] Resposta recebida:", response.json())
    except Exception as e:
        print("[CLIENTE] Erro ao conectar:", e)

    
    time.sleep(5)
