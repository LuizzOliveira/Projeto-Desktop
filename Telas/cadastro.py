import re
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from Database.database import conectar

class TelaCadastro(QWidget):
    def __init__(self, tela_login):
        super().__init__()
        self.tela_login = tela_login
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Cadastro")
        self.setGeometry(100, 100, 450, 550)
        self.setStyleSheet("background-color: #D3D3D3;")

        self.label_usuario = QLabel("Usuário:", self)
        self.label_usuario.setGeometry(75, 50, 300, 20)

        self.input_usuario = QLineEdit(self)
        self.input_usuario.setGeometry(75, 70, 300, 30)

        self.label_email = QLabel("E-mail:", self)
        self.label_email.setGeometry(75, 110, 300, 20)

        self.input_email = QLineEdit(self)
        self.input_email.setGeometry(75, 130, 300, 30)

        self.label_cpf = QLabel("CPF (apenas números):", self)
        self.label_cpf.setGeometry(75, 170, 300, 20)

        self.input_cpf = QLineEdit(self)
        self.input_cpf.setGeometry(75, 190, 300, 30)

        self.label_senha = QLabel("Senha:", self)
        self.label_senha.setGeometry(75, 230, 300, 20)

        self.input_senha = QLineEdit(self)
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_senha.setGeometry(75, 250, 300, 30)

        self.label_repetir_senha = QLabel("Repetir Senha:", self)
        self.label_repetir_senha.setGeometry(75, 290, 300, 20)

        self.input_repetir_senha = QLineEdit(self)
        self.input_repetir_senha.setEchoMode(QLineEdit.EchoMode.Password)
        self.input_repetir_senha.setGeometry(75, 310, 300, 30)

        self.btn_cadastrar = QPushButton("Cadastrar", self)
        self.btn_cadastrar.setGeometry(75, 360, 300, 40)
        self.btn_cadastrar.setStyleSheet("background-color: green; color: white;")
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)

        self.btn_voltar = QPushButton("Voltar", self)
        self.btn_voltar.setGeometry(75, 420, 300, 30)
        self.btn_voltar.setStyleSheet("background-color: red; color: white;")
        self.btn_voltar.clicked.connect(self.voltar_tela_login)

    def cadastrar_usuario(self):
        username = self.input_usuario.text().strip()
        email = self.input_email.text().strip()
        cpf = self.input_cpf.text().strip()
        senha = self.input_senha.text().strip()
        repetir_senha = self.input_repetir_senha.text().strip()

        if not username or not email or not cpf or not senha or not repetir_senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        cpf = re.sub(r'\D', '', cpf)

        if len(cpf) != 11:
            QMessageBox.warning(self, "Erro", "CPF inválido. Digite apenas números.")
            return

        if senha != repetir_senha:
            QMessageBox.warning(self, "Erro", "As senhas não coincidem.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        try:
            sql = "INSERT INTO usuarios (username, email, cpf, password_hash) VALUES (%s, %s, %s, SHA2(%s, 256))"
            cursor.execute(sql, (username, email, cpf, senha))
            conexao.commit()
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.voltar_tela_login()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao cadastrar: {str(e)}")
        finally:
            cursor.close()
            conexao.close()

    def voltar_tela_login(self):
        self.tela_login.show()
        self.close()