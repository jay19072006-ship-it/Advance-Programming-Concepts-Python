# Class and destructor

# class Student:
#     def __init__(self, name, roll_no, marks):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks = marks

#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll_no)
#         print("Marks:", self.marks)

#     def __del__(self):
#         print("\nStudent object is destroyed.")

# name = input("Enter Student Name: ")
# roll_no = int(input("Enter Roll No: "))
# marks = float(input("Enter Marks: "))
# student1 = Student(name, roll_no, marks)
# print("\nStudent Details")
# student1.display()
# del student1


# Inheritance types 

# Single level inheritance

# class A:
#     def show_A(self):
#         print("From class A")

# class B(A):
#     def show_B(self):
#         print("From class B")

# obj = B()
# obj.show_A()
# obj.show_B()


# Multilevel inheritance

# class A:
#     def show_A(self):
#         print("From class A")

# class B(A):
#     def show_B(self):
#         print("From class B")


# class C(B):
#     def show_C(self):
#         print("From class C")
# obj = C()

# obj.show_A()
# obj.show_B()
# obj.show_C()

# Multiple Inheritance
# Public, Protected and Private

# class A:
#     def show_A(self):
#         self.name = "Viraj"          # Public
#         self._roll_no = 24          # Protected
#         self.__marks = 90            # Private
        
#         print("Name:", self.name)
#         print("Roll No:", self._roll_no)
#         print("Marks:", self.__marks)


# class B:
#     def show_B(self):
#         print("\n")
#         print("Class B we can access name:",self.name)
#         print("Class B we can access rollno:",self._roll_no)


# class C(A, B):
#     def show_C(self):
#         print("\n")
#         print("Class C we can access name:",self.name)
#         print("Class C we can access rollno:",self._roll_no)
        


# obj = C()

# obj.show_A()
# obj.show_B()
# obj.show_C()

# print("Public:", obj.name)
# print("Protected:", obj._roll_no)



# Hierarchical Inheritance

# class A:
#     def show_A(self):
#         print("From class A")


# class B(A):
#     def show_B(self):
#         print("From class B")


# class C(A):
#     def show_C(self):
#         print("From class C")

# obj1 = B()
# obj2 = C()

# obj1.show_A()
# obj1.show_B()

# obj2.show_A()
# obj2.show_C()

# # Hybrid Inheritance

# class A:
#     def show_A(self):
#         print("From class A")


# class B(A):
#     def show_B(self):
#         print("From class B")


# class C(A):
#     def show_C(self):
#         print("From class C")


# class D(B, C):
#     def show_D(self):
#         print("From class D")


# obj = D()

# obj.show_A()
# obj.show_B()
# obj.show_C()
# obj.show_D()