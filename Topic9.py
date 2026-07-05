print(pow(2,9))
#usess as 2 to the power of 9 = 512

print(pow(2,10,100)) #used to find the last two digits of pow answer

#print(divmod(x,y)) used to find the remaindwer of the given values
print(divmod(2,5)) # which gives (0,2) 0 is the quotient and 2 is the remainder
x,y=divmod(2,5)
print(x,y)#it gives 2 0 

#abs() is used to find the absolute value (removes the negative value)
print(abs(-10))#10
print(abs(3.4))#3.4

#round() is used to round of the values like 3.4 is 3 and 3.7 is 4
pint(round(3.4))
print(round(3.7))

#bool()is used to print true or false of the given value
print(bool(0))     # False
print(bool(1))     # True
print(bool(""))    # False
print(bool("hi"))  # True
print(bool([]))    # False
print(bool(None))  # False

#all() is true if all the values are true
print(all([True, True, True]))    # True
print(all([True, False, True]))   # False
print(all([1, 2, 3]))             # True → all non-zero
print(all([1, 0, 3]))             # False → 0 is falsy

# Real use
marks = [75, 80, 65, 90]
print(all(m >= 35 for m in marks))  # True → all passed

#any() True if any value is true
print(any([False, False, True]))  # True
print(any([False, False, False])) # False
print(any([0, 0, 1]))             # True

# Real use
marks = [20, 80, 65, 90]
print(any(m < 35 for m in marks))  # True → someone failed

#sum() find the sum of all the numbers
#min() to find the minimum of the given values
#max() to find the maximum of the given values

#complex() is used to create the complex number 
c = complex(3, 4)
print(c)           # (3+4j)
print(c.real)      # 3.0
print(c.imag)      # 4.0

# hex() — convert int to hexadecimal
# bin() — convert int to binar
# oct() — convert int to octal

# % is used to check the given values is even,odd,lastdigit,divisibility
# // used when no decimal 
# and all condition pass
# or when any one condition is enough
# not to flip a condition 
#  is only for non check
# in to search inside seq...
# := walrus to assign inside condition or also for to use for simple one line condition 
# all() to check every thing is true
# any() to check atleat one is true

