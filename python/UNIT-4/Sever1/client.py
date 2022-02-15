import socket

# define sever name and port

host = '192.168.10.18'
port = 5000

# create socket at client side
# Using TCP/IP protocol

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connect to the sever and port

s.connect((host, port))

# receive message from sever at a time 1024 bytes
message = s.recv(1024)

# repeat as long as message
# String not empty

while message:
    print('Client :' + message.decode())
    message = s.recv(1024)
s.close()