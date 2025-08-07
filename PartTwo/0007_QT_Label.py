from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QFont, QPixmap, QMovie
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        # Window config
        self.setGeometry(200, 200, 700, 400) # x pos, y pos, width, height
        self.setWindowTitle("Python GUI Developments")
        self.setWindowIcon(QIcon('../PartOne/images/python.png'))

        ''' ****************** Example of creating/configuring a Qlabel******************
        # Creating a QLabel and config
        label = QLabel("Python GUI Dev", self)
        # label.setText("New text replaces previous")
        label.move(100, 100)
        label.setFont(QFont("Sanserif", 15))
        label.setStyleSheet('color:red')
        # label.setText(str(12)) # Must convert int to str to show it
        label.setNum(15) # This requires not convert/other way to do it
        label.clear()
        '''

        # Adding an image to a label Example
        # label = QLabel(self)
        # pixmap = QPixmap('images/python.png')
        # label.setPixmap(pixmap)

        # Adding a animation w/ no sound
        label = QLabel(self)
        movie = QMovie('images/sky.gif')
        movie.setSpeed(500)
        label.setMovie(movie)
        movie.start()


# Initial config of app
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
