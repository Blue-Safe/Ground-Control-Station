import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from widgets import buttons




# ---------------  Gui  -------------------#

app = QApplication(sys.argv)

# The Main window object.

class Main(QMainWindow):

    # Main window constructor. Uses parents
    # __init__ method, sets the title, and
    # establishes formatting and static widgets
    # for the application.

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ground Control Station")
        layout = QVBoxLayout()
        layout.setContentsMargins(16,16,16,16)
        layout.setSpacing(12)

        self.title = QLabel("Ground Control Station")
        self.title.setAlignment(Qt.AlignCenter)
        f = QFont()
        f.setPointSize(20)
        self.title.setFont(f)

        central = QWidget(self)
        central.setLayout(layout)
        self.setCentralWidget(central)

        layout.addWidget(self.title)

        layout.addStretch(1)

        self.buttons = buttons.ButtonPanel()

        layout.addWidget(self.buttons)

if __name__ == "__main__":
    win = Main()
    win.resize(300,150)
    win.show()
    sys.exit(app.exec_())