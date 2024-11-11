# Lesson 8 - Functions

#Exercise n1 BMI Calculator
#
#from itertools import count

# height = float(input("Enter height in meters: "))
# weight = float(input("Enter weight in kilograms: "))
#
# def calculate_bmi(height,weight):
#     return weight/height**2
#
# print(f"{round(calculate_bmi(height,weight),2)}")

# #Exercise n2 Email Validator
#
# import re
#
# def email_validator(email):
#         if email.count("@") != 1:
#             return False
#         if ".." in email:
#             return False
#         username, domain = email.split("@")
#         if len(username) == 0 or len(username) > 64:
#             return False
#         if username.startswith(".") or username.endswith("."):
#             return False
#         # Username should start with a letter (a-z, A-Z) and only contain valid characters.
#         if not re.match(r"^[A-Za-z][A-Za-z0-9!#$%&'*+/=?^_`{|}~.-]*$", username):
#             return False
#         if "." not in domain:
#             return False
#         if domain.startswith(".") or domain.endswith("."):
#             return False
#         domain_parts = domain.split(".")
#         if any(len(part) == 0 for part in domain_parts[:-1]):
#             return False
#         if len(domain_parts[-1]) < 2:
#             return False
#         # Check each part of the domain for allowed characters (only alphanumeric and hyphens)
#         # Also, hyphens cannot be at the start or end of any domain part
#         for part in domain_parts:
#             if not re.match(r"^[A-Za-z0-9-]+$", part):
#                 return False
#             if part.startswith("-") or part.endswith("-"):
#                 return False
#         if len(email) > 254:
#             return False
#         return True
#
# email = input("Enter an email address: ")
# if email_validator(email):
#     print("The email address is valid.")
# else:
#     print("The email address is invalid.")

# #Exercise n3 Compound Interest Calculator
#
# principal = float(input("Enter the principal amount ($): "))
# rate = float(input("Enter the annual interest rate (%): ")) / 100
# time = float(input("Enter the time (in years): "))
#
# def compound_interest_calculator(principal,rate,time):
#     return round(principal * (1 + rate) ** time, 2)
#
# print(f"The resulting amount after {time} years is {compound_interest_calculator(principal,rate,time)}.")

# #Exercise n4 Sorted Book List
#
# from operator import itemgetter
#
# def sorted_book_list(number_books):
#         sorted_books = []
#         for i in range(number_books):
#             book = input(f"Enter title for book {i + 1}: ")
#             author = input(f"Enter author for book {i + 1}: ")
#             new_book = {"title": book, "author": author}
#             sorted_books.append(new_book)
#         return  sorted(sorted_books, key=itemgetter('author'))
# number_books = int(input("Enter the number of books: "))
# print(f"Sorted books: {sorted_book_list(number_books)}")

# #Exercise n5 Restaurant Rating Filter
#
# def rating_filter(number_restaurant, min_rating):
#     sorted_restaurant = []
#     for i in range(number_restaurant):
#         restaurant_name = input("Enter restaurant name: ")
#         rating = float(input("Enter restaurant rating: "))
#         if rating >= min_rating:
#             new_sorted = {"name":restaurant_name}
#             sorted_restaurant.append(new_sorted["name"])
#     return sorted(sorted_restaurant)

#
# number_restaurant = int(input("Enter the number of restaurants: "))
#
# min_rating = input("Now enter the minimum restaurant rating (or leave blank): ")
# if min_rating == "":
#   min_rating = 4.0
# else:
#   min_rating = float(min_rating)
#
# result = rating_filter(number_restaurant, min_rating)
# print(f"Restaurants with a rating above {min_rating}: {result}")

# #Exercise n6 Task Scheduler
#
# import datetime
#
# def task_scheduler(number_tasks):
#     sorted_tasks = []  #
#
#     for i in range(number_tasks):
#         task_name = input("Enter task name: ")
#         task_deadline = input("Enter deadline (YYYY-MM-DD): ")
#         duration = int(input("Enter duration (days): "))
#
#         deadline = datetime.datetime.strptime(task_deadline, "%Y-%m-%d")
#         adjusted_deadline = deadline - datetime.timedelta(days=duration)
#
#         new_task = {"name": task_name, "deadline": adjusted_deadline}
#         sorted_tasks.append(new_task)
#
#     sorted_tasks = sorted(sorted_tasks, key=lambda x: x["deadline"])
#
#     task_names = [task["name"] for task in sorted_tasks]
#     return task_names
#
# number_tasks = int(input("Enter the number of tasks: "))
# print("Scheduled Tasks:", task_scheduler(number_tasks))