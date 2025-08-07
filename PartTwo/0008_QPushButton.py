from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMenu
from PyQt6.QtGui import QIcon, QFont
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window config
        self.setGeometry(200, 200, 700, 400) # x pos, y pos, width, height
        self.setWindowTitle("Python GUI Developments QPushButton")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_button()

    def create_button(self):
        btn = QPushButton("Click", self)
        btn.setGeometry(100,100, 130,130)
        btn.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        btn.setIcon(QIcon("images/python.png"))
        btn.setIconSize(QSize(36,36))

        #popup menu
        menu = QMenu()
        menu.setFont(QFont("Times", 14, QFont.Weight.ExtraBold))
        menu.setStyleSheet('background-color:green')
        menu.addAction("Copy")
        menu.addAction("Cut")
        menu.addAction("Paste")
        btn.setMenu(menu)

# Initial config of app
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
