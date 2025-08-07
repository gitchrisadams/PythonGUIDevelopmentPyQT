from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window config
        self.setGeometry(200, 200, 700, 400) # x pos, y pos, width, height
        self.setWindowTitle("Python GUI Developments Event Handling")
        self.setWindowIcon(QIcon('images/python.png'))

        self.create_widget()

    def create_widget(self):
        # Add layout and button
        hbox = QHBoxLayout()
        btn = QPushButton("Change Text")

        # Connect the button handler function with the button
        btn.clicked.connect(self.clicked_btn)

        # Create a label we can use to show changing of text
        self.label = QLabel("Default Text")
        hbox.addWidget(btn)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    # Event handler for button click
    def clicked_btn(self):
        self.label.setText("Another Text")
        self.label.setFont(QFont("Times", 15))
        self.setStyleSheet('color:red')

# Initial config of app
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
