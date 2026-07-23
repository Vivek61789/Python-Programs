

#How to Add and remove elements from a set
numbers = {10, 20, 30}

numbers.add(40)
print("After adding:", numbers)

numbers.remove(20)
print("After removing:", numbers)

#Find the union of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1.union(set2))

#Find the intersection of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Intersection:", set1.intersection(set2))

#Find the difference between two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Difference:", set1.difference(set2))

#Takes two sets of integers. Finds and prints the union, intersection, and difference.
set1 = set(map(int, input("Enter first set: ").split()))
set2 = set(map(int, input("Enter second set: ").split()))

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

#Initialize a set and perform add(), remove(), and discard().
numbers = {1, 2, 3, 4, 5}

print("Original Set:", numbers)

add_num = int(input("Enter number to add: "))
numbers.add(add_num)
print("After add:", numbers)

remove_num = int(input("Enter number to remove: "))
numbers.remove(remove_num)
print("After remove:", numbers)

discard_num = int(input("Enter number to discard: "))
numbers.discard(discard_num)
print("After discard:", numbers)

#Create two frozensets and perform union & intersection.
set1 = frozenset({1, 2, 3, 4})
set2 = frozenset({3, 4, 5, 6})

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))

try:
    set1.add(10)
except AttributeError:
    print("Cannot add elements to a frozenset.")

#Store unique words from a sentence in a set.
sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words:", words)

#Create a dictionary with at least five key-value pairs and print it.
student = { "Name": "Vivek", "Age": 22, "Course": "BTech", "Branch": "CSE", "City": "Hyderabad"}

print(student)

#Access and print a value from a dictionary using its key.
student = {"Name": "Vivek","Age": 22,"Course": "BTech"}

print(student["Name"])

#Add a new key-value pair to a dictionary.
student = {
    "Name": "Vivek",
    "Age": 22
}

student["City"] = "Hyderabad"

print(student)

#Remove a key-value pair from a dictionary.
student = {
    "Name": "Vivek",
    "Age": 22,
    "City": "Hyderabad"
}

student.pop("Age")

print(student)

#Check if a key exists in a dictionary.
student = {
    "Name": "Vivek",
    "Age": 22
}

key = input("Enter key: ")

if key in student:
    print("Key exists")
else:
    print("Key does not exist")

#Iterate through a dictionary and print all keys and values.
student = {
    "Name": "Vivek",
    "Age": 22,
    "City": "Hyderabad"
}

for key, value in student.items():
    print(key, ":", value)

#Find and print the number of key-value pairs in a dictionary.
student = {
    "Name": "Vivek",
    "Age": 22,
    "City": "Hyderabad"
}

print("Number of pairs:", len(student))

#Create a nested dictionary and access a value.
students = {
    "Student1": {
        "Name": "Vivek",
        "Age": 22
    },
    "Student2": {
        "Name": "Rahul",
        "Age": 21
    }
}

print(students["Student1"]["Name"])

#Update a dictionary with another dictionary.
dict1 = {
    "Name": "Vivek",
    "Age": 22
}

dict2 = {
    "City": "Hyderabad",
    "Course": "BTech"
}

dict1.update(dict2)

print(dict1)

#Create a dictionary from two lists.
keys = ["Name", "Age", "City"]
values = ["Vivek", 22, "Hyderabad"]

dictionary = dict(zip(keys, values))

print(dictionary)

#Find the maximum and minimum values in a dictionary of numbers.
marks = {
    "Math": 85,
    "Science": 92,
    "English": 78,
    "Social": 88
}

print("Maximum:", max(marks.values()))
print("Minimum:", min(marks.values()))

