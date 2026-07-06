

#Write a program that defines a function greet which prints "Hello, World!" and calls this function.
def greet():
    print("Hello, World!")

greet()

#Write a program that defines a function add which takes two numbers as parameters, adds them, and returns the result.
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = add(num1, num2)

print("Sum:", result)

#Write an example function program to find the greatest number from 3 numbers.
def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

print("Greatest Number:", greatest(num1, num2, num3))

#Write an example function program to find a given string is palindrome or not.
def palindrome(string):
    if string == string[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"

text = input("Enter a string: ")

print(palindrome(text))

#Write an example function program to reverse a string by using a for loop.
def reverse_string(string):
    reverse = ""

    for ch in string:
        reverse = ch + reverse

    return reverse

text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))

#Write a Python function to sum all the numbers in a list.
def sum_list(numbers):
    return sum(numbers)

numbers = [10, 20, 30, 40, 50]

print("Sum:", sum_list(numbers))

#Write a Python function program to reverse a string by using a for loop.
def reverse_string(string):
    reverse = ""

    for ch in string:
        reverse = ch + reverse

    return reverse

text = input("Enter a string: ")

print("Reversed String:", reverse_string(text))

