
# Topic 3 — Conditionals 

# ==================================================================

# Task 1 — Basic
# Take age as input
# Print:
# - "Child"    if age < 13
# - "Teenager" if age between 13 and 17
# - "Adult"    if age between 18 and 59
# - "Senior"   if age >= 60
# - "Invalid"  if age < 0

# age = int(input("Enter your age: "))

# if age < 0:
#     print("Invalid")
# elif age < 13:
#     print("Child")
# elif age >= 13 and age <= 17:
#     print("Teenager")
# elif age >= 18 and age <= 59:
#     print("Adult")
# else:
#     print("Senior")      

#===================================================================

# Task 2 — Intermediate
# Take a number as input
# Check and print:
# - Positive, Negative or Zero
# - Even or Odd
# - Divisible by 2, 3, and 5 (check each separately)
# - If it is a single digit, double digit, or more
# - Use ternary operator for even/odd check

# num = int(input("Enter a number: "))

# # Positive, Negative or Zero
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# # Even or Odd (using ternary operator)
# print("Even" if num % 2 == 0 else "Odd")

# # Divisible by 2
# if num % 2 == 0:
#     print("Divisible by 2")
# else:
#     print("Not Divisible by 2")

# # Divisible by 3
# if num % 3 == 0:
#     print("Divisible by 3")
# else:
#     print("Not Divisible by 3")

# # Divisible by 5
# if num % 5 == 0:
#     print("Divisible by 5")
# else:
#     print("Not Divisible by 5")

# # Single digit, Double digit or More
# digits = len(str(abs(num)))   # abs() ignores the negative sign

# if digits == 1:
#     print("Single Digit")
# elif digits == 2:
#     print("Double Digit")
# else:
#     print("More than Double Digit")

#======================================================================

# Task 3 — Logical Thinking
# A bank gives loan based on these rules:
# - Age must be between 21 and 60
# - Salary must be >= 25000
# - Credit score must be >= 700
# - If all conditions met → "Loan Approved"
# - If age fails → "Age not eligible"
# - If salary fails → "Salary too low"
# - If credit score fails → "Credit score too low"
# - If multiple fail → show all reasons

# a = int(input("Enter your age: "))
# b = int(input("Enter your salary: "))
# c = int(input("Enter your credit score: "))

# approved = True

# if a < 21 or a > 60:
#     print("Age not eligible")
#     approved = False

# if b < 25000:
#     print("Salary too low")
#     approved = False

# if c < 700:
#     print("Credit score too low")
#     approved = False

# if approved:
#     print("Loan Approved")

#================================================================

# Task 4 — Problem Solving
# Build a simple calculator:
# - Take two numbers and an operator (+, -, *, /, //, %, **)
# - Perform the operation using if-elif-else
# - Handle division by zero
# - Handle invalid operator
# - Use match-case as well and compare both approaches

# #Using if-elif-else
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /, //, %, **): ")

# if op == "+":
#     print("Result:", a + b)

# elif op == "-":
#     print("Result:", a - b)

# elif op == "*":
#     print("Result:", a * b)

# elif op == "/":
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Division by zero is not possible.")

# elif op == "//":
#     if b != 0:
#         print("Result:", a // b)
#     else:
#         print("Division by zero is not possible.")

# elif op == "%":
#     if b != 0:
#         print("Result:", a % b)
#     else:
#         print("Division by zero is not possible.")

# elif op == "**":
#     print("Result:", a ** b)

# else:
#     print("Invalid operator")

# #Using match-case
# a = float(input("Enter first number: "))
# b = float(input("Enter second number: "))
# op = input("Enter operator (+, -, *, /, //, %, **): ")

# match op:
#     case "+":
#         print("Result:", a + b)

#     case "-":
#         print("Result:", a - b)

#     case "*":
#         print("Result:", a * b)

#     case "/":
#         if b != 0:
#             print("Result:", a / b)
#         else:
#             print("Division by zero is not possible.")

#     case "//":
#         if b != 0:
#             print("Result:", a // b)
#         else:
#             print("Division by zero is not possible.")

#     case "%":
#         if b != 0:
#             print("Result:", a % b)
#         else:
#             print("Division by zero is not possible.")

#     case "**":
#         print("Result:", a ** b)

#     case _:
#         print("Invalid operator")

# ======================================================================

# Task 5 — Advanced
# Build a student result system:
# - Take marks of 5 subjects as input
# - Use all() to check if passed in all (>= 35)
# - Use any() to check if failed in any
# - Calculate total, average using sum()
# - Find highest and lowest using max(), min()
# - Assign grade using nested ternary
# - Print a full result card:
#     Name, Marks, Total, Average,
#     Highest, Lowest, Grade, Pass/Fail
# - Handle invalid marks (< 0 or > 100)

# name = input("Enter student name: ")

# marks = []

# for i in range(1,6):
#     mark = int(input(f"Enter the student marks{i}:  "))

#     if mark < 0 or mark > 100:
#         print("Invalid marks")
#         exit()

#     marks.append(mark)

# passed = all(mark >= 35 for mark in marks)
# failed = any(mark < 35 for mark in marks)

# total = sum(marks)
# average = total / len(marks)

# highest = max(marks)
# lowest = min(marks)

# grade = (
#     "A+" if average >= 90 else
#     "A" if average >= 80 else
#     "B" if average >= 70 else
#     "C" if average >= 60 else
#     "D" if average >= 50 else
#     "E" if average >= 35 else
#     "F"
# )

# print("\n----- STUDENT RESULT CARD -----")
# print("Name:", name)
# print("Marks:", marks)
# print("Total:", total)
# print("Average:", average)
# print("Highest:", highest)
# print("Lowest:", lowest)
# print("Grade:", grade)
# print("Pass" if passed else "Fail")

# ==================================================================



