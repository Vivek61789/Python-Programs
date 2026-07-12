
#List is an ordered and mutable collection of items ,it can store any thye of data 
#nmbers,string,booleans,other list,all in one place

#empty iist
empty = []

#list of integers
number = [1,2,3,4,5,6,7,8,9]

#list with string
fruits = ["apple", "banana", "mango"]

# Mixed list
mixed = ["Alice", 25, True, 3.14, None]

# Nested list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# List constructor
nums = list((1, 2, 3))   # from tuple
chars = list("Python")   # from string → ['P','y','t','h','o','n']

#iterate the nested lst
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()



#list unpacking
a,b,c=[1,2,3]
print(a,b,c)

#Extended packing with *
first,*rest=[1,2,3,4,5,6,7,8]
print(first)
print(rest)

#List comprehension

#Basic
square = [x**2 for x in range(1,6)]
print(square) # [1, 4, 9, 16, 25]

#With condition
even = [x for x in range(10) if x%2==0]
print(even) # [0, 2, 4, 6, 8]

#Nested comprehension
matrix = [[i*j for j in range(1,4)] for i in range(1,4)]
print(matrix) # [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

#To find the length we use the len fun
num  = [1,2,3,4,5,6,7,8,9]
print(len(num)) #9
print(len([])) #0


