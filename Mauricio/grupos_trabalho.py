import sys
import random

from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Bem Vindo Xavier!", "Vamos começar?", "If-\n Oque deseja fazer?", "Else-\nOk,Vamos encerrar e ir pro intervalo!\n "]

        self.button = QPushButton("Clique aqui!")
        self.text = QLabel("Wellington Aparecido Santos Xavier...")
        self.text.setAlignment(Qt.AlignCenter)

       
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_label.setPixmap(QPixmap("Mauricio/broly.webp"))  

        

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.image_label)  
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())
