import socket
from backend import dummySocket


def connect(pi_mac, channel=4):
    try:
        client = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
        client.connect((pi_mac, channel))
        print("Connected to Pi at", pi_mac)
        return client

    except OSError as e:
        print("Could not connect:", e)
        print("Using DummySocket instead.")
        return dummySocket.DummySocket()


def sendCmd(client,cmd):

    client.send(cmd.encode("utf-8"))
    data = client.recv(1024)

    if data.decode("utf-8") == "PING":
        print("Command Received")
    if data.decode("utf-8") == "N":
        print("Command Unknown")
