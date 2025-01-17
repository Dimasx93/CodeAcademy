# Lesson OOP: Encapsulation & Polymorphism

#Exercise n1 Encapsulation With a Banking System

# class BankAccount:
#     def __init__(self, balance: float):
#         self._balance = balance
#
#     def deposit(self, amount:float):
#         if amount > 0:
#             self._balance += amount
#             print(f"Deposit was successful, {amount}$ has been added to your account.")
#         else:
#             print(f"You cannot deposit 0 or less, enter a valid amount.")
#
#     def withdraw(self, amount:float):
#         if 0 < amount <= self._balance:
#             self._balance -= amount
#             print(f"Withdraw was successful, {amount}$ has been removed to your account.")
#         else:
#             print(f"Invalid amount, please try again.")
#
#     def check_balance(self):
#         print(f"You have {self._balance}$ left in your account.")
#
# bank_account = BankAccount(50)
# bank_account.deposit(50)
# bank_account.withdraw(30)
# bank_account.check_balance()

#Exercise n2 Polymorphism With a Media Player System

# from abc import ABC,abstractmethod
#
#
# class MediaPlayer(ABC):
#     def __init__(self, song:str):
#         self.song = song
#
#     @abstractmethod
#     def play(self, song:str):
#         pass
#
# class AudioPlayer(MediaPlayer):
#
#     def play(self):
#         if "mp3" in self.song:
#             print(f"Playing audio file: {self.song}")
#         else:
#             print("Invalid format.")
#
# class VideoPlayer(MediaPlayer):
#
#     def play(self):
#         if "mp4" in self.song:
#             print(f"Playing video file: {self.song}")
#         else:
#             print("Invalid format.")
#
# audio = AudioPlayer("song.mp3")
# video = VideoPlayer("video.mp4")
#
# media_players = [audio, video]
# for player in media_players:
#     player.play()

#Exercise n3 NASA Report

# class SpaceCraft:
#     def __init__(self,age, cost, year_built, weight):
#         self.age = age
#         self.cost = cost
#         self.year_built = year_built
#         self.weight = weight
#
#     def display_info(self):
#         return (
#             f"Spacecraft Info - Age: {self.age} years, Cost: ${self.cost}, Year Built: "
#             f"{self.year_built}, Weight: {self.weight}kg"
#         )
#
# class SpaceShuttle(SpaceCraft):
#     FUEL_COST = 0.8
#     BURN_RATE = 1.6
#     def __init__(self, age, cost, year_built, weight, orbit_height, number_of_people, base_salary):
#         super().__init__(age, cost, year_built, weight)
#         self.orbit_height = orbit_height
#         self.number_of_people = number_of_people
#         self.base_salary = base_salary
#
#     def calculate_costs(self):
#         burn_rate_var = (2500/self.orbit_height)
#         fuel_cost = self.FUEL_COST * self.BURN_RATE * burn_rate_var
#         avg_personnel_exp = self.number_of_people * self.base_salary
#         return  fuel_cost + avg_personnel_exp
#
#     def get_full_report(self):
#         info = self.display_info()
#         mission_cost = self.calculate_costs()
#         report = (
#             f"{info}\n"
#             f"Orbit Height: {self.orbit_height} miles\n"
#             f"Number of Personnel: {self.number_of_people}\n"
#             f"Base Salary per Person: ${self.base_salary}\n"
#             f"Total Mission Cost: ${mission_cost:.2f}\n"
#         )
#         return report
#
# space_shuttle = SpaceShuttle(5, 100000, 2020, 50000, 13000, 150, 6000)
# print(space_shuttle.get_full_report())

#Exercise n4 Cafeteria Project


class TableReservations:
    def __init__(self, num_tables:int):
        self.tables = ["available"] * num_tables


    def reservation(self, customer: str):
        try:
            table_idx = self.tables.index("available")
            self.tables[table_idx] = customer
            print(f"Table {table_idx + 1} reserved for {customer}.")
        except ValueError:
            print("No tables available for reservation.")

    def get_status(self):
        print("\nTable Status:")
        for idx, table in enumerate(self.tables, start=1):
            status = "Available" if table == "available" else f"Reserved for {table}"
            print(f"Table {idx}: {status}")

