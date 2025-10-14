import socket

class DummySocket:
    def __init__(self):
        self.lastCmd = None
    def send(self, data):
        decoded = data.decode("utf-8")
        self.last_cmd = decoded
        print("[DummySocket] Would send:", decoded)
    def recv(self, bufsize):
        if self.lastCmd == "launch" or "stop":
            return b"PING"
        return b"N"
    def close(self):
        print("[DummySocket] Closed")

