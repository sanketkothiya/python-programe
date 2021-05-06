apple=int(input("enter the number of apple"))
mn=int(input("enter the number of the minumum"))
my=int(input("enter the number of the maximum"))

for i in range(mn,my+1):
    if apple%i==0:
        print(f"{i} is divisile by the {apple}")
    else:
        print(f"{i} is not divisile by {apple}")