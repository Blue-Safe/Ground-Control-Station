import serial, sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout

# Test to make sure pyserial works
print("pyserial OK:", serial.__version__)


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

        buttons = QVBoxLayout()
        buttons.setSpacing(8)

        self.btnConnect = QPushButton("Connect")
        self.btnLaunch = QPushButton("Launch")
        self.btnStop = QPushButton("Stop")

        buttons.addWidget(self.btnConnect)
        buttons.addWidget(self.btnLaunch)
        buttons.addWidget(self.btnStop)

        layout.addLayout(buttons)

if __name__ == "__main__":
    win = Main()
    win.resize(300,150)
    win.show()
    sys.exit(app.exec_())