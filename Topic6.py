

Topic 6 — Strings

==============================================================

# Task 1 — Basic
# 1. Take a string input from user
#    Print:
#    - Length
#    - Uppercase, Lowercase, Title case
#    - First and last character
#    - Reversed string
#    - Is it palindrome?

# 2. Take a sentence
#    Print:
#    - Number of words
#    - Number of vowels
#    - Number of consonants
#    - Number of spaces
#    - Number of digits

# # 1. String Operations

# text = input("Enter a string: ")

# print("Length:", len(text))
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())
# print("Title Case:", text.title())
# print("First Character:", text[0])
# print("Last Character:", text[-1])
# print("Reversed String:", text[::-1])

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


# # 2. Sentence Operations

# sentence = input("Enter a sentence: ")

# words = len(sentence.split())

# vowels = 0
# consonants = 0
# spaces = 0
# digits = 0

# for ch in sentence:
#     if ch.lower() in "aeiou":
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch == " ":
#         spaces += 1
#     elif ch.isdigit():
#         digits += 1

# print("Number of Words:", words)
# print("Number of Vowels:", vowels)
# print("Number of Consonants:", consonants)
# print("Number of Spaces:", spaces)
# print("Number of Digits:", digits)

# ==========================================================================

# Task 2 — Intermediate
# 1. Take a string and a character as input
#    Print:
#    - How many times character appears
#    - All positions (index) where it appears
#    - Replace that character with *

# 2. Take a sentence
#    - Remove all extra spaces
#    - Capitalize first letter of each word
#    - Reverse each word but keep order
#    - Check if it starts and ends with same letter

# 3. Take a string
#    - Check if it is a valid email
#      (must have @, must have ., @ before .)
#    - Check if it is a valid phone number
#      (must be 10 digits, only numbers)

# # 1. Take a string and a character as input

# text = input("Enter a string: ")
# ch = input("Enter a character: ")

# count = text.count(ch)
# print("Occurrences:", count)

# print("Positions:", end=" ")
# for i in range(len(text)):
#     if text[i] == ch:
#         print(i, end=" ")

# print()

# print("Replaced String:", text.replace(ch, "*"))


# # 2. Take a sentence

# sentence = input("\nEnter a sentence: ")

# # Remove extra spaces
# sentence = " ".join(sentence.split())
# print("Without Extra Spaces:", sentence)

# # Capitalize first letter of each word
# print("Title Case:", sentence.title())

# # Reverse each word but keep order
# words = sentence.split()

# print("Reverse Each Word:", end=" ")
# for word in words:
#     print(word[::-1], end=" ")
# print()

# # Check if starts and ends with same letter
# if sentence[0].lower() == sentence[-1].lower():
#     print("Starts and ends with same letter")
# else:
#     print("Starts and ends with different letters")


# # 3. Email and Phone Validation

# text = input("\nEnter email or phone number: ")

# # Email Validation
# if "@" in text and "." in text and text.index("@") < text.rindex("."):
#     print("Valid Email")
# else:
#     print("Invalid Email")

# # Phone Validation
# if text.isdigit() and len(text) == 10:
#     print("Valid Phone Number")
# else:
#     print("Invalid Phone Number")

#========================================================================

# Task 3 — Logical Thinking
# Without running, find the output:

# s = "Hello World"

# print(s[::2])
# print(s[::-1])
# print(s[2:8:2])
# print(s.split()[0][::-1])
# print(s.replace("l","L").lower())

# Write output of each line step by step
# Then verify by running

# HloWrd
# dlroW olleH
# loW
# olleH
# hello world

# ==================================================================

# Task 4 — Problem Solving
# Build a string analyzer:
# Take any sentence as input and print:

# 1. Total characters (with and without spaces)
# 2. Word count
# 3. Most frequent character
# 4. Least frequent character
# 5. All unique characters
# 6. All duplicate characters
# 7. Longest word
# 8. Shortest word
# 9. Sorted words (alphabetically)
# 10. Is the sentence a pangram?
#     (contains every letter a-z at least once)

# sentence = input("Enter a sentence: ")

# # 1. Total characters
# print("Total Characters (with spaces):", len(sentence))
# print("Total Characters (without spaces):", len(sentence.replace(" ", "")))

