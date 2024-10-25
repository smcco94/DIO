# Comandos Básicos do SQL

- ##### SHOW DATABASE
```SQL
SHOW DATABASES; -- EXIBE OS DB'S EXISTENTES
```

- ##### CREATE DATABASE
```SQL
CREATE DATABASE RegistrodePublicacoes; -- CRIA UM DB CHAMADO RegistrodePublicacoes
```

- ##### USE DATABASE
```SQL
USE RegistrodePublicacoes; -- ACESSA UM DB CHAMADO RegistrodePublicacoes
```

- ##### SHOW TABLES
```SQL
SHOW TABLES; -- EXIBE AS TABELAS DE UM DB ACESSADO
```

- ##### DROP DATABASE
```SQL
DROP RegistrodePublicacoes; -- DELETA UM DB CHAMADO RegistrodePublicacoes
```

- ##### CREATE TABLE
```SQL
CREATE TABLE nome_tabela (
    id INT AUTO_INCREMENT PRIMARY KEY, -- Cria a coluna 'id' como um inteiro. Essa coluna é auto-incrementada, o que significa que seu valor será gerado automaticamente a cada nova inserção. É também definida como chave primária (PRIMARY KEY), garantindo que seus valores sejam únicos e não nulos. A PK também poderia ser indicada em uma nova linha. Ex: PRIMARY KEY (id)
    nome_periodico VARCHAR(20), -- Cria a coluna 'nome_periodico' como tipo VARCHAR, permitindo armazenar strings de até 20 caracteres. Essa coluna armazenará o nome do periódico.
    issn VARCHAR(9) UNIQUE, -- Cria a coluna 'issn' como tipo VARCHAR, permitindo armazenar strings de até 9 caracteres (padrão para ISSN). A restrição UNIQUE garante que todos os valores na coluna 'issn' sejam exclusivos, ou seja, não podem se repetir.
    id_editora INT, -- Cria a coluna 'id_editora' como um inteiro, que será usado para armazenar a referência à editora do periódico.
    FOREIGN KEY (id_editora) REFERENCES outra_tabela(id) -- Define 'id_editora' como uma chave estrangeira (FOREIGN KEY), que faz referência à coluna 'id' de 'outra_tabela'. Isso estabelece um relacionamento entre as tabelas, garantindo que os valores em 'id_editora' correspondam a valores válidos em 'outra_tabela'.
);
```

- ##### ALTER TABLE
```SQL
ALTER TABLE nome_tabela ADD CONSTRAINT nome_regra FOREIGN KEY (fk_tabela) REFERENCES tabela_referenciada(fk_tabela);
-- ESSE TRECHO ADICIONA UMA RESTRIÇÃO DE CHAVE ESTRANGEIRA, ESTABELECENDO UMA REFERÊNCIA ENTRE A COLUNA 'fk_tabela' DE 'nome_tabela' E A COLUNA 'fk_tabela' DA 'tabela_referenciada', INDICANDO QUE 'fk_tabela' EM 'nome_tabela' DEVE SE REFERIR A UM VALOR EXISTENTE EM 'tabela_referenciada'.
```

- ##### INSERT INTO
```SQL
INSERT INTO nome_tabela (coluna1, coluna_2) VALUES ('IEEE', 'EUA'), ('DataScienceMagazine', 'EUA');
-- ESSE TRECHO INSERE DOIS NOVOS REGISTROS NA TABELA 'nome_tabela', ALOCAANDO 'IEEE' NA 'coluna1' E 'EUA' NA 'coluna_2' PARA O PRIMEIRO REGISTRO, E 'DataScienceMagazine' NA 'coluna1' E 'EUA' NA 'coluna_2' PARA O SEGUNDO REGISTRO, PERMITINDO A ADIÇÃO DE MÚLTIPLOS VALORES EM UMA ÚNICA OPERAÇÃO.
```

- ##### @@ERROR
```SQL
INSERT INTO nome_tabela (coluna1, coluna_2) 
VALUES ('IEEE', 'EUA'); -- TENTA INSERIR UM NOVO REGISTRO NA TABELA

IF @@ERROR <> 0 
BEGIN
    PRINT 'Erro: Genérico'; 
END
```

- ##### BEGIN TRY || BEGIN CATCH
```SQL
BEGIN TRY
    INSERT INTO nome_tabela (coluna1, coluna_2) 
    VALUES ('IEEE', 'EUA'); -- TENTA INSERIR UM NOVO REGISTRO NA TABELA
END TRY

BEGIN CATCH
    -- SE OCORRER UM ERRO (EXEMPLO: VIOLACAO DE RESTRIÇÃO UNIQUE), EXECUTA ESTE BLOCO
    PRINT 'Erro: + ERROR_MESSAGE()'; 
END CATCH;
```

