# import json
#
# data = '{"var1":"harry", "var2":56}'
# print(data)
#
# parsed = json.loads(data)
# print(type(parsed))
# print(parsed)
#
# #Task 1 - json.load?
#
#
# data2 = {
#     "channel_name": "CodeWithHarry",
#     "cars": ['bmw', 'audi a8', 'ferrari'],
#     "fridge": ('roti', 540),
#     "isbad": False
# }
#
# sk = json.dumps(data2)
# print(sk)
#
# # Task 2 = what is sort_keys parameter in dumps


#
# def solveMeFirst( a, b):
# 	return a+b
#
#
# num1 = int(input("enter the number 1"))
# num2 = int(input(" enter the number 2"))
# res = solveMeFirst(num1,num2)
# print(res)

# def solveMeFirst(int a,int b):
# 	# Hint: Type return a+b below
#     return a+b
#
#
# num1 = int(input())
# num2 = int(input())
# res = solveMeFirst(num1,num2)
# print(res)
#
# num1=int(input("enter the array size"))
#
# array=[]
#
# # for i in range(1,num1 + 1):
# #     n1=int(input("enter the number"))
# #     array.append(n1)
# i=0
# while i<num1:
#  n1=int(input("enter the number by space"))
#  i+=1
#  array.append(n1)
#
# print(sum(array))

#
# def aray1(*args):
#     total=0
#
#
# sk1=int(input("enter the array size"))
# sk1=int(input("enter the arr"))
# def simpleArraySum(*ar):
#     thesum = 0
#     for i in ar:
#         thesum += i
#     return thesum