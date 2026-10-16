# 1] Text processing

# text = str(input("Enter sentence: "))
# textlower = text.lower()

# print("Lowercase text:", textlower)
# print("Number of words:", len(text.split()))

# old_word = input("Enter word to replace: ")
# new_word = input("Enter new word: ")
# text = text.replace(old_word, new_word)
# print("New sentence:", text)


#2] Word Tokenization

# import nltk
# from nltk.tokenize import word_tokenize

# text = input("Enter a sentence: ")
# words = word_tokenize(text)

# print("Original Text:", text)
# print("Tokens:", words)



#3] Stop Word Removal

# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# text = input("Enter a sentence: ")
# words = word_tokenize(text)

# stop_words = set(stopwords.words('english'))
# result = []

# for word in words:
#     if word.lower() not in stop_words:
#         result.append(word)

# print("Original Words:", words)
# print("After Removing Stop Words:", result)



#4 Class and Constructor
class Student:

    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Marks:", self.marks)


name = input("Enter Student Name: ")
roll_no = int(input("Enter Roll No: "))
marks = float(input("Enter Marks: "))

student1 = Student(name, roll_no, marks)

print("\n Student Details ")
student1.display()