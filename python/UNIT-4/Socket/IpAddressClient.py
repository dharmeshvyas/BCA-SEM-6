import socket
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
print(f"Hostname{hostname}")
print(f"Ip address{ip_address}")