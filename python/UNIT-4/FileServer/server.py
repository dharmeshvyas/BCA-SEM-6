import socket
port =  6000

s = socket.socket()

host = socket.gethostname()

s.bind((host,port))
s.listen(5)
print("server listening...")
while True:
    con,addres = s.accept()
    print("got connection from ",addres)
    data = con.recv(1024)
    print("server recieved",repr(data))

    filename = 'mytext.txt'
    f = open(filename,"rb")
    l = f.read()
    while(l):
        con.send(l)
        print('sent',repr(l))
        l = f.read(1024)
    f.close()
    print("done sending")
    msg = 'Thank your for connecting. :)\r\r'
    con.send(msg.encode())
    con.close()


