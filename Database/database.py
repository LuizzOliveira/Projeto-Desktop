import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",  
        password="",  
        database="sistema_login"
    )

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            email VARCHAR(100) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL
        )
    """)
    conexao.commit()
    cursor.close()
    conexao.close()

if __name__ == "__main__":
    criar_tabela()
