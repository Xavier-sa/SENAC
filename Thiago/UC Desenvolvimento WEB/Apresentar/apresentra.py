import sys
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QStackedWidget, QLineEdit, QTextEdit)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap

class PageOne(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.text = QLabel("\n\t Casa do Mestre Kame (SERVIDOR WEB)\n ")
        self.text.setAlignment(Qt.AlignCenter)
        
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap("semente.jpg"))  # Substitua pelo caminho da sua imagem
        
        self.button_to_page_two = QPushButton("Ir para a Página de Pedidos")
        self.button_to_page_two.clicked.connect(self.go_to_page_two)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.image_label)  
        self.layout.addWidget(self.button_to_page_two)
        self.setLayout(self.layout)
        
    @Slot()
    def go_to_page_two(self):
        self.parent().setCurrentIndex(1)

class PageTwo(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.text = QLabel("\n\t Faça um Pedido de Informações\n ")
        self.text.setAlignment(Qt.AlignCenter)
        
        self.request_input = QLineEdit()
        self.request_input.setPlaceholderText("Digite seu pedido aqui...")
        
        self.submit_button = QPushButton("Enviar Pedido")
        self.submit_button.clicked.connect(self.process_request)
        
        self.response_text = QTextEdit()
        self.response_text.setReadOnly(True)
        
        self.button_to_page_one = QPushButton("Voltar para a Casa do Mestre Kame")
        self.button_to_page_one.clicked.connect(self.go_to_page_one)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.request_input)
        self.layout.addWidget(self.submit_button)
        self.layout.addWidget(self.response_text)
        self.layout.addWidget(self.button_to_page_one)
        self.setLayout(self.layout)
        
    @Slot()
    def process_request(self):
        pedido = self.request_input.text().lower()
        respostas = {
            "senzu bean": "Você recebeu um Senzu Bean!",
            "kamehameha": "Aqui está a técnica do Kamehameha!",
            "dragon ball": "Você encontrou uma Dragon Ball!",
            "": "Por favor, faça um pedido válido."
        }
        
        resposta = respostas.get(pedido, "Item não encontrado.")
        self.response_text.setText(resposta)
        
    @Slot()
    def go_to_page_one(self):
        self.parent().setCurrentIndex(0)

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.stacked_widget = QStackedWidget()
        
        self.page_one = PageOne(self.stacked_widget)
        self.page_two = PageTwo(self.stacked_widget)
        
        self.stacked_widget.addWidget(self.page_one)
        self.stacked_widget.addWidget(self.page_two)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stacked_widget)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)  # Ajuste o tamanho conforme necessário
    widget.show()

    sys.exit(app.exec())
