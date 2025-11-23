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

- O que cada item faz?

A pasta api/ possui os arquivos de configuração da api</br>
      - api_flask.py: código python que sobe uma api usando o flask</br>
      - requirements.txt: dependências do arquivo api_flask.py</br>
      - Dockerfile: configurações para subir o container</br>
</br>
A pasta cliente/ possui os arquivos de configuração da do cliente</br>
      - requisicoes.py: código python que envia requisições periódicas a api</br>
      - requirements.txt: dependências do arquivo requisicoes.py</br>
      - Dockerfile: configurações para subir o container</br>
</br>
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

- O que cada item faz?</br>
O arquivo Docker-compose.yaml sobe um banco PostgreSQL</br>
      - Usa variáveis de ambiente para configurar acesso</br>
      - Usa volume dbdata para que os dados NÃO sumam após recriar o container</br>
      - Executa automaticamente o arquivo init.sql</br>
      - Expõe a porta 5432</br>
</br>
Também cria um cliente</br>
      - É um container auxiliar</br>
      - Permite rodar comandos psql sem instalar nada na máquina</br>
      - Fica “rodando parado” para você entrar nele quando quiser</br>
</br>
E define o volume dbdata</br>
      - Onde os dados verdadeiramente ficam</br>
      - Sobrevive mesmo após docker compose down</br>
</br>
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

## Desafio 3
Este desafio consiste em orquestrar três serviços usando Docker Compose: um serviço web (API Flask), um banco de dados PostgreSQL e um serviço de cache Redis. O objetivo é demonstrar como o Compose gerencia dependências, redes internas e variáveis de ambiente para integrar múltiplos serviços.

- Estrutura
```
desafio3/
 │
 ├── web/
 │    ├── app.py
 │    ├── requirements.txt
 │    └── Dockerfile
 │
 └── docker-compose.yml
```

- O que cada item faz?</br>

A pasta web/ possui os arquivos do serviço web</br>
      - app.py: código Python que sobe uma API Flask e se conecta ao PostgreSQL e Redis</br>
      - requirements.txt: dependências necessárias para o serviço web</br>
      - Dockerfile: instruções para construir a imagem do serviço web</br>
</br>
O arquivo docker-compose.yml configura os três serviços:</br>
      - web: serviço Flask que depende do db e do cache</br>
      - db: container PostgreSQL com volume para persistência</br>
      - cache: container Redis usado como sistema de cache</br>
</br>
- Como rodar:

Primeiramente, entre na pasta do desafio 3
```
cd desafio3
```

Inicie os serviços usando o compose
```
docker compose up --build
```

Após subir os serviços, acesse no navegador:
```
http://localhost:8080
```

Para acompanhar logs do serviço web:
```
docker logs -f desafio3-web
```

Para parar todos os containers:
```
docker compose down
```

## Desafio 4
Este desafio consiste em criar dois microsserviços independentes que se comunicam entre si via HTTP, sem API Gateway. Um microsserviço fornece uma lista de usuários, enquanto o outro consome esses dados e retorna informações processadas.

- Estrutura
```
desafio4/
 │
 ├── users-service/
 │   ├── app.py
 │   ├── requirements.txt
 │   └── Dockerfile
 │
 ├── consumer-service/
 │   ├── app.py
 │   ├── requirements.txt
 │   └── Dockerfile
 │
 └── docker-compose.yml
```

- O que cada item faz?</br>

A pasta users-service/ contém o microsserviço que retorna a lista de usuários</br>
      - app.py: código Python que sobe uma API Flask com endpoint /users</br>
      - requirements.txt: dependências utilizadas pelo microsserviço</br>
      - Dockerfile: configurações para montar o container do users-service</br>
</br>
A pasta consumer-service/ contém o microsserviço que consome o serviço de usuários</br>
      - app.py: código Python que envia uma requisição HTTP ao users-service e processa os dados</br>
      - requirements.txt: dependências utilizadas pelo microsserviço</br>
      - Dockerfile: configurações necessárias para montar o container do consumer-service</br>
</br>
O arquivo docker-compose.yml orquestra ambos os microsserviços</br>
      - Define rede, dependências e mapeamento de portas</br>
      - Garante que o consumer-service só inicie após o users-service</br>
</br>

Como rodar:

Primeiramente, entre na pasta do desafio 4:
```
cd desafio4
```

Construa e execute os dois microsserviços:
```
docker compose up --build
```

Após subir os serviços, teste cada endpoint em seu navegador

Para acessar o microsserviço de usuários:
```
http://localhost:5000/users
```

Para acessar o microsserviço consumidor:
```
http://localhost:6000/info
```

Para acompanhar os logs de cada serviço:
```
docker logs -f users-service
```
```
docker logs -f consumer-service
```

Para parar tudo:
```
docker compose down
```