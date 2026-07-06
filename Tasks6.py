

#Write a program using map() to double the values in a list.
numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

#Write a program using filter() to find all the even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = list(filter(lambda x: x % 2 == 0, numbers))

print(result)

#Write a program using reduce() to find the product of all elements in a list.
from functools import reduce

numbers = [1, 2, 3, 4, 5]

product = reduce(lambda x, y: x * y, numbers)

print(product)

#Write a lambda function to capitalize the first letter of each word in a given string.
text = input("Enter a string: ")

capitalize = lambda x: x.title()

print(capitalize(text))

#Write a program using map() to create a list of the lengths of each word in a list of words.
words = ["apple", "banana", "cat", "dog"]

lengths = list(map(len, words))

print(lengths)

#Write a program using filter() to find all words in a list that are longer than 3 characters.
words = ["hi", "apple", "cat", "banana", "dog"]

result = list(filter(lambda x: len(x) > 3, words))

print(result)

#Write a program using reduce() to concatenate a list of strings into a single string.
from functools import reduce

words = ["Hello", " ", "World", "!"]

result = reduce(lambda x, y: x + y, words)

print(result)

#Write a program using map() and filter() to find the squares of even numbers in a list.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squares = list(map(lambda x: x * x, even_numbers))

print(squares)
