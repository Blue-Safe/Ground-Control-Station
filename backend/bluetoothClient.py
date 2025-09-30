from bluetooth import BluetoothSocket, RFCOMM, find_service

PI_MAC = "2C:CF:67:23:E7:0B"
UUID="00001101-0000-1000-8000-00805F9B34FB"

class BluetoothClient:
    def __init__(self):
        self.sock = None

    def connect(self):
        services = find_service(address=PI_MAC,uuid=UUID)
        if not services:
            raise Exception("No SPP service found on PI.")
        host = services[0]["host"]
        port = services[0]["port"]

        self.sock = BluetoothSocket(RFCOMM)
        self.sock.connect((host,port))
        print(f"Connected to {host} on port {port}")

    def send(self, msg: str):
        if self.sock:
            self.sock.send((msg+"\n").encode())
            print(f"Sent: {msg}")
    def close(self):
        if self.sock:
            self.sock.close()
            self.sock = None
