"""
#1.Find the length of the string

string = input("Enter a string")
print("length of the string:" , len(string))

'''input() takes a string from the user.
len() returns the number of characters in the string.
print() displays the result.'''

"""
"""
#2. Concatenate two strings

str1 = input("enter a string1:")
str2 = input("enter a string2:")

result = str1+str2

print("Concatenated string:" , result)

'''Explanation
Two strings are taken as input.
+ operator joins the strings.
The combined string is printed.'''

"""
"""
#3.Convert string to uppercase and lowercase

str=input("Enter a string")

print("Uppercase:", str.upper())
print("Lowercase:", str.lower())

"""
"""Explanation
.upper() converts all letters to uppercase.
.lower() converts all letters to lowercase."""

"""
"""
"""
#4.Count Characters in a string

string = input("Enter a string:")

cout = len(string)

print("Length of the string:",cout)

"""
"""Explanation
len() counts all characters including spaces."""

"""
"""
"""
#5.Replace a Substring in a string

string = input("Enter a string:")
old = input("Enter a sunstring to replace:")
new = input("Enter a new substring:")

substring = string.replace(old,new)

print("New string:",substring)

"""
"""Explanation
.replace(old, new) replaces all occurrences of old with new."""

"""Enter a string: I like Python
Enter substring to replace: Python
Enter new substring: Java
Updated string: I like Java
"""

"""
"""
"""
#6.Check start and end substring

string = input("Enter a string:")
start_sub= input("Enter a starting substring:")
end_sub= input("Enter a ending substring:")

print("Starts with:",string.startswith(start_sub))
print("Ends with",string.endswith(end_sub))

'''Explanation
.startswith() checks the beginning.
.endswith() checks the ending.
Returns True or False.'''
'''Enter a string: Python Programming
Enter starting substring: Python
Enter ending substring: ming

Starts with: True
Ends with: True'''

"""
"""
#7.Count Occurrences of a specific Character

string = input("Enter a string:")
char = input("Enter a character:")
count=string.count(char)
print("Occurrences:",count)

'''Explanation
.count() counts how many times a character appears.

Example
Enter a string: banana
Enter a character: a
Occurrences: 3
'''
"""
"""
#8.Capitalize First Letter of each word

string = input("Enter a string:")
result=string.title()
print("capitalized string:",result)

'''Explanation
.title() converts the first letter of every word to uppercase.
Example
Enter a string: hello world python
Capitalized string: Hello World Python'''

"""
"""
#9.Swap case of all characters

string = input("Enter a string:")

result = string.swapcase()

print("Swappedcase:",result)

'''Explanation
.swapcase() changes:
Uppercase → Lowercase
Lowercase → Uppercase
Example
Enter a string: PyThOn
Swapped case: pYtHoN'''

"""

"""
Important String Functions for Interviews
Function	Purpose
len()	Length of string
upper()	Convert to uppercase
lower()	Convert to lowercase
replace()	Replace substring
count()	Count occurrences
startswith()	Check beginning
endswith()	Check ending
title()	Capitalize each word
swapcase()	Reverse letter cases
find()	Find position of substring
split()	Split string into list
strip()	Remove extra spaces

"""







































