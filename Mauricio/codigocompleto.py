import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtCore import QUrl
from PySide6.QtGui import QIcon

class MusicPlayer(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela
        self.setWindowTitle("Espotifai")
        self.setGeometry(300, 300, 300, 100)
        self.setWindowIcon(QIcon("Mauricio/icons8-kakarotto-16.png"))

        # Layout e botão de controle
        self.layout = QVBoxLayout()
        self.play_button = QPushButton(self)
        self.layout.addWidget(self.play_button)
        self.setLayout(self.layout)

        # Configuração do player de áudio
        self.player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.player.setAudioOutput(self.audio_output)
        self.player.setSource(QUrl.fromLocalFile("Mauricio/musicateste.mp3"))

        # Inicialização do estado
        self.is_playing = False
        self.update_button()

        # Conectar o botão ao método de alternância
        self.play_button.clicked.connect(self.toggle_music)

    def toggle_music(self):
        if self.is_playing:
            self.player.pause()
        else:
            self.player.play()
        self.is_playing = not self.is_playing
        self.update_button()

    def update_button(self):
        if self.is_playing:
            self.play_button.setText("Pause")
            self.play_button.setIcon(QIcon("Mauricio/iconePAUSE.png"))
        else:
            self.play_button.setText("Play")
            self.play_button.setIcon(QIcon("Mauricio/iconePLAY.png"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec())
