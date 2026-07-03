
# Topic 4 — Loops

# ===================================================================

# Task 1 — Basic
# Using for loop and while loop separately:
# - Print numbers 1 to 50
# - Print even numbers from 1 to 100
# - Print odd numbers from 1 to 100
# - Print multiplication table of any number
# - Print sum of numbers from 1 to 100

# #Uing for loop
# for i in range(1,51):
#     print(i)

# for i in range(2,101,2):
#     print(i)

# for i in range(1,101,2):
#     print(i)

# num = int(input("Enter an number: "))

# for i in range(1,11):
#     print(num , "X" , i , " = " , num*i)

# total = 0

# for i in range(1,101):
#     total+=i

# print("Sum: ", total)

# #Using while loop
# i = 1
# while i <= 50:
#     print(i)
#     i += 1

# i = 2
# while i <= 100:
#     print(i)
#     i += 2

# i = 1
# while i <= 100:
#     print(i)
#     i += 2

# num = int(input("Enter a number: "))

# i = 1
# while i <= 10:
#     print(num, "x", i, "=", num * i)
#     i += 1

# i = 1
# total = 0

# while i <= 100:
#     total += i
#     i += 1

# print("Sum:", total)

# ===================================================================

# Task 2 — Intermediate
# - Take a list of 5 numbers as input
# - Find sum, average, max, min without using
#   built-in sum(), max(), min()
# - Count how many are positive, negative, zero
# - Print numbers in reverse order without
#   using reversed()
# - Check if list is sorted or not

# numbers = []

# for i in range(5):
#     num = int(input("Enter the numbers: "))
#     numbers.append(num)

# total = 0
# for num in numbers:
#     total += num

# average = total / len(numbers)

# maximum = numbers[0]
# for num in numbers:
#     if num > numbers:
#         num = maximum

# minimum = numbers[0]
# for num in numbers:
#     if num < minimum:
#         num = minimum

# positive = 0
# negative = 0
# zero = 0

# for num in numbers:
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
#     else:
#         zero += 1

# print("Reverse Order:")
# for i in range(len(numbers) - 1, -1, -1):
#     print(numbers[i], end=" ")
# print()

# sorted_list = True

# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         sorted_list = False
#         break

# print("Numbers:", numbers)
# print("Sum:", total)
# print("Average:", average)
# print("Maximum:", maximum)
# print("Minimum:", minimum)
# print("Positive:", positive)
# print("Negative:", negative)
# print("Zero:", zero)

# if sorted_list:
#     print("List is sorted")
# else:
#     print("List is not sorted")

# ==============================================================

# Task 3 — Logical Thinking
# Without running, trace the output step by step:

# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Write exactly what prints on each line
# Then verify by running

# Iteration 1
# i = 1

# Inner loop:
# j = 1

# Prints:
# 1

# Iteration 2
# i = 2

# Inner loop:
# j = 1
# j = 2

# Prints:
# 1 2

# Iteration 3
# i = 3

# Inner loop:
# j = 1
# j = 2
# j = 3

# Prints:
# 1 2 3

# Iteration 4
# i = 4

# Inner loop:
# j = 1
# j = 2
# j = 3
# j = 4

# Prints:
# 1 2 3 4

# Iteration 5
# i = 5

# Inner loop:
# j = 1
# j = 2
# j = 3
# j = 4
# j = 5

# Prints:
# 1 2 3 4 5

# #Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# ===========================================================================

# Task 4 — Problem Solving
# Build a number guessing game:
# - Computer picks a number between 1 and 100
#   (use: import random → random.randint(1, 100))
# - User keeps guessing until correct
# - Print "Too High" or "Too Low" as hints
# - Count number of attempts
# - Print "Excellent" if guessed in <= 5 attempts
# - Print "Good" if guessed in <= 10 attempts
# - Print "Keep practicing" if more than 10
# - Ask user if they want to play again

# import random

# while True:
#     number = random.randint(1, 100)
#     attempts = 0

#     print("\nGuess the number between 1 and 100")

#     while True:
#         guess = int(input("Enter your guess: "))
#         attempts += 1

#         if guess > number:
#             print("Too High")
#         elif guess < number:
#             print("Too Low")
#         else:
#             print("Correct! You guessed the number.")
#             print("Attempts:", attempts)

#             if attempts <= 5:
#                 print("Excellent")
#             elif attempts <= 10:
#                 print("Good")
#             else:
#                 print("Keep practicing")
#             break

#     choice = input("Do you want to play again? (yes/no): ").lower()

#     if choice != "yes":
#         print("Thanks for playing!")
#         break

# =======================================================================

# Task 5 — Advanced
# 1. Print all prime numbers between 1 and 100
#    using nested loops and for-else

# 2. Using zip() and enumerate() together:
#    - Take two lists of 5 students names and marks
#    - Print rank, name, marks, pass/fail
#    - Sort by marks and reprint with new ranks

# 3. FizzBuzz:
#    - Print numbers 1 to 100
#    - Multiple of 3 → print "Fizz"
#    - Multiple of 5 → print "Buzz"
#    - Multiple of both → print "FizzBuzz"
#    - Otherwise → print the number

# 4. Find all numbers between 1 and 500
#    that are divisible by 3 and 7 both
#    Print them and their count

# 1. Print all prime numbers between 1 and 100 using nested loops and for-else

# print("Prime Numbers:")

# for num in range(2, 101):
#     for i in range(2, num):
#         if num % i == 0:
#             break
#     else:
#         print(num, end=" ")

# print()


# # 2. Using zip() and enumerate()

# names = []
# marks = []

# print("\nEnter 5 Student Names:")
# for i in range(5):
#     names.append(input("Name: "))

# print("\nEnter 5 Student Marks:")
# for i in range(5):
#     marks.append(int(input("Marks: ")))

# print("\nStudent Result")

# for rank, (name, mark) in enumerate(zip(names, marks), start=1):
#     result = "Pass" if mark >= 35 else "Fail"
#     print(rank, name, mark, result)

# students = list(zip(names, marks))
# students.sort(key=lambda x: x[1], reverse=True)

# print("\nSorted by Marks")

# for rank, (name, mark) in enumerate(students, start=1):
#     result = "Pass" if mark >= 35 else "Fail"
#     print(rank, name, mark, result)


# # 3. FizzBuzz

# print("\nFizzBuzz")

# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)


# # 4. Numbers divisible by both 3 and 7 between 1 and 500

# count = 0

# print("\nNumbers divisible by both 3 and 7:")

# for i in range(1, 501):
#     if i % 3 == 0 and i % 7 == 0:
#         print(i, end=" ")
#         count += 1

# print("\nCount:", count)

# ==================================================================
