import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PySide6.QtGui import QIcon

class DragonBallGame(QWidget):
    def __init__(self):
        super().__init__()

        
        self.setWindowTitle("Dragon Ball Game")
        self.setGeometry(500, 500, 500, 450)
        self.setWindowIcon(QIcon("Mauricio/icons8-kakarotto-16.png"))

        self.layout = QVBoxLayout()

        self.attack_button = QPushButton("Atacar", self)
        self.attack_button.clicked.connect(self.show_attack_message)
        self.layout.addWidget(self.attack_button)

        self.eliminated_button = QPushButton("Você foi eliminado", self)
        self.eliminated_button.clicked.connect(self.show_eliminated_message)
        self.layout.addWidget(self.eliminated_button)

        self.setLayout(self.layout)

    def show_attack_message(self):
        QMessageBox.information(self, "Ataque", "Você atacou o inimigo!")

    def show_eliminated_message(self):
        QMessageBox.warning(self, "Eliminação", "Você foi eliminado!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DragonBallGame()
    window.show()
    sys.exit(app.exec())
