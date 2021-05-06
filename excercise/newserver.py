import socket

s = socket.socket()
print("socket established!")

s.bind(('localhost', 8000))

s.listen(5)

print("waiting for connection...")
print("-------------------------")

while True:
    c, add = s.accept()
    print(f"Connection to {add} established successfully")

    er_no = c.recv(1024).decode()
    name = c.recv(1025).decode()
    branch = c.recv(1026).decode()
    city = c.recv(1027).decode()
    print("Student details are:-")
    print(f"Student Enrolment number is: {er_no}\nStudent name is: {name.title()}\nStudent's branch is: {branch.upper()}\nStudent's city is: {city.title()}")
    c.send(bytes(f"Welcome to ADIT {name.title()}", "utf-8"))
    c.close()