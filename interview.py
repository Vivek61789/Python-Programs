#print numbers from 1 to 10
for i in range(1,11):
    print(i)

#print even number from 1 to 20
for i in range(1,21):
    if i % 2 == 0:
        print(i)

#multiplication table of a number
n = 5
for i in range(1,11):
    print(f"{n} x {i} = {n*i}") 

#Factorial of number
n = 5
fact = 1
for i in range(1,n+1):
    fact*=i
    print(fact)

#Fibonacci series 

n = 10
a,b = 0,1
for _ in range(n):
    print(a,end="")
    a,b=b,a+b

#Check prime number
n = 7
for i in range(2,n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("prime")

#reverse a number
n = 123
rev = 0
while n>0:
    rev = rev*10+n%10
    n //= 10
    print(rev)

#Palindrome number
n = 121
temp = n
rev = 0
while n>0:
    rev = rev*10+n%10
    n//=10
    print("palindrome" if temp == rev else "Not palindrome")

#Reverse a string
s = "Python"
print(s[::-1])

#Palindrome string
s = "madam"
print("Palindrome" if s == s[::-1] else "Not palindrome")

#Count vowels
s = "PYTHON"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)







