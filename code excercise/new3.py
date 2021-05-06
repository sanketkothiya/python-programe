num = [23,45,66,78,34,35]
for i in num:
    if i%9==0:
        print(i)

else:
    print("number is not found")


print("second progra")

name,age=input("enter your name and age").split(" ")
print(name)
print(age)

print(third program)

name="sanket"
age=23
print("hello {} your age is {}".format(name,age))
print(f"hello {name} your name is {age-3}")

print("third program")

num1,num2,num3=input("entre three number separate by comma").split(",")
print(f"your avg value is:{(int(num1)+int(num2)+int(num3))/3}")

print("fourth..")

name=input("enter youut name")
print(f"your reverse name is:---{name[-1 : : -1] }")

print("five program")

name,char=input("enter your name and chrater").split(",")
print(f"length is :--{ len(name)}")
print(f"your char val is:-{name.count(char) }")

print("six ..")

total=0
i=1
while i<=10:
    total=total + i
    i+=1
print(total)

print("seven")

n=input("enter a number")
total = 0
i = 0
while i < len(n):
    total = total + int(n[i])
    i+=1

print(total)

print("eight")

name =input("enter your name")

temp_var=""
i=0
while i < len(name):
    if name[i] not in temp_var:
      temp_var+=str(name[i])
      print(f"{name[i]} : {name.count(name[i])}")
    i += 1