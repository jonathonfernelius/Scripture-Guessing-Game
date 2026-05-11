from PyQt6.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel, QComboBox
from PyQt6.QtCore import Qt, QTimer
from scriptle_plus_functions import *

class MainMenuPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.title_label = QLabel("Fern's Scripture Guessing Game")
        self.play_button = QPushButton("Play Game")
        self.high_scores_button = QPushButton('View High Scores')
        layout.addWidget(self.title_label)
        layout.addWidget(self.play_button)
        layout.addWidget(self.high_scores_button)
        self.setLayout(layout)

class GamePage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.title_label = QLabel('Guess the Scripture')
        self.title_label.setStyleSheet("font-size: 30px;")
        
        # Initialize where the random scripture text and answer go
        self.scripture_label = QLabel('scripture goes here')
        self.scripture_label.setStyleSheet("font-size: 20px;")
        self.scripture_label.setWordWrap(True)
        self.scripture_label.setMinimumWidth(700)
        self.answer_label = QLabel('answer goes here')
        self.answer_label.setStyleSheet("font-size: 25px;")

        # Set up teleport buttons and answer inputs
        self.menu_return_button = QPushButton('Return to Menu')
        self.submit_button = QPushButton('Submit')
        self.answer_box = QComboBox()
        self.answer_box.addItems(['1 Nephi', '2 Nephi', 'Jacob', 'Enos', 'Jarom', 'Omni', 'Words of Mormon', 'Mosiah', 'Alma', 'Helaman', '3 Nephi', '4 Nephi', 'Mormon', 'Ether', 'Moroni'])
        self.score_label = QLabel('')
        
        # Make it all appear
        layout.setSpacing(5)
        layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        # layout.addWidget(self.scripture_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
        scripture_area = QVBoxLayout()
        scripture_area.addWidget(self.scripture_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addLayout(scripture_area)
        layout.addWidget(self.answer_label, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.score_label, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        layout.addWidget(self.answer_box)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.menu_return_button)
        self.setLayout(layout)

        self.submit_button.clicked.connect(self.submit_answer)

    def showEvent(self, event):
        super().showEvent(event)
        self.total_answered = 0
        self.total_correct = 0
        self.random_scripture = get_scripture()
        self.scripture_label.setText(self.random_scripture['scripture_text'])
        self.answer_label.setText('')

    def submit_answer(self):
        self.total_answered += 1
        if self.answer_box.currentText() == self.random_scripture['book_title']:
            self.total_correct += 1
        self.score_label.setText(f'{self.total_correct} / {self.total_answered}')
        self.answer_label.setText(self.random_scripture['verse_title'])
        QTimer.singleShot(2000, self.load_next_scripture)

    def load_next_scripture(self):
        self.random_scripture = get_scripture()
        self.scripture_label.setText(self.random_scripture['scripture_text'])
        # self.scripture_label.setLineWidth(500)
        self.answer_label.setText('')

        

class HighScoresPage(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.high_scores_label = QLabel('Nothing here yet, sorry')
        self.menu_return_button = QPushButton('Return to Menu')
        layout.addWidget(self.high_scores_label)
        layout.addWidget(self.menu_return_button)
        self.setLayout(layout)