# # 2. Word count
# words = sentence.split()
# print("Word Count:", len(words))

# # 3 & 4. Most and Least Frequent Character
# freq = {}

# for ch in sentence:
#     if ch != " ":
#         freq[ch] = freq.get(ch, 0) + 1

# most = max(freq, key=freq.get)
# least = min(freq, key=freq.get)

# print("Most Frequent Character:", most)
# print("Least Frequent Character:", least)

# # 5. Unique Characters
# print("Unique Characters:", end=" ")
# for ch in freq:
#     if freq[ch] == 1:
#         print(ch, end=" ")
# print()

# # 6. Duplicate Characters
# print("Duplicate Characters:", end=" ")
# for ch in freq:
#     if freq[ch] > 1:
#         print(ch, end=" ")
# print()

# # 7. Longest Word
# longest = words[0]
# for word in words:
#     if len(word) > len(longest):
#         longest = word
# print("Longest Word:", longest)

# # 8. Shortest Word
# shortest = words[0]
# for word in words:
#     if len(word) < len(shortest):
#         shortest = word
# print("Shortest Word:", shortest)

# # 9. Sorted Words
# sorted_words = sorted(words)
# print("Sorted Words:", sorted_words)

# # 10. Pangram Check
# letters = set()

# for ch in sentence.lower():
#     if ch.isalpha():
#         letters.add(ch)

# if len(letters) == 26:
#     print("The sentence is a Pangram")
# else:
#     print("The sentence is Not a Pangram")

# ================================================================

# Task 5 — Advanced
# 1. Caesar Cipher:
#    - Encrypt a message by shifting each letter
#      by a given number
#    - Decrypt it back
#    - Use ord() and chr()

# 2. String Compression:
#    - "aaabbbccdd" → "a3b3c2d2"
#    - If compressed is longer, return original
#    - Handle uppercase and lowercase separately

# 3. Anagram checker:
#    - Take two strings
#    - Check if they are anagrams
#    - Ignore spaces and case
#    - Example: "listen" and "silent" → True

# 4. Word frequency counter:
#    - Take a paragraph as input
#    - Count frequency of each word
#    - Sort by frequency (highest first)
#    - Print top 5 most frequent words
#    - Ignore punctuation and case

# # 1. Caesar Cipher

# message = input("Enter a message: ")
# shift = int(input("Enter shift value: "))

# encrypted = ""

# for ch in message:
#     if ch.isalpha():
#         if ch.islower():
#             encrypted += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
#         else:
#             encrypted += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
#     else:
#         encrypted += ch

# print("Encrypted:", encrypted)

# decrypted = ""

# for ch in encrypted:
#     if ch.isalpha():
#         if ch.islower():
#             decrypted += chr((ord(ch) - ord('a') - shift) % 26 + ord('a'))
#         else:
#             decrypted += chr((ord(ch) - ord('A') - shift) % 26 + ord('A'))
#     else:
#         decrypted += ch

# print("Decrypted:", decrypted)

# # 2. String Compression

# text = input("Enter a string: ")

# compressed = ""
# count = 1

# for i in range(len(text)):
#     if i < len(text) - 1 and text[i] == text[i + 1]:
#         count += 1
#     else:
#         compressed += text[i] + str(count)
#         count = 1

# if len(compressed) < len(text):
#     print("Compressed:", compressed)
# else:
#     print("Original:", text)

# # 3. Anagram Checker

# str1 = input("Enter first string: ").replace(" ", "").lower()
# str2 = input("Enter second string: ").replace(" ", "").lower()

# if sorted(str1) == sorted(str2):
#     print("True")
# else:
#     print("False")

# # 4. Word Frequency Counter

# paragraph = input("Enter a paragraph: ").lower()

# for ch in ".,!?;:-()[]{}\"'":
#     paragraph = paragraph.replace(ch, "")

# words = paragraph.split()

# frequency = {}

# for word in words:
#     frequency[word] = frequency.get(word, 0) + 1

# sorted_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

# print("Top 5 Most Frequent Words:")

# for word, count in sorted_words[:5]:
#     print(word, ":", count)

# =================================================================
