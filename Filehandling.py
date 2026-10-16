#Q1  Program to create student.txt and write student details

# file = open("student.txt", "w")

# file.write("Name: Viraj Potdar\n")
# file.write("Roll Number: 101\n")
# file.write("Branch: Computer Science and Engineering\n")
# file.write("Semester: V\n")

# file.close()

# print("Student details written successfully.")


# Q2  open a text file and display its complete contents

# file=open("student.txt","r")
# reading=file.read()
# print(reading)

# Q3 append additional student information to an existing file without deleting its previous contents. 

# file=open("student.txt","a")

# file.write("Name: Kiran Patil\n")
# file.write("Roll Number: 102\n")
# file.write("Branch: ENTC\n")
# file.write("Semester: V\n")
# file.close()
# print("Appended 2nd Student details")


# Q4 Write a program to read a text file line by line and display each line separately. 
# file=open("student.txt","r")
 
# for line in file:
#     print(line.strip())
# file.close()

# Q5 to count and display the total number of lines present in a text file

# file=open("student.txt","r")
# count=0
# for line in file:
#     count+=1
# print("Total number of lines:",count)

# file.close()


#Q6 to count the total number of words present in a text file. 

# file=open("student.txt","r")
# count=0
# for words in file:
#      word=words.split()
#      count+=len(word)
# print(count)
# file.close()

#Q7  to count the total number of characters in a text file, including spaces.

# file = open("student.txt", "r")
# data = file.read()
# print("Total characters:", len(data))

# file.close()

#Q8 read a text file and display its lines in reverse order 

# file = open("student.txt", "r")

# lines = file.readlines()
# for line in reversed(lines):
#     print(line.strip())

# file.close()

#Q9 Count the number of vowels and consonants in a text file
# file = open("student.txt", "r")

# vowels = 0
# consonants = 0
# data = file.read()

# for ch in data:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# file.close()
# print("Vowels:", vowels)
# print("Consonants:", consonants)


#Q10 Count alphabets, digits, spaces and special characters

# file = open("student.txt", "r")

# alphabets = 0
# digits = 0
# spaces = 0
# special = 0

# data = file.read()

# for ch in data:
#     if ch.isalpha():
#         alphabets += 1
#     elif ch.isdigit():
#         digits += 1
#     elif ch == " ":
#         spaces += 1
#     else:
#         special += 1

# file.close()

# print("Alphabets:", alphabets)
# print("Digits:", digits)
# print("Spaces:", spaces)
# print("Special Characters:", special)


#Q11 Find the longest word in a text file
# file = open("student.txt", "r")

# data = file.read()
# words = data.split()

# longest = ""

# for word in words:
#     if len(word) > len(longest):
#         longest = word

# file.close()

# print("Longest word:", longest)
# print("Length:", len(longest))