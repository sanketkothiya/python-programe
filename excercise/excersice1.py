# def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if name==target:
#          return pos
#     return -1
#
# name=["preet","sanket"]
# print(find_pos(name,"sanket"))

# class A:
#     def met(self):
#         print("This is a method from class A")
#
# class B(A):
#     def met(self):
#         print("This is a method from class B")
#
# class C(A):
#     def met(self):
#         print("This is a method from class C")
#
# class D(C, B):
#     def met(self):
#         print("This is a method from class D")
#
#
# a = A()
# b = B()
# c = C()
# d = D()
#
# b.met()


# class Employee:
#     no_of_leaves = 8
#
#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#
#     def printdetails(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls, newleaves):
#         cls.no_of_leaves = newleaves
#
#     def __add__(self, other):
#         return self.salary + other.salary
#
#     def __truediv__(self, other):
#         return self.salary / other.salary
#
#     def __repr__(self):
#         return f"Employee('{self.name}', {self.salary}, '{self.role}')"
#
#     def __str__(self):
#         return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
#
# emp1 =Employee("Harry", 345, "Programmer")
# # emp2 =Employee("Rohan", 55, "Cleaner")
# print(str(emp1))

# l=[]
# for i in range(2000, 3201):
#     if (i%7==0) and (i%5!=0):
#         l.append(str(i))
#
# print (','.join(l))

# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
#
# x=int(input("enter the number "))
# print (fact(x))


# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print(d)

# values=input()
# l=values.split(",")
# t=tuple(l)
# print(l)
# print(t)

# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#
#     def getString(self):
#         self.s = str(input("enter the string"))
#
#     def printString(self):
#         print(tuple(self.s.upper()))
#
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()
#
# import math
# c=50
# h=30
# value = []
# items=[x for x in input("enter the number").split(',')]
# for d in items:
#     value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))
#
# print(','.join(value))

# input_str = input("enter the number")
# dimensions=[int(x) for x in input_str.split(',')]
# rowNum=int(input("enter the rownumber"))
# # colNum=int(input("enter the colnumber"))
# # # multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
# # multilist=[[][]]
# #
# # for row in range(rowNum):
# #     for col in range(colNum):
# #         multilist[row][col]= row*col
# #
# # print(multilist)

# items = [x for x in input("enter the number by comma saprated value").split(',')]
# items.sort(reverse=True)
#
# print(','.join(items))

# lines = []
# while True:
#     s = input(" enter the sentence")
#     if s:
#         lines.append(s.upper())
#     else:
#         break;
#
# for sentence in lines:
#     print(sentence)


s = input("enter the sentence ")
words = [word for word in s.split(" ")]
print(" ,".join(sorted(list(set(words)))))