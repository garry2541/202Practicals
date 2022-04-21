# Practical 08
# Client

# This program won't run in Online Compiler
import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "127.0.0.1"
port = 65432
s.connect((host, port))

s.send(b"I am Client\n")
tm = s.recv(1024).decode()
s.close()
print("Message from server is: ",tm)