

# Topic 7 — Lists

# ============================================================

# Task 1 — Basic
# 1. Create a list of 5 subjects and their marks
#    - Print each subject with mark using enumerate()
#    - Find total, average, highest, lowest
#    - Check if all passed (>= 35)
#    - Check if anyone failed

# 2. Take a list of 5 numbers as input
#    - Print original list
#    - Print sorted (asc and desc)
#    - Print reversed
#    - Print without duplicates

# # 1. Subjects and Marks

# subjects = ["Maths", "Science", "English", "Social", "Computer"]
# marks = [85, 72, 90, 68, 95]

# print("Subjects and Marks:")

# for i, (subject, mark) in enumerate(zip(subjects, marks), start=1):
#     print(i, subject, ":", mark)

# total = sum(marks)
# average = total / len(marks)

# print("Total:", total)
# print("Average:", average)
# print("Highest:", max(marks))
# print("Lowest:", min(marks))

# print("All Passed:", all(mark >= 35 for mark in marks))
# print("Anyone Failed:", any(mark < 35 for mark in marks))

# # 2. List Operations

# numbers = []

# for i in range(5):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# print("Original List:", numbers)

# print("Ascending Order:", sorted(numbers))
# print("Descending Order:", sorted(numbers, reverse=True))

# print("Reversed List:", numbers[::-1])

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# print("Without Duplicates:", unique)

# ========================================================================

# Task 2 — Intermediate
# 1. Take a list of 10 numbers
#    - Separate into even and odd lists
#    - Find sum of each
#    - Merge back in sorted order

# 2. Take two lists of 5 items each
#    - Find common items (intersection)
#    - Find items only in first (difference)
#    - Find all unique items (union)
#    - Zip them into a dictionary

# 3. Take a list of names
#    - Sort alphabetically
#    - Sort by length
#    - Sort by last character
#    - Reverse each name but keep list order

# # 1. List of 10 Numbers

# numbers = []

# for i in range(10):
#     num = int(input("Enter a number: "))
#     numbers.append(num)

# even = []
# odd = []

# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)

# print("Even List:", even)
# print("Odd List:", odd)

# print("Sum of Even:", sum(even))
# print("Sum of Odd:", sum(odd))

# merged = even + odd
# merged.sort()

# print("Merged Sorted List:", merged)

# # 2. Two Lists

# list1 = []
# list2 = []

# print("Enter 5 items for List 1:")
# for i in range(5):
#     list1.append(input())

# print("Enter 5 items for List 2:")
# for i in range(5):
#     list2.append(input())

# intersection = list(set(list1) & set(list2))
# difference = list(set(list1) - set(list2))
# union = list(set(list1) | set(list2))

# dictionary = dict(zip(list1, list2))

# print("Common Items:", intersection)
# print("Only in First List:", difference)
# print("All Unique Items:", union)
# print("Dictionary:", dictionary)

# # 3. List of Names

# names = []

# n = int(input("How many names? "))

# for i in range(n):
#     names.append(input("Enter name: "))

# print("Original List:", names)

# print("Alphabetical:", sorted(names))

# print("By Length:", sorted(names, key=len))

# print("By Last Character:", sorted(names, key=lambda x: x[-1]))

# print("Reverse Each Name:")

# for name in names:
#     print(name[::-1], end=" ")

# ===========================================================================

# Task 3 — Logical Thinking
# Without running, trace the output:

# nums = [1, 2, 3, 4, 5]
# nums.append(6)
# nums.insert(0, 0)
# nums.remove(3)
# print(nums)

# a = nums[::2]
# b = nums[::-1]
# print(a)
# print(b)

# x = nums.pop()
# print(x)
# print(nums)

# Write each step and the state of list
# Then verify by running

# [0, 1, 2, 4, 5, 6]
# [0, 2, 5]
# [6, 5, 4, 2, 1, 0]
# 6
# [0, 1, 2, 4, 5]

# ============================================================

# Task 4 — Problem Solving
# Build a student marks manager:
# 1. Start with empty list
# 2. Menu:
#    - Add student (name, marks)
#    - Remove student by name
#    - Search student
#    - Display all students
#    - Show topper
#    - Show failed students
#    - Sort by marks
#    - Show average of class
# 3. Keep running until user exits
# Use list of lists or list of tuples

# students = []

# while True:
#     print("\n===== Student Marks Manager =====")
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. Search Student")
#     print("4. Display All Students")
#     print("5. Show Topper")
#     print("6. Show Failed Students")
#     print("7. Sort by Marks")
#     print("8. Show Class Average")
#     print("9. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students.append([name, marks])
#         print("Student Added Successfully.")

#     elif choice == 2:
#         name = input("Enter student name to remove: ")

#         found = False

#         for student in students:
#             if student[0] == name:
#                 students.remove(student)
#                 found = True
#                 print("Student Removed.")
#                 break

#         if not found:
#             print("Student Not Found.")

#     elif choice == 3:
#         name = input("Enter student name to search: ")

#         found = False

