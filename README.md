# 📌 Sistema de Login com PyQt6 e MySQL

Este projeto é um sistema de login e cadastro desenvolvido em **Python** com a biblioteca **PyQt6** para a interface gráfica e **MySQL** para o banco de dados.

## 📥 Requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 3.10+
- MySQL Server
- Pip

### 📦 Instalar dependências
Execute o seguinte comando para instalar todas as bibliotecas necessárias:
```sh
pip install PyQt6 mysql-connector-python
```

## 🛠 Configuração do Banco de Dados

### 📌 Criando o Banco de Dados e a Tabela de Usuários

Antes de rodar o projeto, crie o banco de dados e a tabela de usuários executando a seguinte query no MySQL:

```sql
CREATE DATABASE sistema_login;

USE sistema_login;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(64) NOT NULL
);
```

## 🚀 Executando o Projeto

1. Clone o repositório ou baixe os arquivos:
```sh
git clone https://github.com/seu-repositorio/sistema-login.git
cd sistema-login
```
2. Configure a conexão com o MySQL no arquivo `Database/database.py`:
```python
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="seu_usuario",
        password="sua_senha",
        database="sistema_login"
    )
```
3. Execute o arquivo `main.py`:
```sh
python main.py
```

## 📌 Estrutura do Projeto
```
📂 Projeto Login
│── 📂 Database
│   ├── database.py  # Conexão com o banco de dados
│── 📂 Telas
│   ├── login.py      # Tela de login
│   ├── cadastro.py   # Tela de cadastro
│── main.py          # Arquivo principal
│── README.md        # Documentação do projeto
```

## 🔥 Funcionalidades
- ✅ Tela de login com autenticação por **usuário e senha**
- ✅ Cadastro de novos usuários com **CPF, e-mail e senha**
- ✅ Senha armazenada de forma segura com **hashing SHA-256**
- ✅ Design moderno usando **PyQt6**

## 📌 Autor
Desenvolvido por **Luiz Henrique** 🚀