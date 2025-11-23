#Imagem pyhton
FROM python:3.11-slim

#Diretório de trabalho do container
WORKDIR /app

#Copia e intala o requirements.txt
COPY requirements.txt .
RUN pip install -r requirements.txt

#Copia o arquivo python
COPY app.py .

#Roda o arquivo
CMD ["python", "app.py"]
