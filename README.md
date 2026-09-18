# 📋 Sistema de Cadastro de Usuários com Python e SQLite

Projeto desenvolvido em **Python** com integração ao banco de dados **SQLite**, com o objetivo de praticar conceitos de **Programação Orientada a Objetos (POO)**, manipulação de bancos de dados e comandos SQL.

O sistema funciona através do terminal e permite cadastrar usuários e visualizar os registros armazenados no banco de dados.

## 🚀 Funcionalidades

- Criação automática do banco de dados
- Criação da tabela de usuários
- Cadastro de novos usuários
- Armazenamento de nome, e-mail e telefone
- Consulta dos usuários cadastrados
- Menu interativo no terminal
- Persistência dos dados utilizando SQLite

## 🛠️ Tecnologias utilizadas

- Python
- SQLite
- SQL
- Programação Orientada a Objetos (POO)

## 🗃️ Estrutura do banco de dados

O projeto utiliza uma tabela chamada `usuarios` com a seguinte estrutura:

| Campo | Tipo | Descrição |
|------|------|-----------|
| id | INTEGER | Identificador único do usuário |
| nome | TEXT | Nome do usuário |
| email | TEXT | E-mail do usuário |
| numero | TEXT | Número de telefone |

O campo `id` é utilizado como chave primária da tabela.

## 💻 Operações SQL utilizadas

Durante o desenvolvimento foram utilizadas operações como:

### Criação da tabela

```sql
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    numero TEXT
);

INSERT INTO usuarios (nome, email, numero)
VALUES (?, ?, ?);

SELECT * FROM usuarios;
