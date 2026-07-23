
#Write a program to demonstrate the use of arithmetic operators (+, -, *, /, %, **, //) with two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Modulus:", num1 % num2)
print("Exponent:", num1 ** num2)
print("Floor Division:", num1 // num2)

#Write a program to demonstrate the use of comparison operators (==, !=, >, <, >=, <=) with two numbers.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print(num1 == num2)
print(num1 != num2)
print(num1 > num2)
print(num1 < num2)
print(num1 >= num2)
print(num1 <= num2)

#Write a program to demonstrate the use of logical operators (and, or, not) with boolean values.
a = True
b = False

print("a and b:", a and b)
print("a or b:", a or b)
print("not a:", not a)
print("not b:", not b)

#Write a program to demonstrate the use of identity operators (is, is not) with lists.
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print(list1 is list2)
print(list1 is list3)
print(list1 is not list3)

#Write a program to demonstrate the use of membership operators (in, not in) with a list.
num = [10, 20, 30, 40, 50]

print(20 in num)
print(60 in num)
print(60 not in num)

#Write a program to demonstrate the use of + and * operators with strings.
string1 = "Hello"
string2 = "World"

print(string1 + " " + string2)
print(string1 * 3)

#Create a program to check given string is palindrome or not.
str1 = input("Enter a string: ")

if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#Write a program to print numbers from 1 to 10 using a for loop.
for i in range(1, 11):
    print(i)

#Write a program to print even numbers from 1 to 20 using a while loop.
a = 2

while i<=20:
    print(i)
    i+=2

#Write a program to find the sum of the first N natural numbers using a for loop.
a = input("Enter a string: ")

sum = 0
for i in range(1,n+1):
    sum += i

print(sum)

#Write a program to find the sum of the digits of a given number using a while loop.
number = int(input("Enter a number: "))

sum = 0

while number > 0:
    digit = number % 10
    sum += digit
    number = number // 10

print("Sum of digits:", sum)

#Write a program to print Multiplication Table using while Loop.
number = int(input("Enter a number: "))

i = 1

while i <= 10:
    print(number, "x", i, "=", number * i)
    i += 1

#Write a program to reverse a given string using a for loop.
string = input("Enter a string: ")

reverse = ""

for i in string:
    reverse = i + reverse

print("Reversed string:", reverse)

#Write a program to Display Squares of Numbers from 1 to 10.
for i in range(1, 11):
    print(i, "=", i * i)

#Write a for loop to print all prime numbers between 1 and 100.
for num in range(2, 101):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)

#Write a program to Print Numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)

#Write a program to Count the Vowels in a String.
string = input("Enter a string: ")

count = 0

for i in string:
    if i in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)

#Create a program to find greatest number from 3 nums
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number:", a)
elif b >= a and b >= c:
    print("Greatest number:", b)
else:
    print("Greatest number:", c)

#Write a program to display grade based on marks.
marks = int(input("Enter marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

#Create a program that classifies a person's age into categories (child, teenager, adult, senior).
age = int(input("Enter age: "))

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")
else:
    print("Senior")

#Create a basic calculator that performs addition, subtraction, multiplication, or division based on user choice.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter operator (+, -, *, /): ")

if choice == "+":
    print("Result:", num1 + num2)
elif choice == "-":
    print("Result:", num1 - num2)
elif choice == "*":
    print("Result:", num1 * num2)
elif choice == "/":
    print("Result:", num1 / num2)
else:
    print("Invalid operator")

#Create a program to check given string is palindrome or not.
string = input("Enter a string: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")







