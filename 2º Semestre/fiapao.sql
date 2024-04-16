-- Criando tabela
DROP TABLE PETSHOP;
CREATE TABLE PETSHOP(
    ID NUMBER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    tipo_pet VARCHAR(30),
    nome_pet VARCHAR(30),
    idade INT
);


-- Cadastro
INSERT INTO PETSHOP (tipo_pet, nome_pet, idade)
VALUES ('gato', 'Bianca', 2);


-- Consulta
SELECT nome_pet, tipo_pet FROM PETSHOP;


-- Atualizar
UPDATE PETSHOP SET idade = 3, tipo_pet = 'demonio';


-- DELETE FROM <tabela>
-- WHERE <condição>



