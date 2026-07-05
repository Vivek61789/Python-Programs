
# Function - Function is a reuseable block of code that performes
#             a specific task.instead of writing the same code again
#             and again , you define it once and call whenever needed

def area(radius):
    return 3.14*radius*radius

print(area(5))  #78.5
print(area(7)) #254.34

#why we use function 
#Reusability - Write once use many times
#Readability - code is easier to understand
#Modularity -  break big problems in smaller pieces
#Debugging - fix in one place , fixed everywhere
#Dry principle - Don't repeat yourself

#how it works 
def greet(name):
    message = "hello"+name
    return message
result = greet("Luffy")
print(result)

# 1. def → Python stores function in memory
# 2. greet("Alice") → Python jumps to function
# 3. name = "Alice" → argument assigned to parameter
# 4. message = "Hello Alice" → code executes
# 5. return message → sends value back
# 6. result = "Hello Alice" → returned value stored
# 7. print(result) → Hello Alice

#define and calling
def function_name(parameter):
    #code block
    return Value

#ex
def greet():
    print("Hello world")
#call
greet()
greet()

#function with parameter
def greet(name):
    print(f"Hello {name}")
greet("luffy")
greet("Ace")

#function with return
def greet(a,b):
    return a+b

result = add(5,3)
print(result)

#parameter - Variable in the function definition
#Argument - Actual value pssed when calling

def add(a,b):
    return a+b
add(5,3)

#There are 3 types of arguments in this :
# 1. Positional argument
# 2. Keyword argument
# Mix of positional and keyword
# 3. Defaut argument

#positional  - value asigined by position - order matters
def student(name,age,grade):
    print(f"{name} is {age} year old in grade {grade}")
student("Luffy",33,"S++")
student("S++","Luffy",33)#wrong order

#keyword argument - value asign by name order does not matter
def student(name,age,grade):
    print(f"{name} is {age} year old in grade{grade}")

student(age = 20,name="Luffy",grade="S++")

student("Alice", grade="A", age=20)
# positional first, then keyword
# ❌ keyword before positional is error
student(name="Alice", 20, "A")   # SyntaxError

#Default arugement - parameter has a defaut value if not passed
def greet(name,message="Hello"):
    print(f"{message}{name}")
print("Luffy")
print("Ace","Good morning")

# ❌ Wrong
def greet(message="Hello", name):   # SyntaxError
    pass

# ✅ Correct
def greet(name, message="Hello"):
    pass

# *args-Variable positional arguments-Accept ant number of positional argument as a tuple
def add(*args):
    print(args)
    return sum(args)

print(add(1,2))
print(add(1,2,3))
print(add(1,2,3,4,5,6,7,))

#with other parameters
def student(name , *subjects):
    print(f"Name:{name}")
    print(f"Subject: {subjects}")

student("Luffy","ARC","King","Kings")

# **kwargs-Variable keyword argument - Accept any number of keyword arguments as a dictionary
def display(**kwargs):
    print(kwargs)
    for key,value in kwargs.item():
        print(f"{key} : {value}")
display(name="luffy",age=33,city="Blue East")
#{'name':'luffy','age':'33','city':'East blue'}
# name:luffy
# age : 33
# city : East Blue

 #without parameters
 def student(name, age, **extra):
        print(f"Name: {name}, Age: {age}")
    print(f"Extra info: {extra}")

student("Alice", 20, city="Paris", grade="A")
# Name: Alice, Age: 20
# Extra info: {'city': 'Paris', 'grade': 'A'}

#order of parameters(important)
#def func(positional,*args,Keyword=default,**kwargs)

 def student(name,*subject,grade="S++",**extra):
    print(name,subject,grade,extra)

student("Luffy","ARC","SEA",grade="S++",city="Wanno")
# Luffy ('ARC','SEA') S++{'City':'Wanno'}

#return statement
#single return value

def square(n):
    return n*n
print(square(5))

#multiple return value
def min_max(numbers):
    return min(numbers), max(numbers)
low,high=min_max([3,1,4,1,5,9])
print(low,high)

#return none
def greet(name):
    print(f"Hello {name}")
    # No return -> returns no value
result = greet("Luffy") #Hello Luffy
print(result) #None

#Early return
def divide(a,b):
    if b == 0:
        return "Error : dividing by zero" #Early exit
    return a/b
print(divide(10,2)) #5.0
print(divide(10,0)) #Error

#Local scope - Variable creeated inside function only accessible inside
def greet():
    message = "Hello" #local variable
    print(message) #Hello

greet()
print(message) #name error not accessible otside

#Global Scope - Variable created outside function-accessible everywhere
message = "Luffy" #gloable varible

def greet():
    print(message) #accessible inside
greet() #Luffy
print(message) #Luffy






