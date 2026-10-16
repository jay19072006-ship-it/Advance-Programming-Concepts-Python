# Reading and writing in the file 

# file=open("report.txt", "w+")
# print ("writing in the file")
# print() 

# while True:
#  line= input("Enter a sentence ")
#  file.write(line)
#  file.write('\n')
#  choice=input("Do you wish to enter more data? (y/n): ")
#  if choice in ('n','N'): break
 
# print("The byte position of file object is ",file.tell())
# file.seek(0) 
# print()

# print("File contains(Reading from file):")
# str=file.read()
# print(str)
# file.close()



# # 1 read -r
# print("\n read")
# file = open("report.txt", "r")
# data = file.read()
# print(data)
# file.close()


# # 2. write -w
# print("\n Write")
# file = open("report.txt", "w")
# line = input("Enter text to write: ")
# file.write(line)
# file.close()

# # 3. Append -a
# print("\n append -a")
# file = open("report.txt", "a")
# line = input("Enter text to append: ")
# file.write("\n" + line)
# file.close()

# # 4. read + write r+
# print("\nread + write r+")

# file = open("report.txt", "r+")
# line = input("Enter text: ")
# file.write(line)
# file.seek(0)
# data = file.read()
# print("File content:", data)
# file.close()


# # 5. write + read w+
# print("\nwrite + read w+")
# file = open("report.txt", "w+")
# line = input("Enter text: ")
# file.write(line)
# file.seek(0)
# data = file.read()
# print("File content:", data)
# file.close()


# # 6. append + read a+
# print("\nappend + read a+")
# file = open("report.txt", "a+")
# line = input("Enter text to append: ")
# file.write("\n" + line)
# file.seek(0)
# data = file.read()
# print("File content:", data)
# file.close()


# # 7. create new file (empty file)  x
# print("\nCreate new empty file x")
# try:
#     file = open("new_report.txt", "x")
#     file.write("This is a newly created file.")
#     file.close()
#     print("new_report.txt created successfully.")
# except FileExistsError:
#     print("new_report.txt already exists.")

# # 8. read binary rb
# print("\n read binary rb")
# file = open("report.txt", "rb")
# data = file.read()
# print(data)
# file.close()


# # 9. Write binary  wb 
# print("\nWrite binary wb")
# file = open("binary_report.txt", "wb")
# data = input("Enter text for binary file: ")
# file.write(data.encode())
# file.close()


# # 10. append binary ab
# print("\n append binary ab")
# file = open("binary_report.txt", "ab")
# data = input("Enter text to append to binary file: ")
# file.write(("\n" + data).encode())
# file.close()


f = open("report.txt", "r")

print(f.tell())      
f.seek(5)            
print(f.tell())      

f.close()




# Directory Basic code 

import os

# 1. Working directory
# print("\nWorking directory",os.getcwd())

# # 2. List directory
# print("\nList directory",os.listdir())

# # 3. Create directory
# print("\nCreate directory")
# if not os.path.exists("myfolder"):
#     os.mkdir("myfolder")
#     print("Directory created")
# else:
#     print("Directory already exists")

# 4. RENAME FILE
# print("\nrename file")
# os.rename("new1_report.txt", "new_report.txt")


# 5. Change Path 
print("\n Change Directory")
os.chdir(r"D:\Sem_V\Training_5")
print("Current directory",)

# 6 Delete folder
# print("\n Delete empty folder")6
# os.rmdir("myfolder")