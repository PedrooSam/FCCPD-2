CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100)
);

INSERT INTO usuarios (nome) VALUES ('Pedro');
INSERT INTO usuarios (nome) VALUES ('Maria');