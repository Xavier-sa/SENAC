import sys
from PySide6.QtWidgets import QApplication, QPushButton
from PySide6.QtCore import Slot

@Slot()
def say_hello():
 print("Button clicked, Hello!")

app = QApplication(sys.argv)

button = QPushButton("Clica aqui!")

button.clicked.connect(say_hello)
button.show()
app.exec()