
#Write a Python program to reverse a given list.
num = [10, 20, 30, 40, 50]

print("Original List:", num)

num.reverse()

print("Reversed List:", num)

#Write a Python program to find the sum of all elements in a list.
numbers = [10, 20, 30, 40, 50]

total = sum(numbers)

print("Sum of elements:", total)

#Write a Python program to find the largest element in a list.
numbers = [12, 45, 67, 23, 89, 10]

largest = max(numbers)

print("Largest element:", largest)

#Write a Python program to count the occurrences of a specified element in a list.
numbers = [10, 20, 30, 20, 40, 20, 50]

element = int(input("Enter element to count: "))

count = numbers.count(element)

print("Occurrences:", count)

#Write a Python program to remove duplicates from a list.
numbers = [10, 20, 30, 20, 40, 10, 50]

unique = list(set(numbers))

print("List after removing duplicates:", unique)

#Concatenate two tuples.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = tuple1 + tuple2

print("Concatenated Tuple:", result)

#Count the occurrences of a specific element in a tuple.
numbers = (10, 20, 30, 20, 40, 20)

element = int(input("Enter element: "))

count = numbers.count(element)

print("Occurrences:", count)

#Find the index of a specific element in a tuple.
numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

index = numbers.index(element)

print("Index:", index)

#Convert a list to a tuple.
numbers = [10, 20, 30, 40, 50]

result = tuple(numbers)

print("Tuple:", result)

#Create a tuple containing nested tuples and access elements within them.
data = (
    ("Apple", "Red"),
    ("Banana", "Yellow"),
    ("Grapes", "Green")
)

print(data)
print("First Fruit:", data[0][0])
print("Second Fruit Color:", data[1][1])
print("Third Fruit:", data[2][0])

#Check if an element exists within a tuple.
numbers = (10, 20, 30, 40, 50)

element = int(input("Enter element: "))

if element in numbers:
    print("Element exists")
else:
    print("Element does not exist")

