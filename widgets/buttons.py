from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton
from backend import bluetoothServer


class ButtonPanel(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.bt = bluetoothClient.BluetoothClient()


        self.layout = QVBoxLayout(self)
        self.connectBtn = QPushButton("Connect")
        self.launchBtn = QPushButton("Launch")
        self.stopBtn = QPushButton("Stop")


        self.connectBtn.clicked.connect(self.bt.connect)
        self.launchBtn.clicked.connect(lambda: self.bt.send("Launch"))
        self.stopBtn.clicked.connect(lambda: self.bt.send("Stop"))


        self.layout.addWidget(self.connectBtn)
        self.layout.addWidget(self.launchBtn)
        self.layout.addWidget(self.stopBtn)

