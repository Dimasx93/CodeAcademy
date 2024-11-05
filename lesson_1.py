# #Lesson 2 Data types and operations
#
# #Exercise n1
#
# number_1 = int(input("Enter the first number: "))
# number_2 = int(input("Enter the second number: "))
# result = number_1 + number_2
# print(f"The result is {result}")
#
# # #Exercise n2
#
# temp_f = float(input("What is the temperature in Fahrenheit? "))
# temp_c = (temp_f - 32) * 5/9
# print(f"The temperature in Celsius is {temp_c}")
#
# #Exercise n3
#
# word = input("Write something: ")
# reversed_word = word[::-1]
# print(reversed_word)
#
# #Exercise n4
#
# first_name = input("What's your name? ")
# last_name = input("And your surname? ")
# formatted_name = last_name + " " + first_name
# print(f"Hello, {formatted_name}")
#
# # #Exercise n5
#
# cash_amount = float(input("Enter the principal amount: "))
# interest_rate = float(input("Enter the interest rate (%): "))
# duration = float(input("Enter the time (years): "))
# result = (cash_amount * interest_rate * duration) / 100
# print(f"The simple interest is {result}")
#
# #Exercise n6
#
# full_name = input("Enter your full name: ")
# name = full_name.split()
# print(f"Hello {name[0].upper()}, welcome!")
#
# #Lesson 3 Conditional Statements
#
# # #Exercise n1
#
# a = int(input("Enter a number: "))
# b = int(input("Enter a number: "))
#
# if a > b:
#     print(f"{a} is bigger than {b}")
# elif a == b:
#     print(f"{a} is equal to {b}")
# else:
#     print(f"{a} is smaller than {b}")
#
# # Exercise n2
#
# name = input("Enter your name: ")
# surname = input("Enter your surname: ")
# age = int(input("Enter your age: "))
# eligibility = "allowed" if age >= 21 else "not allowed"
#
# print(f"{name} {surname}, you are {eligibility} to enter the casino.")
#
# #Exercise n3
#
# number_1 = float(input("Enter the first number: "))
# symbol = input("Enter the symbol (+, -, *, /): ")
# number_2 = float(input("Enter the second number: "))
#
# if symbol == "+":
#     result = number_1 + number_2
#     print(f"The result of {number_1} {symbol} {number_2} is {result}")
# elif symbol == "-":
#     result = number_1 - number_2
#     print(f"The result of {number_1} {symbol} {number_2} is {result}")
# elif symbol == "*":
#     result = number_1 * number_2
#     print(f"The result of {number_1} {symbol} {number_2} is {result}")
# elif symbol == "/":
#     result = number_1 / number_2
#     print(f"The result of {number_1} {symbol} {number_2} is {result}")
# else:
#         print("Wrong input.")
#
# # Exercise n4
#
# membership = input("Are you a library member? (yes/no): ").lower()
#
# if membership == "yes":
#     age = int(input("Enter your age: "))
#     if age >= 12:
#         print("You can loan all books.")
#     else:
#         adult = input("Is an adult accompanying you? (yes/no): ").lower()
#         if adult == "yes":
#             print("You can loan all books.")
#         else:
#             print("You can only loan children's books.")
# else:
#     print("You cannot loan any books.")
#
# # Exercise n5
#
# from random import randint
#
# random_number = randint(1,10)
#
# is_true = True
#
# while is_true:
#     guess = int(input("Guess the number (1 - 10): "))
#     if guess == random_number:
#         print(f"Correct! The number was {random_number}.")
#         is_true = False
#     elif guess < random_number:
#         print("Too low! Try again.")
#     else:
#         print("Too high! Try again.")
#
# #Lesson 4 Loops
#
# # Exercise n1
#
# user_name = input("Enter username: ")
# pwrd = input("Enter password: ")
#
# while True:
#     new_username = input("Enter username: ")
#     new_pwrd = input("Enter password: ")
#     if new_username == user_name and new_pwrd == pwrd:
#         print(f"Login successful! Welcome, {new_username}.")
#         break
#     else:
#         print("Wrong input.")
#
# # Exercise n2
#
# number = 0
# total = 0
# while number < 10:
#     ask = int(input("Enter integer: "))
#     total += ask
#     number += 1
#     average = total / number
#     print(f"Sum: {total}, Average: {average}")
# total_sum = 0
#
# for i in range(10):
#     number = int(input(f"Enter integer {i + 1}: "))
#     total_sum += number
#
# average = total_sum / 10
# print(f"Sum: {total_sum}, Average: {average}")
#
# # Exercise n3
#
# stored_pin = "2254"
#
# for x in range(10000):
#     pin = str(x).zfill(4)
#
#     if pin == stored_pin:
#         print(f"Found PIN: {pin}")
#     else:
#         print("Wrong input.")
#
# # Exercise n4
#
# n1, n2 = 0, 1
# for i in range(10):
#     print(n1)
#     tot = n1 + n2
#     n1 = n2
#     n2 = tot
#
# # Exercise n5
#
# done = True
# numbers = []
# while done:
#     number = input("Enter a number (or 'done' to finish): ")
#     if number == "done":
#         done = False
#     else:
#         numbers.append(float(number))
#         avg = sum(numbers) / len(numbers)
# print(f"Numbers: {numbers}\nAverage: {avg}")
#
# # Lesson 5 Lists and Tuples
#
# # Exercise n1
#
# day_temperatures = (22.6, 19.1, 21.3)
# print(len(day_temperatures))
#
# # Exercise n2
#
# shopping_list = ['milk', 'eggs', 'bread', 'butter']
# print(f"{shopping_list}\n{shopping_list[0]}")
# # for x in range(len(shopping_list)):
# #     if shopping_list[x] == "bread":
# #         shopping_list[x] = "banana"
# #         print(shopping_list)
# shopping_list[shopping_list.index("bread")] = "banana"
# print(shopping_list)
# shopping_list.insert(0, "apple")
# print(shopping_list)
# shopping_list.extend(["flour", "sugar"])
# print(shopping_list)
# print(shopping_list[2:4])
#
# # Exercise n3
#
# number = int(input("Enter the triangle size: "))
# triangle = []
# for x in range(number):
#     x +=1
#     triangle.append(x)
#     print(*triangle)
#
# # Exercise n4
##FIRST WAY
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# prime_numbers = []
# for x in range(a,b + 1):
#     if x > 1:
#         for i in range(2, x):
#             if (x % i) == 0:
#                 break
#         else:
#             prime_numbers.append(x)
# print(f"Prime numbers: {prime_numbers}")
# # SECOND WAY
# start = int(input("Enter the start of the range: "))
# end = int(input("Enter the end of the range: "))
# primes = []
#
# for num in range(start, end + 1):
#     if num > 1:
#         is_prime = True
#
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 is_prime = False
#                 break
#
#         if is_prime:
#             primes.append(num)
#
# print("Prime numbers:", primes)
#from itertools import count
#
# # Exercise n5
#
# numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
# longest_sequence = 1
# current_sequence = 1
#
# for i in range(1, len(numbers)):
#     if numbers[i] == numbers[i - 1] + 1:
#         current_sequence += 1
#     # Reset if numbers are the same or sequence breaks
#     elif numbers[i] != numbers[i - 1]:
#         current_sequence = 1
#
#     longest_sequence = max(longest_sequence, current_sequence)
#
# print("The length of the longest consecutive sequence is:", longest_sequence)
#
# # Exercise n6
#
# new_set = set()
# is_true = True
# while is_true:
#     answer = input("Enter an integer (or 'done' to finish): ")
#     if answer == "done":
#         is_true = False
#     else:
#         new_set.add(int(answer))
# print(new_set)
#
# # Exercise n7
#
# from collections import Counter
#
# sentence = list(input("Enter a string: "))
#
# #First way
#
# a = (dict(Counter(sentence)))
# for char, freq in sorted(a.items()):
#     print(f"{char}: {freq}")
#
# text = input("Enter a string: ")
# frequency = {}
#
# #Second way
#
# for char in text:
#     if char in frequency:
#         frequency[char] += 1
#     else:
#         frequency[char] = 1
#
# for char, freq in sorted(frequency.items()):  # sorting to maintain consistent order
#     print(f"{char}: {freq}")