#         for student in students:
#             if student[0] == name:
#                 print("Name:", student[0])
#                 print("Marks:", student[1])
#                 found = True
#                 break

#         if not found:
#             print("Student Not Found.")

#     elif choice == 4:
#         if len(students) == 0:
#             print("No Students Available.")
#         else:
#             print("\nStudent List")
#             for student in students:
#                 print("Name:", student[0], "Marks:", student[1])

#     elif choice == 5:
#         if len(students) == 0:
#             print("No Students Available.")
#         else:
#             topper = students[0]

#             for student in students:
#                 if student[1] > topper[1]:
#                     topper = student

#             print("Topper:", topper[0], "-", topper[1])

#     elif choice == 6:
#         if len(students) == 0:
#             print("No Students Available.")
#         else:
#             print("Failed Students:")
#             found = False

#             for student in students:
#                 if student[1] < 35:
#                     print(student[0], "-", student[1])
#                     found = True

#             if not found:
#                 print("No Failed Students.")

#     elif choice == 7:
#         if len(students) == 0:
#             print("No Students Available.")
#         else:
#             students.sort(key=lambda x: x[1], reverse=True)

#             print("Students Sorted by Marks:")
#             for student in students:
#                 print(student[0], "-", student[1])

#     elif choice == 8:
#         if len(students) == 0:
#             print("No Students Available.")
#         else:
#             total = 0

#             for student in students:
#                 total += student[1]

#             average = total / len(students)

#             print("Class Average:", average)

#     elif choice == 9:
#         print("Exiting...")
#         break

#     else:
#         print("Invalid Choice.")

# ====================================================================

# Task 5 — Advanced
# 1. Matrix operations using nested lists:
#    - Create two 3x3 matrices
#    - Add them
#    - Multiply them
#    - Transpose a matrix
#    - Find diagonal sum

# 2. Without using built-in sort:
#    - Implement Bubble Sort
#    - Implement Selection Sort
#    - Show step by step sorting process

# 3. List manipulation:
#    - Rotate list by n positions (left and right)
#    - Find second largest and second smallest
#    - Find all pairs that sum to a given number
#    - Move all zeros to end keeping order
#    - Find longest consecutive sequence

# # 1. Matrix Operations

# matrix1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# matrix2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]

# # Matrix Addition
# print("Matrix Addition:")
# result = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(matrix1[i][j] + matrix2[i][j])
#     result.append(row)

# for row in result:
#     print(row)

# # Matrix Multiplication
# print("\nMatrix Multiplication:")

# result = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         total = 0
#         for k in range(3):
#             total += matrix1[i][k] * matrix2[k][j]
#         row.append(total)
#     result.append(row)

# for row in result:
#     print(row)

# # Transpose
# print("\nTranspose of Matrix1:")

# transpose = []

# for i in range(3):
#     row = []
#     for j in range(3):
#         row.append(matrix1[j][i])
#     transpose.append(row)

# for row in transpose:
#     print(row)

# # Diagonal Sum
# diagonal = 0

# for i in range(3):
#     diagonal += matrix1[i][i]

# print("\nDiagonal Sum:", diagonal)

# # 2. Bubble Sort

# numbers = [5, 3, 8, 4, 2]

# print("Bubble Sort")

# for i in range(len(numbers)):
#     for j in range(len(numbers) - i - 1):
#         if numbers[j] > numbers[j + 1]:
#             numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

#     print("Step", i + 1, ":", numbers)


# # Selection Sort

# numbers = [5, 3, 8, 4, 2]

# print("\nSelection Sort")

# for i in range(len(numbers)):
#     minimum = i

#     for j in range(i + 1, len(numbers)):
#         if numbers[j] < numbers[minimum]:
#             minimum = j

#     numbers[i], numbers[minimum] = numbers[minimum], numbers[i]

#     print("Step", i + 1, ":", numbers)

# # 3. List Manipulation

# numbers = [1, 2, 3, 0, 5, 0, 4, 6]
# n = 2

# # Left Rotation
# print("Left Rotation:", numbers[n:] + numbers[:n])

# # Right Rotation
# print("Right Rotation:", numbers[-n:] + numbers[:-n])

# # Second Largest and Second Smallest

# unique = []

# for num in numbers:
#     if num not in unique:
#         unique.append(num)

# unique.sort()

# print("Second Smallest:", unique[1])
# print("Second Largest:", unique[-2])

# # Pairs with Given Sum

# target = int(input("Enter target sum: "))

# print("Pairs:")

# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == target:
#             print(numbers[i], numbers[j])

# # Move Zeros to End

# non_zero = []
# zero = []

# for num in numbers:
#     if num == 0:
#         zero.append(num)
#     else:
#         non_zero.append(num)

# print("Move Zeros:", non_zero + zero)

# # Longest Consecutive Sequence

# nums = list(set(numbers))
# nums.sort()

# longest = 1
# current = 1

# for i in range(1, len(nums)):
#     if nums[i] == nums[i - 1] + 1:
#         current += 1
#         longest = max(longest, current)
#     else:
#         current = 1

# print("Longest Consecutive Sequence:", longest)

# =======================================================================


