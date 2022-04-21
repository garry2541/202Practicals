# Practical 08
# Server

# This program won't run in Online Compiler
import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port =  65432
serversocket.bind((host, port))
serversocket.listen(5)
print('Server started...')
while True:
     conn,addr = serversocket.accept()
     print("Got a connection from ",str(addr))
     data=conn.recv(1024).decode()
     print(f"Received {data}")
     conn.send(b"Hello! I am server\n")
     conn.close()
     print("Client disconnected")