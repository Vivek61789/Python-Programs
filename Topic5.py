

# Topic 5 — Functions

# =========================================================================

# Task 1 — Basic
# Write functions for:
# 1. Greet a person by name (with default greeting)
# 2. Calculate area of circle, rectangle, triangle
# 3. Convert Celsius to Fahrenheit and vice versa
# 4. Check if a number is even or odd
# 5. Find largest of three numbers

# Each function must:
# - Have proper parameters
# - Return a value
# - Have a docstring

# import math

# # 1. Greet a person by name (with default greeting)
# def greet(name, greeting="Hello"):
#     """Returns a greeting message."""
#     return f"{greeting}, {name}!"

# print(greet("Vivek"))


# # 2. Calculate area of circle
# def area_circle(radius):
#     """Returns the area of a circle."""
#     return math.pi * radius ** 2

# print(area_circle(5))


# # Calculate area of rectangle
# def area_rectangle(length, width):
#     """Returns the area of a rectangle."""
#     return length * width

# print(area_rectangle(10, 5))


# # Calculate area of triangle
# def area_triangle(base, height):
#     """Returns the area of a triangle."""
#     return 0.5 * base * height

# print(area_triangle(10, 6))


# # 3. Convert Celsius to Fahrenheit
# def celsius_to_fahrenheit(celsius):
#     """Converts Celsius to Fahrenheit."""
#     return (celsius * 9 / 5) + 32

# print(celsius_to_fahrenheit(25))


# # Convert Fahrenheit to Celsius
# def fahrenheit_to_celsius(fahrenheit):
#     """Converts Fahrenheit to Celsius."""
#     return (fahrenheit - 32) * 5 / 9

# print(fahrenheit_to_celsius(77))


# # 4. Check if a number is even or odd
# def even_or_odd(num):
#     """Returns Even if the number is even, otherwise Odd."""
#     return "Even" if num % 2 == 0 else "Odd"

# print(even_or_odd(10))


# # 5. Find largest of three numbers
# def largest(a, b, c):
#     """Returns the largest of three numbers."""
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c

# print(largest(10, 25, 15))

# =======================================================================

# Task 2 — Intermediate
# 1. Write a function using *args that:
#    - Accepts any number of marks
#    - Returns total, average, min, max, grade

# 2. Write a function using **kwargs that:
#    - Accepts any student details
#    - Prints a formatted student card

# 3. Write a function with both *args and **kwargs:
#    - Accepts subject marks (*args)
#    - Accepts student info (**kwargs)
#    - Prints complete report card

# # 1. Function using *args

# def student_marks(*args):
#     total = sum(args)
#     average = total / len(args)
#     minimum = min(args)
#     maximum = max(args)

#     grade = (
#         "A+" if average >= 90 else
#         "A" if average >= 80 else
#         "B" if average >= 70 else
#         "C" if average >= 60 else
#         "D" if average >= 50 else
#         "Fail"
#     )

#     return total, average, minimum, maximum, grade


# total, average, minimum, maximum, grade = student_marks(80, 75, 90, 65, 88)

# print("Total:", total)
# print("Average:", average)
# print("Minimum:", minimum)
# print("Maximum:", maximum)
# print("Grade:", grade)


# # 2. Function using **kwargs

# def student_details(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")


# student_details(
#     Name="Vivek",
#     Age=21,
#     Roll_No=101,
#     Branch="CSE"
# )


# # 3. Function using *args and **kwargs

# def report_card(*args, **kwargs):
#     total = sum(args)
#     average = total / len(args)

#     grade = (
#         "A+" if average >= 90 else
#         "A" if average >= 80 else
#         "B" if average >= 70 else
#         "C" if average >= 60 else
#         "D" if average >= 50 else
#         "Fail"
#     )

#     print("\n----- Report Card -----")

#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

#     print("Marks:", args)
#     print("Total:", total)
#     print("Average:", average)
#     print("Grade:", grade)


# report_card(
#     80, 75, 90, 65, 88,
#     Name="Vivek",
#     Roll_No=101,
#     Branch="CSE"
# )

# ====================================================================

# Task 3 — Logical Thinking
# Trace the output without running:

# def mystery(n):
#     if n == 0:
#         return 0
#     return n + mystery(n - 1)

# print(mystery(5))

# Write each recursive call step by step
# Then verify by running
# Explain what this function actually does

# Step 1: Recursive Calls
# mystery(5)
# = 5 + mystery(4)

# mystery(4)
# = 4 + mystery(3)

# mystery(3)
# = 3 + mystery(2)

# mystery(2)
# = 2 + mystery(1)

# mystery(1)
# = 1 + mystery(0)

# mystery(0)
# = 0
# Step 2: Returning Values (Backtracking)

# Now Python returns from the last function call.

# mystery(0)
# = 0
# mystery(1)
# = 1 + 0
# = 1
# mystery(2)
# = 2 + 1
# = 3
# mystery(3)
# = 3 + 3
# = 6
# mystery(4)
# = 4 + 6
# = 10
# mystery(5)
# = 5 + 10
# = 15
# Final Output
# 15

# ========================================================================

# Task 4 — Problem Solving
# Build a simple calculator using functions:
# 1. add(a, b)
# 2. subtract(a, b)
# 3. multiply(a, b)
# 4. divide(a, b) — handle division by zero
# 5. power(base, exp)
# 6. factorial(n) — use recursion
# 7. is_prime(n) — check if prime

