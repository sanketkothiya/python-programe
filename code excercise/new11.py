n=int(input("enter the number"))
temp=n
r=0
while(n>0):
    d=n%10
    r=r*10+d
    n=n//10

if(r==temp):
          print("its palindrop")
else:
        print("its not palindrop")
