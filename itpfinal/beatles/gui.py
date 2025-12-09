import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
)
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import QProcess 
from PyQt6.QtCore import QProcess, Qt

def on_button_click():
    import markovify

    def load_lyrics(corpus_path):
        with open(corpus_path, 'r', encoding='utf-8') as f:
            return f.read().split('\n')
    
    def generate_lyrics(corpus_path, genre, num_lines):
        lyrics = load_lyrics(corpus_path)

        corpus_text = "\n".join(lyrics)

        if not corpus_text or len(corpus_text.split()) < 2:
            print("ERROR: corpus_text is empty or too short. Check your input file.")
            return None

        text_model = markovify.Text(corpus_text, state_size=2)

        generated_lines = []
        for _ in range(num_lines):
            line = text_model.make_sentence(tries=100)
            if line:
                generated_lines.append(line)

        title = f"Generated {genre} Lyrics"
        lyrics_str = "\n".join(generated_lines)
        return f"{title}\n\n{lyrics_str}"

    corpus_path = 'all_lyrics_onlytwo.txt'
    genre = 'pop' 
    num_lines = 20  

    result = generate_lyrics(corpus_path, genre, num_lines)
    print(result)

    from gtts import gTTS
    import os

    text_to_speak = (result)
    tts = gTTS(text=text_to_speak, lang='en')
    tts.save("lyricsbyeann.mp3")

    print("lyrics generated!")

import os
def play_audio():
    audio_file = "lyricsbyeann.mp3"
    
    if not os.path.exists(audio_file):
        print(f"Error: Audio file '{audio_file}' not found. Generate lyrics first.")
        return
    
    player_process = QProcess()

    if sys.platform.startswith('darwin'):
        success = player_process.startDetached("open", [audio_file])
    

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lyric Generator")
        self.setGeometry(100, 100, 300, 150)

        top_widget = QWidget()
        self.setMenuWidget(top_widget)
        layout = QVBoxLayout()

        self.resize(400, 100)

        self.button = QPushButton("generate lyrics")
        
        self.button.clicked.connect(on_button_click)

        layout.addWidget(self.button)
        top_widget.setLayout(layout)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        layout = QVBoxLayout(central_widget) 
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addStretch(1)

        self.play_button = QPushButton("listen!!")
        self.play_button.clicked.connect(play_audio)
        self.play_button.setEnabled(True) 

        layout.addStretch(1)

        layout.addWidget(self.play_button, alignment=Qt.AlignmentFlag.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    



