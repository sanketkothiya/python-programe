import socket

s = socket.socket()

s.connect(('localhost',8000))

er_no = input("Enter your Enrolment number: ")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
name = first_name + " " + last_name
branch = input("Enter your Branch: ")
city = input("Enter your City: ")

print("-------------------------")

s.send(bytes(er_no, "utf-8"))
s.send(bytes(name, "utf-8"))
s.send(bytes(branch, "utf-8"))
s.send(bytes(city, "utf-8"))

welcome = s.recv(1024).decode("utf-8")
print(welcome)