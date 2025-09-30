from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton

class ButtonPanel(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        connectBtn = QPushButton("Connect")
        launchBtn = QPushButton("Launch")
        stopBtn = QPushButton("Stop")

        layout.addWidget(self.connectBtn)
        layout.addWidget(self.launchBtn)
        layout.addWidget(self.stopBtn)

