from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtCore import Qt
from Database.database import conectar
from Telas.cadastro import TelaCadastro

class TelaLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setWindowIcon(QIcon("Img/image.png"))
        self.showMaximized()

    def initUI(self):
        self.setWindowTitle("Login Administrador")
        self.setStyleSheet("background-color: #D3D3D3;")

        self.label_icone = QLabel(self)
        self.label_icone.setPixmap(QPixmap("Img/image.png"))
        self.label_icone.setScaledContents(True)

        self.label_titulo = QLabel("", self)
        self.label_titulo.setStyleSheet("font-size: 16px; font-weight: bold;")

        self.label_usuario = QLabel("Usuário:", self)
        self.input_usuario = QLineEdit(self)

        self.label_senha = QLabel("Senha:", self)
        self.input_senha = QLineEdit(self)
        self.input_senha.setEchoMode(QLineEdit.EchoMode.Password)

        self.btn_login = QPushButton("Login", self)
        self.btn_login.setStyleSheet("background-color: green; color: white;")
        self.btn_login.clicked.connect(self.fazer_login)

    def resizeEvent(self, event):
        largura = self.width()
        altura = self.height()

        self.label_icone.setGeometry(largura // 2 - 50, altura // 6, 100, 100)
        self.label_titulo.setGeometry(largura // 2 - 100, altura // 6 + 110, 200, 30)
        self.label_usuario.setGeometry(largura // 2 - 150, altura // 3, 300, 20)
        self.input_usuario.setGeometry(largura // 2 - 150, altura // 3 + 20, 300, 30)
        self.label_senha.setGeometry(largura // 2 - 150, altura // 3 + 60, 300, 20)
        self.input_senha.setGeometry(largura // 2 - 150, altura // 3 + 80, 300, 30)
        self.btn_login.setGeometry(largura // 2 - 150, altura // 3 + 130, 300, 40)

    def fazer_login(self):
        usuario = self.input_usuario.text().strip()
        senha = self.input_senha.text().strip()

        if not usuario or not senha:
            QMessageBox.warning(self, "Erro", "Preencha todos os campos.")
            return

        conexao = conectar()
        cursor = conexao.cursor()

        sql = "SELECT * FROM usuarios WHERE username = %s AND password_hash = SHA2(%s, 256)"
        cursor.execute(sql, (usuario, senha))
        usuario_encontrado = cursor.fetchone()

        cursor.close()
        conexao.close()

        if usuario_encontrado:
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.abrir_tela_cadastro()
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")

    def abrir_tela_cadastro(self):
        self.tela_cadastro = TelaCadastro(self)
        self.tela_cadastro.show()
        self.close()