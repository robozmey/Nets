import socket

serverAddressPort   = ("127.0.0.1", 20002)
bufferSize          = 1024

# Create a UDP socket at client side
TCPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Send to server using created UDP socket

TCPClientSocket.connect(serverAddressPort)
 
while True:

    command = input()
    bytesToSend = str.encode(command)

    TCPClientSocket.sendall(bytesToSend)

    msgFromServer = TCPClientSocket.recv(bufferSize)
    msg = msgFromServer.decode("utf-8") 

    print(msg)