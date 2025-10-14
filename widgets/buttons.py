from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from backend import bluetoothClient as bc
PI_MAC = "2C:CF:67:23:E7:0B"


class ButtonPanel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.client = None

        # layout and buttons
        self.layout = QVBoxLayout(self)
        self.connectBtn = QPushButton("Connect")
        self.launchBtn = QPushButton("Launch")
        self.stopBtn = QPushButton("Stop")

        # connect button signals to methods
        self.connectBtn.clicked.connect(self.on_connect_clicked)
        self.launchBtn.clicked.connect(self.on_launch_clicked)
        self.stopBtn.clicked.connect(self.on_stop_clicked)

        # add to layout
        self.layout.addWidget(self.connectBtn)
        self.layout.addWidget(self.launchBtn)
        self.layout.addWidget(self.stopBtn)


    # === Button actions === #

    def on_connect_clicked(self):
        print("Connecting to Pi...")
        self.client = bc.connect(PI_MAC)
        if self.client:
            print("Connected")
        else:
            print("Connection failed or dummy client used.")

    def on_launch_clicked(self):
        if self.client:
            bc.sendCmd(self.client, "launch")
        else:
            print("No connection")

    def on_stop_clicked(self):
        if self.client:
            bc.sendCmd(self.client, "stop")
        else:
            print("No connection")
