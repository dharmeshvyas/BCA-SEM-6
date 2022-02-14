import socket

# define the server name and port
host = '192.168.10.18'
port = 5000

# create socket at sever side
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# bind the socket with sever and port number
s.bind((host, port))

# number of connection in int can connect
s.listen(1)

# wait for connecting connection
c, addpres = s.accept()
# display client info address
print("Connection from:", str(addpres))

# send message after client connected

c.send(b"Hello there how are you?Welcome to Dv's Sever")
message = "Bye have good day...."
c.send(message.encode())
# close connection
c.close()
