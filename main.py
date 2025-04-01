import sys
from PyQt6.QtWidgets import QApplication
from Telas.login import TelaLogin

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TelaLogin()
    window.show()
    sys.exit(app.exec())