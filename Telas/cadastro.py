import re
from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
from Database.database import conectar

class TelaCadastro(QWidget):
    def __init__(self, tela_login):
        super().__init__()
        self.tela_login = tela_login
        self.initUI()
        self.setWindowIcon(QIcon("Img/cadastro.png"))
        self.showMaximized()

    def initUI(self):
        self.setWindowTitle("Cadastro")
        self.setStyleSheet("background-color: #D3D3D3;")

        self.label_usuario = QLabel("Usuário:", self)
        self.input_usuario = QLineEdit(self)

        self.label_email = QLabel("E-mail:", self)
        self.input_email = QLineEdit(self)

        self.label_cpf = QLabel("CPF (apenas números):", self)
        self.input_cpf = QLineEdit(self)

        self.label_senha = QLabel("Senha:", self)
        self.input_senha = QLineEdit(self)
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.label_repetir_senha = QLabel("Repetir Senha:", self)
        self.input_repetir_senha = QLineEdit(self)
        self.input_repetir_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_cadastrar = QPushButton("Cadastrar", self)
        self.btn_cadastrar.setStyleSheet("background-color: green; color: white;")
        self.btn_cadastrar.clicked.connect(self.cadastrar_usuario)

        self.btn_voltar = QPushButton("Voltar", self)
        self.btn_voltar.setStyleSheet("background-color: red; color: white;")
        self.btn_voltar.clicked.connect(self.voltar_tela_login)

    def resizeEvent(self, event):
        largura = self.width()
        altura = self.height()

        self.label_usuario.setGeometry(largura // 2 - 150, altura // 6, 300, 20)
        self.input_usuario.setGeometry(largura // 2 - 150, altura // 6 + 20, 300, 30)
        self.label_email.setGeometry(largura // 2 - 150, altura // 6 + 60, 300, 20)
        self.input_email.setGeometry(largura // 2 - 150, altura // 6 + 80, 300, 30)
        self.label_cpf.setGeometry(largura // 2 - 150, altura // 6 + 120, 300, 20)
        self.input_cpf.setGeometry(largura // 2 - 150, altura // 6 + 140, 300, 30)
        self.label_senha.setGeometry(largura // 2 - 150, altura // 6 + 180, 300, 20)
        self.input_senha.setGeometry(largura // 2 - 150, altura // 6 + 200, 300, 30)
        self.label_repetir_senha.setGeometry(largura // 2 - 150, altura // 6 + 240, 300, 20)
        self.input_repetir_senha.setGeometry(largura // 2 - 150, altura // 6 + 260, 300, 30)
        self.btn_cadastrar.setGeometry(largura // 2 - 150, altura // 6 + 310, 300, 40)
        self.btn_voltar.setGeometry(largura // 2 - 150, altura // 6 + 360, 300, 30)

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