# Array lambda  module package  functions 

# 1 Array

# import array as arr
# nums= arr.array('i', [1, 2, 3, 4])
# nums.append(5)
# print("First Element:", nums[0])
# print("Third Element:", nums[2])
# print(nums)
# nums.reverse()
# print("Reversed Array:", nums)
# nums.extend([2, 3, 4,5])
# print("After Extend:", nums)


 
# 3 Module
# 1 Built-in module
import math
import random
import datetime
# math module
print("Square Root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
# random module
print("Random Number:", random.randint(1, 100))
# datetime module
print("Current Date and Time:", datetime.datetime.now())


# 2  User Defined module
# from Calculator import *

# a = int(input("Enter no1: "))
# b = int(input("Enter no2: "))

# while True:

#     print("\nMenu")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Divide")
#     print("5. Exit")

#     ch = int(input("Enter your choice: "))

#     match ch:
#         case 1:
#             print("Addition is", add(a, b))
#         case 2:
#             print("Subtraction is", subtract(a, b))
#         case 3:
#             print("Multiplication is", multiply(a, b))
#         case 4:
#             if b != 0:
#                 print("Division is", divide(a, b))
#             else:
#                 print("Cannot divide by zero")
#         case 5:
#             print("Program Ended")
#             break
#         case _:
#             print("Invalid Choice")
            
# 3 Third-party module
import numpy as np # type: ignore
nums = np.array([10, 20, 30, 40, 50])

print("Array:", nums)
print("Sum:", np.sum(nums))
print("Average:", np.mean(nums))
print("Maximum:", np.max(nums))
print("Minimum:", np.min(nums))   
            
                  

# # Functions in Py

# # 1 Function without argument & without return value
# def welcome():
#     print("Welcome to Python")

# # 2 Function with arguments & without return value
# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)

# # 3 Function with arguments & with return value
# def add(a, b):
#     return a + b

# # 4 Function without argument but with return value
# def get_number():
#     return 100

# # 5. Function with default argument
# def greet(name="Student"):
#     print("Hello", name)

# # 6. Function with keyword arguments
# def student(name, branch, marks):
#     print("Name:", name)
#     print("Branch:", branch)
#     print("Marks:", marks)

# # 7. Function with variable number of arguments
# def total(*numbers):
#     return sum(numbers)

# 8 lambda function 
# square=lambda x:x*x
# print(square(5))

# add = lambda x, y: x + y
# print(add(3, 7)) 

# calls
# welcome()
# student("Jay", 20)
# result = add(10, 20)
# print("Addition:", result)
# number = get_number()
# print("Number:", number)
# greet()
# greet("Jay")
# student(name="Jay", branch="CSE", marks=85)
# print("Total:", total(10, 20, 30, 40))
# print("Square:", square(5))