# Simple Exception Handling code

# try:
#     n=1
#     res=100/n
# except ZeroDivisionError:
#     print("You can't divide by zero")
    
# except ValueError:
#     print("Enter the valid number")
# else:
#     print("Result is:",res)
# finally:
#     print("Excecution Complete")


# 2 Index Error
# try:
#     numbers = [10, 20, 30]
#     print(numbers[5])

# except IndexError:
#     print("Index does not exist")


# 3 FileNotFoundError  
# try:
#     file = open("abc.txt", "r")
#     print(file.read())

# except FileNotFoundError:
#     print("File not found")


# 4
# class AgeError(Exception):
#     pass

# try:
#     age = int(input("Enter age: "))

#     if age < 18:
#         raise AgeError("Age must be 18 or above")

#     print("Valid age")

# except AgeError as e:
#     print("Error:", e)

  
    
# User defined Exception

# class InsufficientFundError(Exception):
#     def __init__(self, bal,amt):
#         self.bal=bal
#         self.amt=amt
#         super().__init__(f"Cant withdraw balance is only {bal}")
    
# class BankAccount:
#     def __init__(self,bal):
#         self.bal=bal
        
#     def withdraw(self,amt):
#         if amt>self.bal:
#             raise InsufficientFundError(self.bal,amt)
#         self.bal-=amt
#         return self.bal

# acc=BankAccount(500)

# try:
#     amt = int(input("Enter amount you want to withdraw: "))
#     balance = acc.withdraw(amt)

# except InsufficientFundError as e:
#     print("Transaction failed:", e)

# else:
#     print("Withdrawal successful")
#     print("Remaining balance:", balance)
# finally:
#     print("Thanks for using our banking System")
    
    
# Regular Expression

# import re
# text = "jay@gmail.com"

# result = re.match(r"\w+", text)
# if result:
#     print("Match:", result.group())
# else:
#     print("Not Found")

# result = re.search(r"gmail", text)
# if result:
#     print("Search:", result.group())
# else:
#     print("Not Found")
    
# pattern = re.compile(r"\w+@\w+\.\w+")
# result = pattern.search(text)
# if result:
#     print("Compile:", result.group())
# else:
#     print("Not found")

# result = re.findall(r"\w+", text)
# print("Findall:", result)


import re


def check_email(email):
    pattern = r"^[\w.-]+@[\w.-]+\.\w+$"

    if re.match(pattern, email):
        print("Valid Email")
    else:
        print("Invalid Email")


def check_phone(phone):
    pattern = r"^[0-9]{10}$"

    if re.match(pattern, phone):
        print("Valid Phone Number")
    elif len(phone) < 10:
        print("Enter 10 digit phone number")
    else:
        print("Invalid Phone Number")

def check_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@_]).+$"

    if re.match(pattern, password):
        print("Valid Password")
    else:
        print("Invalid Password")


email = input("Enter Email: ")
phone = input("Enter Phone Number: ")
password = input("Enter Password: ")

check_email(email)
check_phone(phone)
check_password(password)