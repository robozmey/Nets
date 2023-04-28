import socket
import time

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"

# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM, proto=socket.IPPROTO_UDP)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))

# # Set timeout
UDPServerSocket.settimeout(1)

# UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
UDPServerSocket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print("UDP server up and listening")

# Listen for incoming datagrams

addresses = []

times = 0

while(True):
    try:
        _, address = UDPServerSocket.recvfrom(bufferSize)
        addresses.append(address)
    except TimeoutError:
        times += 1
    

    # Sending a reply to client

    str_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    bytesToSend = str.encode(str_time)

    for addres in addresses:
        UDPServerSocket.sendto(bytesToSend, addres)

    # time.sleep(1)