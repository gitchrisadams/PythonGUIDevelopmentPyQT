from PyQt6.QtWidgets import QApplication, QDialog
import sys

# Initial config of app
app = QApplication(sys.argv)

# Create a Dialog window
# This has no max and close buttons
window = QDialog()

# Show the window
window.show()
sys.exit(app.exec())
