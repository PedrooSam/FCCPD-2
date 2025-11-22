--Cria a tabela de usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);

--Adiciona dois usuários à tabela
INSERT INTO usuarios (nome) VALUES ('Pedro');
INSERT INTO usuarios (nome) VALUES ('Maria');