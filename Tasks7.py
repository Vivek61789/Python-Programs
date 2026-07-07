

#Write a program to create a Class and its Object in Python

class name:
    pass
name1 = name()
print("Object created")

#Write a program to create and call Method of a Class in Python

class name:
    def greet(self):
        print("Hello")
name1 = name()
name1.greet()

#Write an example program for Constructor

class name:
    def __init__(self):
        print("Constructor")

name1 = name()

#Write a Python program for Class and Object Creation
class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age 
student1 = student("luffy",33)
print(student1.name)
print(student1.age)

#Write a program for Encapsulation
class student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print("Name: ",self.name)
        print("Marks: ",self.marks)

student1 =student("Luffy",33)
student1.display()

#Create a Calculator class

class calculator:

    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b

calc = calculator()

print(calc.add(5,8))
print(calc.subtract(5,8))
print(calc.multiply(5,8))
print(calc.divide(5,8))

#Student Class

class student:
    def __init__(self,name,roll_no,marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display_details(self):
        print("name: ",self.name)
        print("Roll_no: ",self.roll_no)
        print("Marks: ",self.marks)

student1 = student("Luffy",131,99)
student2 = student("Ace",130,100)

student1.display_details()
print()

student2.display_details()

#BankAccount Class
class BankAccount:
    
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient Balance")

    def check_balance(self):
        print("Balance:", self.balance)

account = BankAccount(123456, "luffy", 10000)

account.check_balance()
account.deposit(5000)
account.withdraw(3000)
account.check_balance()

#Product Class
class Product:
    
    def __init__(self, product_name, price, discount):
        self.product_name = product_name
        self.price = price
        self.discount = discount

    def final_price(self):
        return self.price - self.discount

    def show_product(self):
        print("Product:", self.product_name)
        print("Price:", self.price)
        print("Discount:", self.discount)
        print("Final Price:", self.final_price())

product = Product("Laptop", 50000, 5000)

product.show_product()

#Book Class
class Book:
    
    def __init__(self, title, author, available_copies):
        self.title = title
        self.author = author
        self.available_copies = available_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            print("Book Borrowed")
        else:
            print("No Copies Available")

    def return_book(self):
        self.available_copies += 1
        print("Book Returned")

    def status(self):
        print("Available Copies:", self.available_copies)

book = Book("Python", "Guido", 5)

book.status()
book.borrow()
book.status()
book.return_book()
book.status()

#Car Class
class Car:
    
    def __init__(self, company, model, fuel_used, distance_travelled):
        self.company = company
        self.model = model
        self.fuel_used = fuel_used
        self.distance_travelled = distance_travelled

    def mileage(self):
        return self.distance_travelled / self.fuel_used

    def info(self):
        print("Company:", self.company)
        print("Model:", self.model)
        print("Fuel Used:", self.fuel_used)
        print("Distance Travelled:", self.distance_travelled)
        print("Mileage:", self.mileage(), "km/l")

car = Car("Toyota", "Innova", 20, 300)

car.info()
