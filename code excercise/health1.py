from datetime import datetime



client1 = "harry"

client2 = "rohan"

client3 = "hamed"

def getdate():

    import datetime

    return datetime.datetime.now()

def excercises1():

    f = open("exercise1.txt", "w")

    dates = getdate()

    print(dates)

    f.write("seated row")

    f = open("exercise1.txt")

    first = f.read()

    print(first)

    f.close()



def excercises2():

    f = open("exercise1.txt", "w")

    dates = getdate()

    print(dates)

    f.write("seated row")

    f = open("exercise1.txt")

    first = f.read()

    print(first)





def excercises3():

    f = open("exercise1.txt", "w")

    dates = getdate()

    print(dates)

    f.write("seated row")

    f = open("exercise1.txt")

    first = f.read()

    print(first)





def food1():

    f = open("diet1.txt", "w")

    dates = getdate()

    print(dates)

    f.write("chicken")

    f = open("diet1.txt")

    second = f.read()

    print(second)





def food2():

    f = open("diet1.txt", "w")

    dates=getdate()

    print(dates)

    f.write("chicken")

    f = open("diet1.txt")

    second = f.read()

    print(second)





def food3():

    f = open("diet1.txt", "w")

    dates = getdate()

    print(dates)

    f.write("chicken")

    f = open("diet1.txt")

    second = f.read()

    print(second)







print("enter the client number")

number = int(input())

if 1 == number:

    a = "exercise"

    print(a)

    b = "diet"

    print(b)

    name = input("enter the word exercise or diet:")

    if name == a:

        excercises1()

    else:

        food1()

elif 2 == number:

    a = "exercise locked"

    b = "diet locked"

    name = input("enter the word a or b:")

    if name == a:

        excercises2()

    else:

        food2()

elif 3 == number:

    a = "exercise locked"

    b = "diet locked"

    name = input("enter the word a or b:")

    if name == a:

        excercises3()

    else:

        food3()