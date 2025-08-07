from PyQt6.QtWidgets import QApplication, QWidget
import sys

# Initial config of app
app = QApplication(sys.argv)

# Create a basic normal size window
# You can't add things like statusbar, file menu etc...
window = QWidget()


# Show the window
window.show()
sys.exit(app.exec())


