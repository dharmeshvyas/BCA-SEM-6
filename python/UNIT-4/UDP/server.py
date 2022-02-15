import socket
import struct

localid = '127.0.0.1'
localport = 2002
buffersize = 1024
#creating udp socket

msgFromserver = "Thank you for connection our server"
byteToSend = str.encode(msgFromserver)

UDpsocketsever = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)

UDpsocketsever.bind((localid,localport))

print('UDP server and listing ')

while True:

    bytesAddresspair = UDpsocketsever.recvfrom(buffersize)

    message = bytesAddresspair[0]
    address =   bytesAddresspair[1]

    clientMsg = "Server:{}".format(message)
    print(clientMsg)

    UDpsocketsever.sendto(byteToSend,address)
