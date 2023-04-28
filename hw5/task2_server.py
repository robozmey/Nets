import socket
import time
import os
import subprocess

localIP     = "127.0.0.1"
localPort   = 20002
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"

# Create a datagram socket
TCPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Bind to address and ip
TCPServerSocket.bind((localIP, localPort))

TCPServerSocket.listen()

print("TCP server up and listening")

# Listen for incoming datagrams

conn, addr = TCPServerSocket.accept()

while(True):

    msg = conn.recv(bufferSize)
    
    print(msg)

    # Sending a reply to client

    ans = subprocess.run(msg.split(), stdout=subprocess.PIPE).stdout.decode("utf-8") 

    # print(type(ans), ans)
    # if type(ans) != str:
    #     ans = str(ans)

    bytesToSend = str.encode(ans)

    conn.sendall(bytesToSend)

    # time.sleep(1)