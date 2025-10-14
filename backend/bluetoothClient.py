import socket

client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

PI_MAC = "2C:CF:67:23:E7:0B",4

client.connect(PI_MAC)

try:
    while True:
        message = input("Enter message: ")
        client.send(message.encode("utf-8"))
        data = client.recv(1024)
        if not data:
            break
        if data.decode("utf-8") == "PING":
            print("Command Received")
        if data.decode("utf-8") == "N":
            print("Command Unknown")
except OSError as e:
    pass

client.close()
