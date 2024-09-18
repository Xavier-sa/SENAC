import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        #caixa
        self.setWindowTitle("Espotifai")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon("Mauricio/icons8-kakarotto-16.png"))


        #play
        self.layout = QVBoxLayout()
        self.play_button = QPushButton("Play", self)
        self.play_button.setIcon(QIcon("Mauricio/iconePLAY.png"))
        self.layout.addWidget(self.play_button)
        self.setLayout(self.layout)

       #
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        
       
        self.player.setSource(QUrl.fromLocalFile("Mauricio/musicateste.mp3"))

        
        self.play_button.clicked.connect(self.toggle_music)

   
        self.is_playing = False

    def toggle_music(self):
        if self.is_playing:
            self.player.pause()
            self.play_button.setText("Play")
        else:
            self.player.play()
            self.play_button.setText("Pause")
           
            self.play_button.setIcon(QIcon("Mauricio/iconePAUSE.png")) 

       
        self.is_playing = not self.is_playing


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec())
