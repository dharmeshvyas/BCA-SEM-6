import socket


msgFromClient = "Hello UDP server"
bytesToSend = str.encode(msgFromClient)

serverAddressPort = ("127.0.0.1",2002)

buffersize = 2048
UDPClientServer = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPClientServer.sendto(bytesToSend,serverAddressPort)
msgFromServer = UDPClientServer.recvfrom(buffersize)
msg = "Message From server {}".format(msgFromServer[0])
print(msg)