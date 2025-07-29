# var1 = True

# if var1:
#     print(var1)
# else:
#     print(var1)

# how to input in python
# by default input function will return string
# python2=>raw_input()->string input
#             input()-<int input

x = int(input("Enter Integer Value"))

if x < 0:
    x = 0
    """print('Negative changed to zero')"""
    if x == 0:
        print('Zero')
elif x == 1:
    print('Single')
    if x == 0:
        print('Zero')
else:
    print('More')

# Print Numbers: Write a program to print all the numbers from 1 to 20.
# Sol:
# for i in range (1,21):
#     print(i)

# "C:\Program Files\Python312\python.exe" c:/Users/mitul/Desktop/pypratice/loopqa

# user enter number 
# num = int(input("Enter till how many number to print number "))

# for i in range(1, num + 1):
#     print(i)

# Sum of a List: Given a list of numbers, write a loop to calculate their sum.

# Question 2: Calculate the sum of a list of numbers

# The list of numbers to sum up
# my_list = [1, 5, 2, 9]

# 1. Initialize a variable to store the sum. We start at 0.
# total_sum = 0

# 2. Loop through each number in the list.
# for number in my_list:
#     # 3. Add the current number to the total_sum.
#     total_sum += number  # This is shorthand for: total_sum = total_sum + number

# # 4. After the loop is finished, print the final result.
# print(f"The list is: {my_list}")
# print(f"The sum of the numbers is: {total_sum}")

# Even Numbers: Print all even numbers between 1 and 50.

# for i in range(1,51):
#     if (i%2==0):
#         print(str(i) + " is even number")

    
# String Characters: Write a program that takes a string from the user and prints each character on a new line.
# string = input("ENTER THE STRING: ")
# for char in string:
#     print(char)

# Reverse a String: Create a program that reverses a string using a loop. For example, "hello" should become "olleh".

# input_str = input("Enter string which you want to reverse: ")
# reversed_str = ""
# for char in input_str:
#     reversed_str = char + reversed_str
# print(reversed_str)

# Q- Multiplication Table: Ask the user for a number and then print the multiplication table for that number from 1 to 10.

# num = int(input("Enter the number of which u want table: "))

# for i in range(1, 11):
#     table = num * i
#     print(f"{num} * {i} = {table}")   

# Q- Factorial: Write a program to calculate the factorial of a number. For example, the factorial of 5 (written as 5!) is 5 * 4 * 3 * 2 * 1, which equals 120.

# num = int(input("Enter Number"))
# fac=1
# if num < 0:
#     print("Factorial does not exist for negative numbers")
# elif num == 0:
#     print("The factorial of 0 is 1")
# else:
#    for i in range(num, 0, -1):
#         fac = fac * i
# print(f"The factorial of {num} is {fac}")


# Count Vowels: Create a program that counts the number of vowels (a, e, i, o, u) in a given string.

# x=input("Enter the String")
# count=0
# for char in x:
#     if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#      count = count + 1



# print(f" total vowel in this string is {count}")
# ---------------------------------------------------------
# Get input from the user
# input_str = input("Enter the String: ")

# A string containing all the lowercase vowels we want to check for
# vowels = "aeiou"

# count = 0

# # Loop through each character in the user's input string
# for char in input_str:
#     # Convert the character to lowercase and check if it's in our 'vowels' string
#     if char.lower() in vowels:
#         count = count + 1 # You can also write this as count += 1

# print(f"Total vowels in this string is: {count}")

# -----------------------------------------------------------------------------------------------------

# Find the Largest Number: Given a list of numbers, use a loop to find the largest number in the list without using the built-in max() function.

# list=[5,9,2,55,33]

# largest_number=list[0]
# len=len(list)
# for number in list:
#     if number>largest_number:
#         largest_number=number


# print(f"Largest number among list is {largest_number}")
# ----------------------------------------------------------------------------------------------------------------
# Fibonacci Sequence: Write a program to generate the first 10 numbers in the Fibonacci sequence, which starts with 0 and 1. (i.e., 0, 1, 1, 2, 3, 5, 8...).

# num_of_terms = 10

# a = 0
# b = 1

# print(f"The first {num_of_terms} numbers of the Fibonacci sequence are:")

# for _ in range(num_of_terms):
#     print(a)
#     a, b = b, a + b


