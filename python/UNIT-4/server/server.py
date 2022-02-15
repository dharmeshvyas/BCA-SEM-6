import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port= 9099
serversocket.bind((host,port))
serversocket.listen(5)
while True:
    clientsocket,addr = serversocket.accept()
    print("Got connection from %s"%str(addr))

    msg = 'Thank your for connecting. :)\r\r'
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()
