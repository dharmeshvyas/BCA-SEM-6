import socket
#to create a socket we have to use the socket.socket() method. 

#syntex :socket.socket(socket_family, socket_type, protocol=0)
#socket_family: Either AF_UNIX or AF_INET
#socket_type: Either SOCK_STREAM or SOCK_DGRAM.
#protocol: Usually left out, defaulting to 0.

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print(s)
