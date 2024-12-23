# Exercise 1: Christmas Gift Organizer (Object-Oriented Programming, File Handling, Exception Handling)


# class Gift:
#     def __init__(self, name:str, recipient:str, price:float):
#         self.name = name
#         self.recipient = recipient
#         self.price = price
#
#     def __str__(self):
#         return f"The present is for {self.recipient}, and is {self.name}, it costs {self.price}"
#
#     def is_expensive(self):
#         return self.price > 50
#
#
# class Giftlist:
#     def __init__(self):
#         self.giftlist = []
#
#     def print_gifts(self):
#         if not self.giftlist:
#             print("No gifts to show.")
#         else:
#             for gift in self.giftlist:
#                 print(gift)
#
#     def add_gift(self, gift:Gift):
#         try:
#             if not isinstance(gift.price, (int, float)) or gift.price < 0:
#                 raise ValueError("Price must be a positive number.")
#             if not isinstance(gift.name, str) or not isinstance(gift.recipient, str):
#                 raise ValueError("Name and recipient must be strings.")
#             self.giftlist.append(gift)
#             print("Present added.")
#             self.print_gifts()
#         except ValueError as e:
#             print(f"Error adding gift: {e}")
#
#     def remove_gift(self, gift_name: str):
#
#         for gift in self.giftlist:
#             if gift.name == gift_name:
#                 self.giftlist.remove(gift)
#         print("No more present")
#         self.print_gifts()
#
#     def save_list(self):
#         try:
#             with open("gift_list.csv", "w") as f:
#                 f.write("name, recipient, price\n")
#                 for gift in self.giftlist:
#                     f.write(f"{gift.name}, {gift.recipient}, {gift.price}\n")
#             print("Gift list saved successfully.")
#         except FileNotFoundError:
#             print("Error: The file could not be found.")
#         except PermissionError:
#             print("Error: You do not have permission to write to the file.")
#         except Exception as e:
#             print(f"An unexpected error occurred while saving the file: {e}")
#
#     def load_gifts(self, file_name:str):
#         try:
#             self.giftlist = []
#             with open(file_name, "r") as f:
#                 lines = f.readlines()
#                 for line in lines[1:]:  # Skip header
#                     name, recipient, price = line.split(",")
#                     name = name.strip()
#                     recipient = recipient.strip()
#                     try:
#                         price = float(price.strip())
#                     except ValueError:
#                         print(f"Invalid price value for {name}. Skipping gift.")
#                         continue
#                     new_gift = Gift(name, recipient, price)
#                     self.giftlist.append(new_gift)
#             self.print_gifts()
#         except FileNotFoundError:
#             print(f"Error: The file '{file_name}' could not be found.")
#         except PermissionError:
#             print("Error: You do not have permission to read the file.")
#         except Exception as e:
#             print(f"An unexpected error occurred while loading the file: {e}")
#
#
# gift = Gift("TV", "Paulius", 400)
# gift2 = Gift("Napkins", "Barack Obama", 0.5)
# gift_list = Giftlist()
#
# gift_list.add_gift(gift)
# gift_list.add_gift(gift2)
#
# gift_list.remove_gift("Napkins")
#
# gift_list.save_list()
#
# gift_list.load_gifts("gift_list.csv")

#Exercise n2 Christmas Tree Generator (Generators, Functional Programming)

# from colorama import init, Fore, Back
# init()
#
#
# def christmas_tree(height:int):
#     star = "*"
#     try:
#
#         height = int(height)
#         if height <= 0:
#             raise ValueError("Height must be a positive number!")
#         for level in range(height+1):
#             rows = star * (2 * level-1)
#             row = rows.center(2 * height - 1)
#             if level == 0:
#                 color = Fore.YELLOW
#             elif level % 2:
#                 color = Fore.RED
#             else:
#                 color = Fore.GREEN
#             print(row+color)
#     except ValueError as e:
#         print(f"Error: {e}")
#
# christmas_tree(-2)

#Exercise n3 Christmas Countdown

# import datetime
# import time
#
#
# def days_until_xmas(today):
#     xmas = datetime.datetime.strptime("2024-12-25 00:00:00","%Y-%m-%d %X")
#     difference = xmas - today
#     return difference
#
# def print_countdown():
#     countdown = days_until_xmas(today)
#     for day in range(countdown.days, 0, -1):
#         print(f"Only {day} day left until Christmas! Get ready!")
#         time.sleep(2)
#
#
#
# today = datetime.datetime.strptime("2024-12-15 00:00:00", "%Y-%m-%d %X")
# print_countdown()
