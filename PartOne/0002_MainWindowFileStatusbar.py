from PyQt6.QtWidgets import QApplication, QMainWindow
import sys

# Initial config of app
app = QApplication(sys.argv)

# Create a smaller size window
window = QMainWindow()

# Statusbar
window.statusBar().showMessage("Welcome to PyQT6 Course")

# File menu
window.menuBar().addMenu(("File"))


# Show the window
window.show()
sys.exit(app.exec())
