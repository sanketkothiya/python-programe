import socket

s=socket.socket()
print(" socket is crearted")

s.bind(('localhost',8000))

s.listen(3)

print('waiting for connection ')

while True:
    c, add =s.accept()
    erno = c.recv(1024).decode()

    name = c.recv(1025).decode()

    branch = c.recv(1026).decode()

    city = c.recv(1027).decode()

    print(" server connect with : ",add)
    print("student details is:-------")
    print(f"student enrollment number is: {erno}   ,student name is: {name}   , student branch name is: { branch}   ,  student current city name is: { city} ")


    c.send(bytes(f'welcome to ADIT {name} \n','utf-8'))
    c.send(bytes('your data is now saved\n','utf-8'))
    c.send(bytes(f'now you login with  {erno}.{name}\n','utf-8'))

    c.close()


















