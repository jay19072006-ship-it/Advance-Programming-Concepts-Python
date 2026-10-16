
# ==========================================
# PYTHON PRACTICAL PROGRAMS
# IF-ELSE, FOR LOOP, PATTERNS, WHILE LOOP
# ==========================================


# ========== 1. IF-ELSE PROGRAMS ==========

# 1. Check Zero or Non-Zero
# n = int(input("Enter number: "))
# if n == 0:
#     print("Number is Zero")
# else:
#     print("Number is Non-Zero")


# 2. Largest of Two Numbers
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# if a > b:
#     print(a, "is largest")
# elif b > a:
#     print(b, "is largest")
# else:
#     print("Both are equal")


# 3. Positive, Negative or Zero
# n = float(input("Enter number: "))
# if n > 0:
#     print("Positive")
# elif n < 0:
#     print("Negative")
# else:
#     print("Zero")


# 4. Vowel or Consonant
# ch = input("Enter a character: ")
# if len(ch) == 1 and ch.isalpha():
#     if ch.lower() in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonant")
# else:
#     print("Enter a single alphabet")


# 5. Student Performance
# a = int(input("Subject 1 marks: "))
# b = int(input("Subject 2 marks: "))
# c = int(input("Subject 3 marks: "))
# d = int(input("Subject 4 marks: "))
# total = a + b + c + d
# per = total / 400 * 100
# print("Total =", total, "out of 400")
# print("Percentage =", per)
# if per >= 90:
#     print("Excellent Performance")
# elif per >= 80:
#     print("Very Good Performance")
# elif per >= 70:
#     print("Good Performance")
# elif per >= 60:
#     print("Average Performance")
# else:
#     print("Poor Performance")


# 6. Largest of Three Numbers
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# if a >= b and a >= c:
#     print(a, "is largest")
# elif b >= a and b >= c:
#     print(b, "is largest")
# else:
#     print(c, "is largest")


# 7. Smallest of Three Numbers
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# if a <= b and a <= c:
#     print(a, "is smallest")
# elif b <= a and b <= c:
#     print(b, "is smallest")
# else:
#     print(c, "is smallest")


# 8. Even or Odd
# n = int(input("Enter number: "))
# if n % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# 9. Leap Year
# year = int(input("Enter year: "))
# if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")


# ========== 2. FOR LOOP PROGRAMS ==========

# 1. Print Natural Numbers
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     print(i)


# 2. Print Even Numbers
# n = int(input("Enter n: "))
# for i in range(2, n + 1, 2):
#     print(i)


# 3. Print Odd Numbers
# n = int(input("Enter n: "))
# for i in range(1, n + 1, 2):
#     print(i)


# 4. Print Powers of 2: 1, 2, 4, 8, 16...
# n = int(input("Enter n: "))
# for i in range(n + 1):
#     print(2 ** i)


# 5. Sum of Series: 1 + 1/1! + 1/2! + ... + 1/n!
# n = int(input("Enter n: "))
# total = 1
# fact = 1
# for i in range(1, n + 1):
#     fact = fact * i
#     total = total + 1 / fact
# print("Sum =", total)


# 6. Prime Number Using Square Root
# n = int(input("Enter number: "))
# prime = True
# if n <= 1:
#     prime = False
# else:
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             prime = False
#             break
# if prime:
#     print("Prime Number")
# else:
#     print("Not Prime")


# ========== 3. PATTERN PROGRAMS ==========

# 1. Print ABC Three Times
# for i in range(3):
#     for j in range(65, 68):
#         print(chr(j), end=" ")
#     print()


# 2. Increasing Alphabet Pattern
# n = int(input("Enter n: "))
# for i in range(n):
#     for j in range(i + 1):
#         print(chr(65 + j), end=" ")
#     print()


# 3. Decreasing Alphabet Pattern
# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     for j in range(i):
#         print(chr(65 + j), end=" ")
#     print()


# 4. Increasing Number Pattern
# n = int(input("Enter n: "))
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# 5. Decreasing Number Pattern
# n = int(input("Enter n: "))
# for i in range(n, 0, -1):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()


# ========== 4. WHILE LOOP PROGRAMS ==========

# 1. Print Natural Numbers
# n = int(input("Enter n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 1


# 2. Print Even Numbers
# n = int(input("Enter n: "))
# i = 2
# while i <= n:
#     print(i)
#     i += 2


# 3. Print Odd Numbers
# n = int(input("Enter n: "))
# i = 1
# while i <= n:
#     print(i)
#     i += 2


# 4. Sum of Natural Numbers
# n = int(input("Enter n: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 1
# print("Sum =", total)


# 5. Sum of Odd Numbers
# n = int(input("Enter n: "))
# i = 1
# total = 0
# while i <= n:
#     total += i
#     i += 2
# print("Sum =", total)


# 6. Sum of Even Numbers
# n = int(input("Enter n: "))
# i = 2
# total = 0
# while i <= n:
#     total += i
#     i += 2
# print("Sum =", total)


# 7. Print Natural Numbers in Reverse
# n = int(input("Enter n: "))
# while n >= 1:
#     print(n)
#     n -= 1


# 8. Fibonacci Series
# n = int(input("Enter number of terms: "))
# a = 0
# b = 1
# i = 1
# while i <= n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     i += 1
# print()


# 9. Factorial of a Number
# n = int(input("Enter number: "))
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print("Factorial =", fact)


# 10. Check Prime Number
# n = int(input("Enter number: "))
# i = 2
# prime = True
# if n <= 1:
#     prime = False
# else:
#     while i * i <= n:
#         if n % i == 0:
#             prime = False
#             break
#         i += 1
# if prime:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")


# 11. Sum of Digits
# n = int(input("Enter number: "))
# total = 0
# while n > 0:
#     digit = n % 10
#     total += digit
#     n //= 10
# print("Sum of digits =", total)


# 12. Palindrome Number
# n = int(input("Enter number: "))
# temp = n
# rev = 0
# while temp > 0:
#     digit = temp % 10
#     rev = rev * 10 + digit
#     temp //= 10
# if n >= 0 and n == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# 13. Reverse a Number
# n = int(input("Enter number: "))
# rev = 0
# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n //= 10
# print("Reverse =", rev)


# 14. Multiplication Table
# n = int(input("Enter number: "))
# i = 1
# while i <= 10:
#     print(n, "x", i, "=", n * i)
#     i += 1


# 15. Largest of N Numbers
# count = int(input("How many numbers? "))
# i = 1
# largest = None
# while i <= count:
#     num = int(input("Enter number: "))
#     if largest is None or num > largest:
#         largest = num
#     i += 1
# if count > 0:
#     print("Largest =", largest)
# else:
#     print("Enter at least one number")


# 16. Smallest of N Numbers
# count = int(input("How many numbers? "))
# i = 1
# smallest = None
# while i <= count:
#     num = int(input("Enter number: "))
#     if smallest is None or num < smallest:
#         smallest = num
#     i += 1
# if count > 0:
#     print("Smallest =", smallest)
# else:
#     print("Enter at least one number")
