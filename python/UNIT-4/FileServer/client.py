import socket

s = socket.socket()
host = socket.gethostname()
ipaddres = socket.gethostbyname(host)

port = 6000
print(ipaddres)
s.connect((ipaddres,port))
s.send(b"Hello Server!")
with open("received_file.txt","wb") as f:
    print("File opened")
    while True:
        print("receiving data...")
        data = s.recv(1024)
        print("data = %s",(data))
        if not data:
                break
        f.write(data)

f.close()
s.close()


