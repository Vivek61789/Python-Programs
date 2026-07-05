# # Loops helps you print the code multiple times 
# #without writing it again and again

# # For loop is used for - repeat a known number of times
# #Whie loop is used for - repeat until a condition is false

# #Iterating over a string
# name = "python"
# for char in name:
#     print(char)# p y t h o n 

# vowels = 0
# for char in "Hello World":
#     if char in "aeiouAEIOU":
#         vowels += 1
# print(vowels)#3

# #iterating over a list
# fruits = ["apple" , "banana" , "mango"]
# for fruit in fruits:
#     print(fruit) # apple banana mango

# #with the index using enumerate
# for index , fruit in enumerate(fruits):
#     print(index,fruit) #0 apple 
#                         #1 banana
#                         # mango

# for index,fruit in enumerate(fruits,start=1):
#     print(index,fruit)
#     # 1 apple
#     # 2 banana
#     # 3 mango

# #iterating over a tuple
# coordinates = (10,20,30)
# for coord in coordinates:
#     print(coord) # 10n  20 30 

# #iterating over the dictionary
# person = {"name" : "luffy" , "age" : 30 , "citty" : "wanno"}

# #keys only 
# for key in person:
#     print(key)# name age city

# #values only
# for value in person.values():
#     print(value)# luffy 30 wanno

# #key and values
# for key,value in person.items():
#     print(key, ";" , value)
# # name : luffy
# # age : 30
# # city : wanno

# #iterating over a set
# colors = {"red","green","blue"}
# for color in colors:
#     print(color)#oreder was not fixed in set

# #while loop is repeats as long as condition is true

# i = 1
# while i <= 5:
#     print(i)
#     i += 1 # 1 2 3 4 5 

# #infinite loop 
# while True:
#     print("Running forever")

# #infinite loop with break
# while True:
#     name = input("Enter name(quit to exit): ")
#     if name == "quit":
#         break
#     print(f"Hello{name}")

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("loop finished")
#1 2 3 4 5
#loop finished

#loop control statements
#for loop
for i in range(5):
    if i == 5:
        break
    print(i) # 0 1 2 3 4

# while loop
while True:
    print(i)
    i += 1
    if i == 5:
        break  # 0 1 2 3 4

names = ["luffy" , "Ace" , "Sabo" , "ASC"]
search = "Ace"

for name in names:
    if name == search:
        print(f"found:{name}")
        break
else:
    print("not found")


#Continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
    # 1 3 5 7 9

numbers = [1,-2,3,-4,5]
for num in numbers:
    if num<0:
        continue
    print(num)
    # 1 3 5

# pass - do nothing

#real use to check the prime numbers
num = 17
for i in range(2,num):
    if num % i == 0:
        print("Not prime")
        break
else:
    print("prime")




              




