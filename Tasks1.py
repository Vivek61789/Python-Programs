
# Write a program that takes a string input from the user and prints its length.
a = input("Enter an string: ")
print("Length of the string:",len(a))

#Write a program that concatenates two strings entered by the user and prints the result.
str1 = input("Enter 1st string: ")
str2 = input("Enter 2nd string: ")
result = str1+str2
print(result)

#Write a program that converts a string entered by the user to upper case and lower case.
a = input("Enter a string: ")

print("Uppercase: ",a.upper())
print("Lowercase: ",a.lower())

#Write a program to count the character in a string entered by the user.
a = input("Enter a string: ")

result = len(a)
print("Numer of character: ", result)

#Write a program to replace a substring within a string entered by the user.
a = input("Enter a string: ")
old = input("Enter substring to replace: ")
new = input("Enter new substring: ")

result = a.replace(old,new)
print("Updated string: ",result)

#Write a program to check if a string starts with a specified substring and ends with another specified substring.
a = input("Enter a string: ")
start = input("Enter starting substring: ")
end = input("Enter ending substring: ")

print("Starts with: ",a.startswith(start))
print("Ends with: ",a.endswith(end))

#Write a program to count the number of occurrences of a specific character in a string entered by the user.
a = input("Enter a string: ")
char = input("Enter a character: ")

count = a.count(char)

print("Occurrencess: ",count)

#Write a program that capitalizes the first letter of each word in a string.
a = input("Enter aa string: ")

result = a.title()

print(result)

#Write a program that swaps the case of all characters in a string entered by the user.
a = input("Enter astring: ")

result = a.swapcase()

print("After swapping case: ",result)

