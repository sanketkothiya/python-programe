# met =True
# while met:
#
#     s1=str.lower(input())
#
#     if s1=='yes':
#         s1=True
#         break
#
#     if s1 == 'no':
#         s1 = False
#         break


user=input("enter maritial status")
user:user.upper()
valid=True
while not valid:
    if user=='M' or user=='S':
        valid=True
    else:
        print("invalid input")
        user=input("enter proper maritial status")
        user=user.upper()





