import serial, sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel

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
        central = QWidget(self)
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        lable = QLabel("Hello world")
        layout.addWidget(lable)




if __name__ == "__main__":
    win = Main()
    win.resize(900,600)
    win.show()
    sys.exit(app.exec_())