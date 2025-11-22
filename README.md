# FCCPD-2

Este repositório consiste na implementação dos 5 desafios do projeto da segunda unidade da cadeira de FCCPD.
Todos os códigos e arquivos estão com comentários explicando detalhadamente o que cada parte do projeto faz, e nas sessões seguintes do README, há uma explicação sobre o contexto do projeto e como rodar cada um deles.

## Desafio 1
Este desafio consiste em criar dois containers que se comunicam entre si, onde um roda uma API e outro envia requisições a cada 5 minutos e printa as respostas.

- Estrutura
```
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
```

- Como rodar:

Primeiramente, entre na pasta do desafio 1
```
cd desafio1
```

Crie uma rede em docker
```
docker network create minha-rede
```

Construa e execute o container da API
```
docker build -t api-flask ./api
```
```
docker run -d --name servidor --network minha-rede -p 8080:8080 api-flask
```

Construa e execute o container cliente
```
docker build -t cliente-http ./cliente
```
```
docker run -d --name cliente --network minha-rede cliente-http
```

Para verificar a conexão, rode
```
docker logs -f cliente
```


## Desafio 2
Este desafio consiste em demonstrar o uso de volumes Docker para garantir que dados de um banco permaneçam mesmo após a remoção do container.

- Estrutura
```
desafio2/
│
├── docker-compose.yml
├── init.sql
└── README.md
```

- Como rodar

Primeiramente, entre na pasta do desafio 2
```
cd desafio2
```

Suba os containers
```
docker compose up -d
```

Entrar no container do cliente
```
docker exec -it desafio2-client bash
```

Acessar banco (senha: admin)
```
psql -h db -U admin -d teste
```

Verificar dados (deve haver Pedro e Maria)
```
SELECT * FROM usuarios;
```

PARA TESTAR A PERSISTENCIA

Em outro terminal, remova o container iniciado
```
docker compose down
```

Suba-o novamente
```
docker compose up -d
```

Verifique os dados novamente
```
docker exec -it desafio2-client bash
```
```
psql -h db -U admin -d teste
```
```
SELECT * FROM usuarios;
```