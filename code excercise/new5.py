from array import  *

# val = array ('i',[34,565,654,356])

# for i in range(4):
#     print(val[i])

# for e in val:
#     print(e)

num=array('i',[])
a=int(input("enter the array length"))

for i in range(a):
    x=int(input("enter the array value"))
    num.append(x)
print(num)

z=int(input("enter the number you want to check"))
t=0
for e in num:
    if e==z:
        print(t)
        break
    t+=1

print("program close")
