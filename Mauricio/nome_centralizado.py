
import sys
import random

from PySide6.QtWidgets import (QApplication, QLabel,
     QPushButton, QVBoxLayout, QWidget)
from PySide6.QtCore import Qt, Slot

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Bem Vindo Xavier!", "Vamos começar?", "If-\n Oque deseja fazer?", "Else-Ok,Vamos encerrar e ir pro intervalo!"]

        self.button = QPushButton("Clique aqui!")
        self.text = QLabel("Wellington Aparecido Santos Xavier...")
        self.text.setAlignment(Qt.AlignCenter)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @Slot()
    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())