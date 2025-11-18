#Pega a imagem python 3.10 do dockerhub
FROM python:3.10-slim

#Cria o diretório de trabalho /app no container
WORKDIR /app

#Copia os requirements para o container
COPY requirements.txt .

#intala as dependências no container
RUN pip install -r requirements.txt

#Copia o script python para o container
COPY cliente.py .

#Comandos para executar o script
CMD ["python", "cliente.py"]