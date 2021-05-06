#
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
# emp2 =Employee("Rohan", 55, "Cleaner")
# print(str(emp1))
# print(emp1 + emp2)


# from abc import ABCMeta, abstractmethod
# from abc import ABC, abstractmethod
#
# class Shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
#
# class Rectangle(Shape):
#     type = "Rectangle"
#     sides = 4
#     def __init__(self):
#         self.length = 6
#         self.breadth = 7
#
#     def printarea(self):
#         return self.length * self.breadth
#
# rect1 = Rectangle()
# print(rect1.printarea())

import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
# print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)
