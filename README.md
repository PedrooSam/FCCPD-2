# FCCPD-2

Este repositório consiste na implementação dos 5 desafios do projeto da segunda unidade da cadeira de FCCPD.
Todos os códigos e arquivos estão com comentários explicando detalhadamente o que cada parte do projeto faz, e nas sessões seguintes do README, há uma explicação sobre o contexto do projeto e como rodar cada um deles.

## Desafio 1
Este desafio consiste em criar dois containers que se comunicam entre si, onde um roda uma API e outro envia requisições a cada 5 minutos e printa as respostas.

- Estrutura

desafio1/
 │
 ├── api/
 │    ├── api_flask.py
 │    ├── requirements.txt
 │    └── Dockerfile
 │
 └── cliente/
      ├── requisicoes.py
      ├── requirements.txt
      └── Dockerfile

- Como rodar:
Crie uma rede em docker
```
docker network create minha-rede
```

Construa e execute o container da API
´´´
docker build -t api-flask ./api
´´´
´´´
docker run -d --name servidor --network minha-rede -p 8080:8080 api-flask
´´´

Construa e execute o container cliente
´´´
docker build -t cliente-http ./cliente
´´´
´´´
docker run -d --name cliente --network minha-rede cliente-http
´´´

Para verificar a conexão, rode
´´´
docker logs -f cliente
´´´