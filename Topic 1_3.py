# Task 3 — Logical Thinking

# python
# x = "5"
# y = 3
# print(x + y)  # Will this work? Why or why not?
# # Fix it and print the result as 8

# No. Python will raise a TypeError.

# The reason is that x and y have different data types:

x = "5"   # str
y = 3     # int

# Python cannot directly use + to add a str and an int.

# You will get an error similar to:

# TypeError: can only concatenate str (not "int") to str

x = "5"
y = 3

x = int(x)

print(x + y) #Output is 8


















