# Lesson n16 Object-Oriented Programming part2
#
#Exercise n1 Four Pillars of OOP in Action
#
# from abc import ABC, abstractmethod
#
# class Business:
#     def __init__(self, name:str, address:str, sector:str):
#         self.name = name
#         self.address = address
#         self.sector = sector
# #Abstraction
#     @abstractmethod
#     def show(self) -> None:
#         print(self.name, self.address, self.sector)
#
# #Inheritance, Encapsulation, Polymorphism
# class CoffeeShop(Business):
#     def __init__(self, name:str, address:str, sector:str, funds: float ):
#         super().__init__(name, address, sector)
#         self.__funds = funds
#     def print_funds(self):
#          print(self.__funds)
#         def add_funds(self,amount):
#             self.__funds += amount
#     def show(self):  # Override the method of the parent class
#         super().show()  # Call the parent class method
#
#
# class Pizzeria(Business):
#     def __init__(self, name:str, address:str, sector:str, funds: float ):
#         super().__init__(name, address, sector)
#         self.__funds = funds
#
#     def show(self):  # Override the method of the parent class
#         super().show()  # Call the parent class method
#
# coffe = CoffeeShop("Bar Catalano", "Via Matteotti 44", "Restoration", 5500.55)
# pizza = Pizzeria("Da Michele", "Via Garibaldi 10", "Restoration", 15000.77)
# coffe.show()
# pizza.show()
#
#Exercise n2 Coffee Shop
#
class Shop:
    def __init__(self, name:str, menu:list[dict[str, str | float]]):
        self._name = name
        self._menu = menu

    def describe_shop(self) -> str:
        return "This is a general shop"

class CoffeeShop(Shop):
    def __init__(self, name:str, menu:list[dict[str, str | float]]):
        super().__init__(name , menu)
        self.__orders: list[dict[str, str | float]] = []

    def add_order(self, item_name: str) -> str:
        for item in self._menu:
            if item["name"] == item_name:
                self.__orders.append(item)
                return "Order added!"
        return "This item is currently unavailable!"


    def fulfill_order(self):
        if self.__orders:
            item = self.__orders.pop(0)
            return f"The {item["name"]} is ready!"
        return "All orders have been fulfilled!"

    def list_orders(self) -> list[str]:
        return [item["name"] for item in self.__orders]

    def due_amount(self) -> float:
        return round(sum(item["price"] for item in self.__orders),2)

    def cheapest_item(self) -> str:
        return min(self._menu, key=lambda x: x["price"])["name"]

    def drinks_only(self) -> list[str]:
        return [item["name"] for item in self._menu if item["type"] == "drink"]

    def food_only(self) -> list[str]:
        return [item["name"] for item in self._menu if item["type"] == "food"]

    def describe_shop(self) -> str:
        return f"Welcome to {self._name}, serving the best coffee!"

menu = [
    {"name": "lemonade", "type": "drink", "price": 1.50},
    {"name": "cinnamon roll", "type": "food", "price": 2.00},
    {"name": "iced coffee", "type": "drink", "price": 2.50},
]

tcs = CoffeeShop("Tesha's Coffee Shop", menu)
print(tcs.describe_shop())  # Welcome to Tesha's Coffee Shop, serving the best coffee!

print(tcs.add_order("cinnamon roll"))  # Order added!
print(tcs.add_order("iced tea"))  # This item is currently unavailable!
print(tcs.add_order("iced coffee"))  # Order added!

print(tcs.list_orders())  # ['cinnamon roll', 'iced coffee']
print(tcs.due_amount())  # 4.5

# Fulfill orders (FIFO)
print(tcs.fulfill_order())  # The cinnamon roll is ready!
print(tcs.fulfill_order())  # The iced coffee is ready!
print(tcs.fulfill_order())  # All orders have been fulfilled!

print(tcs.list_orders())  # []
print(tcs.due_amount())  # 0

# Additional functionalities
print(tcs.cheapest_item())  # lemonade
print(tcs.drinks_only())  # ['lemonade', 'iced coffee']
print(tcs.food_only())  # ['cinnamon roll']