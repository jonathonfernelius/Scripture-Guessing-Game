from PyQt6.QtWidgets import QApplication, QMainWindow, QStackedWidget
import sys
from scriptle_plus_pages import *
from scriptle_plus_functions import *

class MainWindow(QMainWindow): # Manage the entire window
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fern's Scripture Guessing Game")
        self.resize(800, 600)
        self.setMinimumSize(800, 600)
        
        # All ze pages
        self.stack = QStackedWidget()
        self.menu_page = MainMenuPage()
        self.game_page = GamePage()
        self.high_scores_page = HighScoresPage()
        self.stack.addWidget(self.menu_page)
        self.stack.addWidget(self.game_page)
        self.stack.addWidget(self.high_scores_page)
        self.setCentralWidget(self.stack)

        # Teleportation
        self.game_page.menu_return_button.clicked.connect(self.show_menu_page)

        self.menu_page.play_button.clicked.connect(self.show_game_page)
        self.menu_page.high_scores_button.clicked.connect(self.show_high_scores_page)

        self.high_scores_page.menu_return_button.clicked.connect(self.show_menu_page)

    # Change the page
    def show_menu_page(self):
        self.stack.setCurrentIndex(0)
    def show_game_page(self):
        self.stack.setCurrentIndex(1)
    def show_high_scores_page(self):
        self.stack.setCurrentIndex(2)



app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())