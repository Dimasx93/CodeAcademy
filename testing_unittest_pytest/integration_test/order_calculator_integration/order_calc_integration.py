#Lesson Integration tests

# order_calculator.py
import pytest


# order_calculator.py
class OrderCalculator:
    def __init__(self):
        self._items = []

    def get_items(self) -> list:
        """Returns the list of items in the order."""
        return self._items

    def add_item(self, item: tuple) -> None:
        """Adds an item to the order.

        The item is a tuple of form (name, price, quantity)

        Raises a ValueError if the item is not of the correct form.
        """
        if len(item) < 3:
            raise ValueError("The item consists of 3 values: name, price, and quantity")

        if None in item:
            raise ValueError("There must be no None in the item!")

        self._items.append(item)

    def calculate_subtotal(self) -> float:
        """Calculates the price of all items in the order without tax."""
        subtotal = 0
        for item in self._items:
            price = item[1]
            quantity = item[2]
            subtotal += price * quantity
        return subtotal

    def set_discount(self, value: float) -> None:
        if value > 1:
            raise ValueError("Discount cannot be higher than 1.")

        if value < 0:
            raise ValueError("Discount cannot be less than 0.")

        self._discount = value

    def apply_discount(self):
        price = self.calculate_subtotal()
        discount = price * self._discount
        return price - discount

    def tot_price_with_taxes(self, value:float):
        if value < 0:
            raise ValueError("You wish taxes were 0% :(")
        if not isinstance(value, float):
            raise TypeError("Taxes are money, so it has to be a number.")
        price = self.calculate_subtotal()
        taxes = price * value
        return price + taxes

    def retrieve_name(self) -> float:
        """Calculates the price of all items in the order without tax."""
        names = []
        for item in self._items:
            name = item[0]
            names.append(name)
        return names
