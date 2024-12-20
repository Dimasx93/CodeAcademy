# Lesson Date and Time Operations  19/12/2024

# Exercise n1 Elementary Operations

import datetime
import time

from PIL.ImageChops import difference

# def elementary_operations():
#     today_date = datetime.datetime.now()
#     print(today_date)
#     five_days = datetime.timedelta(5)
#     new_date = today_date - five_days
#     print(new_date)
#     eight_hours = datetime.timedelta(hours=8)
#     new_date = today_date + eight_hours
#     print(new_date)
#
#     print(today_date.strftime("%Y-%m-%d, %X"))
#
# now = datetime.datetime.now()
#
# print(now)
# print(now - datetime.timedelta(days=5))
# print(now + datetime.timedelta(hours=8))
# print(now.strftime("%Y-%m-%d, %X"))
#
#
# elementary_operations()

# Exercise n2 Word Every X Seconds


# x = 0
#
# while x < 5:
#     try:
#         seconds = float(input("Enter an amount of seconds: "))
#         word = input("Enter a word: ")
#
#         if seconds < 0:
#             print("Please enter a positive number of seconds.")
#             continue
#     except ValueError:
#         print("Please enter a valid number of seconds.")
#         continue
#
#     for y in range(5):
#         time.sleep(seconds)
#         print(word)
#         x += 1

#Exercise n3 How Much Time Has Passed?
#2004-03-29 00:00:00

random_date = input("Enter a date: ")
date = datetime.datetime.strptime(random_date,"%Y-%m-%d %X")
new_date = datetime.datetime.now() - date


years = new_date.days // 365
remaining_months = new_date.days % 365

months = remaining_months // 30
days = remaining_months % 30

hours = new_date.seconds // 3600
minutes = (new_date.seconds % 3600) // 60
seconds = new_date.seconds % 60

print(f"Years: {years}")
print(f"Months: {months}")
print(f"Days: {days}")
print(f"Hours: {hours}")
print(f"Minutes: {minutes}")
print(f"Seconds: {seconds}")