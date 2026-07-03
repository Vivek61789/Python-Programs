

# Topic2 -- Operators 

# ================================================================

# Task 1 — Basic
# Given a = 15, b = 4
# Calculate and print all arithmetic operations
# Also print type of each result
# Use pow(), divmod(), abs() functions

# a = 15
# b = 4

# c = a + b
# d = a - b
# e = a ** b
# f = a * b
# g = a % b
# h = a / b
# i = a // b

# print(c, type(c))
# print(d, type(d))
# print(e, type(e))
# print(f, type(f))
# print(g, type(g))
# print(h, type(h))
# print(i, type(i))

# print(pow(a, b))
# print(divmod(a, b))
# print(abs(-10))

# ===================================================================

# Task 2 — Intermediate
# Take a number
# Check and print:
# - Even or Odd (use ternary operator)
# - Positive, Negative or Zero (use ternary)
# - Divisible by both 3 and 5
# - Last digit
# - Binary, Hex, Octal representation

# a = 10

# result = "Even" if a % 2 == 0 else "Odd"
# print(result)

# result1 = "Positive" if a > 0 else "Negative" if a < 0 else "Zero"
# print(result1)

# result2 = "Divisible by both 3 and 5" if a % 3 == 0 and a % 5 == 0 else "Not divisible by both 3 and 5"
# print(result2)

# print(a % 10)

# print(bin(a))
# print(hex(a))
# print(oct(a))

# ======================================================================

# Task 3 — Logical Thinking
# Without running, find output step by step:
# x = 10
# y = 3
# print(x // y + x % y * 2 - y ** 2)
# Write each step using precedence rules
# Then verify by running

# Parentheses: ()
# Exponentiation: ** (Right-to-left associativity)
# Unary Operators: +x, -x, ~x (Right-to-left)
# Multiplication/Division: *, /, //, % (Left-to-right)
# Addition/Subtraction: +, - (Left-to-right)
# Bitwise Shifts: <<, >> (Left-to-right)
# Bitwise AND: & (Left-to-right)
# Bitwise XOR: ^ (Left-to-right)
# Bitwise OR: | (Left-to-right)
# Comparisons: ==, !=, >, >=, <, <=, is, is not, in, not in (Left-to-right)
# Logical NOT: not (Right-to-left)
# Logical AND: and (Left-to-right)
# Logical OR: or (Left-to-right)
# Conditional Expression: if...else (Right-to-left)
# Assignment: =, +=, -=, etc. (Right-to-left) 

# x = 10
# y = 3
# print(x // y + x % y * 2 - y ** 2) #output : -4

#==============================================================================

# Task 4 — Problem Solving
# A student has marks in 5 subjects
# Using all(), any(), sum(), min(), max():
# - Check if passed in all subjects (>= 35)
# - Check if failed in any subject
# - Total and Average
# - Highest and Lowest mark
# - Grade using ternary operator

# a = 40
# b = 33
# c = 70
# d = 56
# e = 75

# marks=[a,b,c,d,e]

# print("Passed in all the subjects: ", all(mark >=35 for mark in marks)) #function(expression for variable in iterable)
# print("Fail in any subject: ", any(mark < 35 for mark in marks))        #all(condition for item in collection) #any(condition for item in collection)

# Total = sum(marks)
# print("Total: ",Total)

# Average = Total / len(marks)
# print(Average)

# print("Highest: ",max(marks))
# print("Lowest: ",min(marks))

# grade = "Pass" if Average>=35 else "Fail"
# print("Grade: ", grade)

# =====================================================================

# Task 5 — Advanced
# 1. Use walrus operator to take input until user types "quit"
#    and count how many inputs were given

# 2. Create a complex number c = 5 + 3j
#    Print real, imaginary parts
#    Add two complex numbers

# 3. Swap two numbers using XOR bitwise operator

# 4. Find if a year is leap year using only logical operators
#    (divisible by 4, not 100, unless also 400)

# #1
# count = 0

# while(text := input("Enter any value:")) != "quit" :
#     count += 1
# print("Total entred vales: " ,count)

# #2
# c = 5+3j
# print("Complex Number: ",c)
# print("Real: ", c.real)
# print("Imaginary: ", c.imag)

# d = 3+5j
# print(c+d)

# #3
# a = 2
# b = 3

# print("Before swap: ",a,b)

# a = a ^ b
# b = a ^ b
# a = a ^ b

# print("After swpap: ",a,b)

# #4
# year = int(input("Enter an year: "))

# if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) :
#     print("Leap year: ", year)
# else:
#     print("Not Leap year: ", year)    

# ====================================================================




