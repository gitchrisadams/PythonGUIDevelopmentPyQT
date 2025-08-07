from PyQt6.QtWidgets import QApplication, QWidget
import sys
from PyQt6 import uic

# This loads a .ui file that was created in
# pyQT designer and runs the UI file in python
class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("WindowUI.ui", self)



app = QApplication(sys.argv)
window = UI()
window.show()
app.exec()