# Main function:
# - Show menu to user
# - Take input and call the right function
# - Show result
# - Ask if user wants to continue

# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     if b == 0:
#         return "Division by zero is not possible."
#     return a / b


# def power(base, exp):
#     return base ** exp


# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)


# def is_prime(n):
#     if n <= 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# def main():
#     while True:
#         print("\n----- Calculator Menu -----")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. Power")
#         print("6. Factorial")
#         print("7. Prime Check")

#         choice = int(input("Enter your choice: "))

#         if choice in [1, 2, 3, 4, 5]:
#             a = int(input("Enter first number: "))
#             b = int(input("Enter second number: "))

#             if choice == 1:
#                 print("Result:", add(a, b))

#             elif choice == 2:
#                 print("Result:", subtract(a, b))

#             elif choice == 3:
#                 print("Result:", multiply(a, b))

#             elif choice == 4:
#                 print("Result:", divide(a, b))

#             elif choice == 5:
#                 print("Result:", power(a, b))

#         elif choice == 6:
#             n = int(input("Enter a number: "))
#             print("Result:", factorial(n))

#         elif choice == 7:
#             n = int(input("Enter a number: "))
#             if is_prime(n):
#                 print("Prime Number")
#             else:
#                 print("Not a Prime Number")

#         else:
#             print("Invalid Choice")

#         again = input("Do you want to continue? (yes/no): ").lower()

#         if again != "yes":
#             print("Thank You!")
#             break

# main()

# ============================================================================

# Task 5 — Advanced
# 1. Write a function that:
#    - Takes a list of student names and marks
#    - Uses lambda with sorted() to rank students
#    - Uses map() to assign grades
#    - Uses filter() to get passed students
#    - Returns ranked list with grades

# 2. Write a recursive function:
#    - Binary search (find number in sorted list)
#    - Explain each recursive call

# 3. Write a higher order function:
#    - apply_twice(func, value)
#    - Applies any function twice on value
#    - Test with: double, square, add_10

# 4. Validate user input using functions:
#    - validate_age(age) → must be 0-150
#    - validate_email(email) → must have @ and .
#    - validate_password(pwd) → min 8 chars,
#      must have number and letter
#    - Keep asking until valid input received

# # 1. Student Ranking using lambda, map(), filter()

# def student_result(names, marks):
#     students = list(zip(names, marks))

#     ranked = sorted(students, key=lambda x: x[1], reverse=True)

#     grades = list(map(lambda x:
#         "A+" if x >= 90 else
#         "A" if x >= 80 else
#         "B" if x >= 70 else
#         "C" if x >= 60 else
#         "D" if x >= 50 else
#         "Fail", marks))

#     passed = list(filter(lambda x: x[1] >= 35, students))

#     result = []

#     for i in range(len(ranked)):
#         name, mark = ranked[i]

#         if mark >= 90:
#             grade = "A+"
#         elif mark >= 80:
#             grade = "A"
#         elif mark >= 70:
#             grade = "B"
#         elif mark >= 60:
#             grade = "C"
#         elif mark >= 50:
#             grade = "D"
#         else:
#             grade = "Fail"

#         result.append((i + 1, name, mark, grade))

#     return result


# names = ["Vivek", "Rahul", "Ajay", "Ram", "Kiran"]
# marks = [85, 92, 67, 45, 76]

# print(student_result(names, marks))

# # 2. Recursive Binary Search

# def binary_search(arr, left, right, target):
#     print("Searching:", arr[left:right+1])

#     if left > right:
#         return -1

#     mid = (left + right) // 2

#     if arr[mid] == target:
#         return mid

#     elif target < arr[mid]:
#         return binary_search(arr, left, mid - 1, target)

#     else:
#         return binary_search(arr, mid + 1, right, target)


# numbers = [10, 20, 30, 40, 50, 60, 70]

# print(binary_search(numbers, 0, len(numbers) - 1, 50))

# Recursive Calls Example (Searching 50):

# Searching: [10, 20, 30, 40, 50, 60, 70]
# mid = 40

# Searching: [50, 60, 70]
# mid = 60

# Searching: [50]
# Found at index 4

# # 3. Higher Order Function

# def apply_twice(func, value):
#     return func(func(value))


# def double(x):
#     return x * 2


# def square(x):
#     return x ** 2


# def add_10(x):
#     return x + 10


# print(apply_twice(double, 5))
# print(apply_twice(square, 2))
# print(apply_twice(add_10, 5))

# # 4. Validation Functions

# def validate_age(age):
#     return 0 <= age <= 150


# def validate_email(email):
#     return "@" in email and "." in email


# def validate_password(password):
#     if len(password) < 8:
#         return False

#     has_letter = False
#     has_number = False

#     for ch in password:
#         if ch.isalpha():
#             has_letter = True
#         if ch.isdigit():
#             has_number = True

#     return has_letter and has_number


# while True:
#     age = int(input("Enter Age: "))
#     if validate_age(age):
#         break
#     print("Invalid Age")


# while True:
#     email = input("Enter Email: ")
#     if validate_email(email):
#         break
#     print("Invalid Email")


# while True:
#     password = input("Enter Password: ")
#     if validate_password(password):
#         break
#     print("Invalid Password")

# print("All Inputs are Valid.")

# ==========================================================================