class Menu:
    def __init__(self, menu_name):
        self.menu_items = []
        self.menu_name = menu_name

    def add_item(self,name:str, weight:int, time:int, calories:int, price:float):
        menu_item = MenuItem(name, weight, time, calories, price)
        self.menu_items.append(menu_item)

    def print_menu(self):
        print(f"{self.menu_name}")
        for item in self.menu_items:
            print(item)


class MenuItem:
    def __init__(self,name:str, weight:int, time:int, calories:int, price:float):
        self.name = name
        self.weight = weight
        self.time = time
        self.calories = calories
        self.price = price

    def __str__(self):
        return f"{self.name}: Weights: {self.weight}, Time: {self.time}, Calories: {self.calories}, Price: {self.price}."

class Order:
    def __init__(self):
        self.items = []

    @staticmethod
    def find_item_in_menu(list_of_menus, item_name):
        for menu in list_of_menus:
            for item in menu.menu_items:
                if item_name == item.name:
                    return item

    def add_item(self, item:MenuItem):
        if item is None:
            print("This item is not available.")
        else:
            self.items.append(item)
            print(f"{item.name} added to your order.")

    def remove_item(self, item_name:str):
        for item in self.items:
            if item_name == item.name:
                self.items.remove(item)
                print(f"{item_name} was removed.")
                return
        print(f"{item_name} was not found.")

    def view_order(self):
        print("\nYour current order: ")
        for item in self.items:
            print(f"{item.name}: ${item.price}")

    def finalize_order(self):
        total_payable = sum([item.price for item in self.items])
        print(f"Total to pay: ${total_payable}")

        while True:
            try:
                tip = input("Enter tip percentage (0 for no tip): ")
                tip = float(tip)  # Convert input to a float
                if tip < 0:
                    print("Tip cannot be negative. Please enter a valid tip percentage.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for the tip.")

        tot_price = total_payable + total_payable * tip / 100
        print(f"Total to pay with tips is: ${round(tot_price, 2)}")


breakfast_menu = Menu("---BREAKFAST---")
breakfast_menu.add_item("Pancakes", 200, 10, 450, 5)


lunch_menu = Menu("---LUNCH---")
lunch_menu.add_item("Kebab Cesnakinu padazas", 300, 15, 1000, 9.5 )
lunch_menu.add_item("Vegan Salad", 150, 5, 300, 7)


dinner_menu = Menu("---DINNER---")
dinner_menu.add_item("Steak", 350, 15, 800, 20)

drinks_menu = Menu("---DRINKS---")
drinks_menu.add_item("Coke", 200, 0, 180, 2)
drinks_menu.add_item("Stalo Vandens su citrinu", 500, 0, 10, 1.5)


table_reservation = TableReservations(5)
print("\nWelcome to the Restaurant Management System")
user = input("Please enter your name for reservation check: ")
table_reservation.reservation(user)
table_reservation.get_status()

list_of_menus = [breakfast_menu, lunch_menu, dinner_menu, drinks_menu]
for item in list_of_menus:
    item.print_menu()

order = Order()

while True:
    print("\nWould you like to:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. View your order")
    print("4. Finalize your order")

    choice = input("Please enter the number of your choice (1/2/3/4): ").strip()

    if choice == "1":
        user_item = input("Choose the item to add: ")
        menu_item = Order.find_item_in_menu(list_of_menus, user_item)
        if menu_item:
            order.add_item(menu_item)
        else:
            print(f"Item '{user_item}' not found in the menu.")
    elif choice == "2":
        user_item = input("Choose the item to remove: ")
        order.remove_item(user_item)
    elif choice == "3":
        order.view_order()
    elif choice == "4":
        order.finalize_order()
        break  # Exit the loop after finalizing the order
    else:
        print("Invalid input. Please choose a valid option.")

