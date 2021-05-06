arr=[]
num=int(input("enter the n number "))
for i in range(num):
    numbers=int(input("enter number"))
    arr.append(numbers)
print("maximum number is",max(arr))
print("minimum number is ",min(arr))