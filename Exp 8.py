# # Polymorphism through method overriding
# class Animal:
# 	def sound(self):
# 		return "Animal makes a sound"


# class Dog(Animal):
# 	def sound(self):
# 		return "Dog barks"


# class Cat(Animal):
# 	def sound(self):
# 		return "Cat meows"


# print("Method overriding")
# animals = [Dog(), Cat()]
# for animal in animals:
# 	print(animal.sound())


# # Program 2: Polymorphism through duck typing
# class Car:
# 	def move(self):
# 		return "Car is driving"


# class Boat:
# 	def move(self):
# 		return "Boat is sailing"


# def start_moving(vehicle):
# 	print(vehicle.move())


# print("\nDuck typing")
# start_moving(Car())
# start_moving(Boat())


# # Program 3: Polymorphism through operator overloading
# class Number:
# 	def __init__(self, value):
# 		self.value = value

# 	def __add__(self, other):
# 		return Number(self.value + other.value)

# 	def __str__(self):
# 		return str(self.value)


# print("\nOperator overloading")
# first_number = Number(10)
# second_number = Number(20)
# print("Sum:", first_number + second_number)