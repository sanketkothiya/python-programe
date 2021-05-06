import socket

c= socket.socket()


c.connect(("localhost",8000))

erno=input("enter the your enrollment number:--\n")
name=input("enter the your name:--\n")
branch=input("enter your field name:--\n")
city=input("enter your city name:--\n")


c.send(bytes(erno,'utf-8'))
c.send(bytes(name,'utf-8'))
c.send(bytes(branch,'utf-8'))
c.send(bytes(city,'utf-8'))

print(c.recv(1024).decode())
print(c.recv(1024).decode())
print(c.recv(1024).decode())
