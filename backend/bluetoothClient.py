# from bluetooth import BluetoothSocket, RFCOMM, find_service
#
# PI_MAC = "2C:CF:67:23:E7:0B"
# UUID="00001101-0000-1000-8000-00805F9B34FB"
#
# class BluetoothClient:
#     def __init__(self):
#         self.sock = None
#
#     def connect(self):
#         services = find_service(address=PI_MAC,uuid=UUID)
#         if not services:
#             raise Exception("No SPP service found on PI.")
#         host = services[0]["host"]
#         port = services[0]["port"]
#
#         self.sock = BluetoothSocket(RFCOMM)
#         self.sock.connect((host,port))
#         print(f"Connected to {host} on port {port}")
#
#     def send(self, msg: str):
#         if self.sock:
#             self.sock.send((msg+"\n").encode())
#             print(f"Sent: {msg}")
#     def close(self):
#         if self.sock:
#             self.sock.close()
#             self.sock = None

import socket

server = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

PI_MAC = "2C:CF:67:23:E7:0B"

server.bind(PI_MAC)

server.listen(1)

client, addr = server.accept()

try:
    while True:
        data = client.recv(1024)
        if not data:
            break
        print(f"Message: {data.decode('utf-8')}")
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
except OSError as e:
    pass



