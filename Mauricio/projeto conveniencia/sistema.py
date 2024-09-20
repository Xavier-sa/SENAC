import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QTextEdit, QHBoxLayout, QListWidget
)

class LoginScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Tela de Login")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Usuário:")
        self.username_input = QLineEdit()

        self.password_label = QLabel("Senha:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)

        self.login_button = QPushButton("Entrar")
        self.login_button.clicked.connect(self.handle_login)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username == "black" and password == "senha":  
            self.parent.setCentralWidget(SalesScreen(self.parent))
        else:
            QMessageBox.warning(self, "Erro", "Usuário ou senha incorretos.")


class SalesScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Tela de Vendas")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.sales_label = QLabel("Vendas:")
        self.product_list = QListWidget()

        
        self.sell_button = QPushButton("Registrar Venda")
        self.sell_button.clicked.connect(self.register_sale)
        
        self.stock_button = QPushButton("Gerenciar Estoque")
        self.stock_button.clicked.connect(self.open_stock_management)

        layout.addWidget(self.sales_label)
        layout.addWidget(self.product_list)
        layout.addWidget(self.sell_button)
        layout.addWidget(self.stock_button)

        self.setLayout(layout)

    def register_sale(self):
        if not self.product_list.selectedItems():
            QMessageBox.warning(self, "Erro", "Selecione um produto para vender.")
            return
        product = self.product_list.currentItem().text()
        QMessageBox.information(self, "Venda Registrada", f"Venda registrada para {product}.")
    
    def open_stock_management(self):
        self.parent.setCentralWidget(StockManagementScreen(self.parent))


class StockManagementScreen(QWidget):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setWindowTitle("Gerenciamento de Estoque")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.stock_label = QLabel("Gerenciar Estoque:")
        self.product_list = QListWidget()
        self.product_list.addItems(["Coca-Cola", "Heineken"])  

        self.add_product_input = QLineEdit()
        self.add_product_input.setPlaceholderText("Nome do novo produto")

        self.add_button = QPushButton("Adicionar Produto")
        self.add_button.clicked.connect(self.add_product)

        layout.addWidget(self.stock_label)
        layout.addWidget(self.product_list)
        layout.addWidget(self.add_product_input)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def add_product(self):
        new_product = self.add_product_input.text()
        if new_product:
            self.product_list.addItem(new_product)
            self.add_product_input.clear()
            QMessageBox.information(self, "Produto Adicionado", f"{new_product} adicionado ao estoque.")
        else:
            QMessageBox.warning(self, "Erro", "Digite um nome de produto.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistema de Conveniência")
        self.setGeometry(100, 100, 300, 200)

        self.setCentralWidget(LoginScreen(self))

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
