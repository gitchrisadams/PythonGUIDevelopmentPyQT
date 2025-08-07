from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window config
        self.setGeometry(200, 200, 700, 400) # x pos, y pos, width, height
        self.setWindowTitle("Python GUI Developments QHboxLayout")
        self.setWindowIcon(QIcon('images/python.png'))

        # QHBoxLayout - Horizontal
        hbox = QHBoxLayout()

        # Create some buttons
        btn1 = QPushButton("Clicke one")
        btn2 = QPushButton("Clicke two")
        btn3 = QPushButton("Clicke three")
        btn4 = QPushButton("Clicke four")

        # Add buttons to our QHBoxLayout
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)
        hbox.addWidget(btn3)
        hbox.addWidget(btn4)
        # hbox.addSpacing(100)
        hbox.addStretch(5)

        self.setLayout(hbox)



# Initial config of app
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
