# import math
# import calendar
import function
# import  sys
# #
# # print(math.sqrt(25))
# # print(math.pow(2,5))
# # print(dir(math))
# #
# # cal=calendar.month(2018,1)
# # print(cal)
# sys.path.append("E:\LIC details ")
# print(sum([2,3,4,5,2,3,4,5,6,7]))

# import pack
# pack.a()

# from packages import first
# first.sk()

# Python program to demonstrate
# Creation of Array

# importing "array" for array creations
# import array as arr
# #
# # # creating an array with integer type
# # a = arr.array('i', [1, 2, 3])
# #
# # # printing original array
# # print("The new created array is : ", end=" ")
# # for i in range(0, 3):
# #     print(a[i], end=" ")
# # print()
# #
# # # creating an array with float type
# # b = arr.array('d', [2.5, 3.2, 3.3])
# #
# # # printing original array
# # print("The new created array is : ", end=" ")
# # for i in range(0, 3):
# #     print(b[i], end=" ")

# Python program to demonstrate
# Removal of elements in a Array

# importing "array" for array operations
import array

# initializing array with array values
# initializes array with signed integers
arr = array.array('i', [1, 2, 3, 1, 5])

# printing original array
print ("The new created array is : ", end ="")
for i in range (0, 5):
	print (arr[i], end =" ")

print ("\r")

# using pop() to remove element at 2nd position
print ("The popped element is : ", end ="")
print (arr.pop(2))

# printing array after popping
print ("The array after popping is : ", end ="")
for i in range (0, 4):
	print (arr[i], end =" ")

print("\r")

# using remove() to remove 1st occurrence of 1
arr.remove(1)

# printing array after removing
print ("The array after removing is : ", end ="")
for i in range (0, 3):
	print (arr[i], end =" ")
