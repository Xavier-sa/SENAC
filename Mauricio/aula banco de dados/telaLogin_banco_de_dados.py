import sys;
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout, QHBoxLayout,QMessageBox
from hashlib import sha256
import mysql.connector

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        layout = QVBoxLayout()

        h_layout = QHBoxLayout()
        label = QLabel("Login")
        label.setStyleSheet("font-size: 24px; font-weight: bold;")
        h_layout.addStretch(1)
        h_layout.addWidget(label)
        h_layout.addStretch(1)

        layout.addLayout(h_layout)

        email_label = QLabel("Email:")
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Digite seu email")
        layout.addWidget(email_label)
        layout.addWidget(self.email_input)

        senha_label = QLabel("Senha:")
        self.senha_input = QLineEdit()
        self.senha_input.setPlaceholderText("Digite seu senha")
        self.senha_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(senha_label)
        layout.addWidget(self.senha_input)
        login_button = QPushButton("Login")
        login_button.clicked.connect(self.handle_Login)#TODO
        layout.addWidget(login_button)

        self.setLayout(layout)

    def conectar_banco(self):
        try:
            conn = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "",
                database = "meu_banco"
            )
            return conn
        except mysql.connector.error as err:
            QMessageBox.critical(self, "Erro de conexão", f"Erro ao connectar: {err}")
            return None
    
    def validar_login(self, email, senha):
        conn = self.conectar_banco()
        if conn is None:
            return False
        
        cursor = conn.cursor()
        senha_hash = sha256(senha.encode()).hexdigest()

        query = "SELECT * FROM Usuario WHERE email = %s AND senha = %s"
        cursor.execute(query, (email, senha_hash))

        result = cursor.fetchone()
        cursor.close()
        conn.close()
        if result:
            return True
        else:
            return False
    def handle_Login(self):
        email = self.email_input.text()
        senha = self.senha_input.text()

        if self.validar_login(email, senha):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
        else:
            QMessageBox.information(self, "Erro", "Email ou senha invalida.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

