from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window config
        self.setGeometry(200, 200, 700, 400) # x pos, y pos, width, height
        self.setWindowTitle("Python GUI Developments")
        self.setWindowIcon(QIcon('images/python.png'))

# Initial config of app
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
