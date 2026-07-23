
#1. Print numbers from 1 to 10
for i in range(1,11):
    print(i)

#2. Print even numbers from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)

#3. Multiplication table of a number
n = 5
for i in range(1,11):
    print(f"{n}X{i}={n*i}")

#4. Factorial of a number
n = 5
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

#5. Fibonacci series
n = 10
a,b = 0,1
for i in range(n):
    print(a,end="")
    a,b=b,a+b

#6. Check prime number
n =7
for i in range(2,n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")  

#7. Reverse a number
n = 123
rev = 0
while n > 0:
    rev = rev*10+n%10
    n //= 10
print(rev)

#8. Palindrome number
n = 121
temp = n
rev = 0
while n > 0:
    rev = rev*10+n%10
    n //= 10
print("Palindrome" if temp == rev else "Not Palindrome")

#9. Reverse a string
s = "Luffy"
print[::-1]

#10. Palindrome string
s = "madam"
print("Palindrome" if s == s[::-1]else"Not palindrome")

#11. Count vowels
s="Luffy"
vowels="aeioAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print(count)

#12. Count characters frequency
s = "aabbcc"
freq= ()
for ch in s:
    freq[ch]=freq.get(ch,0)+1
print(freq)

#13. Find largest number in list
a = [1,2,3,4,5,6]
print(max(a))

#14. Remove duplicates from list
a = [1,2,3,4,1,4,3,2]
print(list(set(a)))

#15. Sum of list elements
a = [1,2,3,4,5]
print(sum(a))

#16. Second largest number
a=[1,2,3,4]
a.sort()
print(a[-2])

#17. Armstrong number
n = 153
temp = n
s = 0
while temp>0:
    d = temp%10
    s +=d**3
    temp //= 10
print("Armstrong"if s==n else "Not Armstrong")

#18. GCD of two numbers
a,b=12,18
while b:
    a,b=b,a%b
print(a)

#19. Anagram check
a = "listen"
b = "slient"
print("Anagram" if sorted(a)==sorted(b)else "Not Anagram")

#20. Find common elements in two lists
a = [1,2,3,4]
b = [2,5,6,4,7,1]
print(list(set(a)&set(b)))

#21. Count words in a sentence
a = "I will become the king of pirates"
print(len(a.split()))

#22. Find missing number in array
a = [1,2,4,5,7]
n = 8
total = n*(n+1)//2
print(total-sum(a))

#23. Move zeros to end
a = [1,0,2,0,3,0]
res=[x for x in a if x !=0]+[0]*a.count(0)
print(res)

#24. Pair with given sum
lst = [1,2,3,4,5]
target = 6
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            print(lst[i], lst[j])






