import sys
import random

from PySide6.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout)

from PySide6.QtCore import QUrl, Qt
from PySide6.QtMultimedia import QMediaPlayer,QAudioOutput

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Meu Espotifai")
        self.setGeometry(300,300,300,100)
        self.setWindowIcon('Mauricio/favicon-32x32.png')
        self.layout= QVBoxLayout()
        self.play_button = QPushButton("Play",self)
        self.layout.addWidget(self.play_button)
        self.setLayout(self.layout)
        #Audio
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)

        self.player.setSource(QUrl.fromLocalFile("Mauricio/musicateste.mp3"))
        self.play_button.clicked.connect(self.play_music)
        


    def play_music(self):
        print(f"Tocando \n a Musica legal")
        self.player.play()

app = QApplication(sys.argv)    
window = MusicPlayer()
window.show()
sys.exit(app.exec())    