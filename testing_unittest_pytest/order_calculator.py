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


# Other tests here

def test_add_one_item():
    # Setup object
    order_calculator = OrderCalculator()
    # Each item is a tuple of name, price, and quantity
    item = ("Apples", 2, 4)
    # Execute main method to test
    order_calculator.add_item(item)
    # Test the functionality
    assert order_calculator.get_items() == [item]


def test_add_multiple_items():
    order_calculator = OrderCalculator()

    item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)

    order_calculator.add_item(item1)
    order_calculator.add_item(item2)
    order_calculator.add_item(item3)

    assert order_calculator.get_items() == [item1, item2, item3]


def test_calculate_subtotal_one_item():
    # Setup object
    order_calculator = OrderCalculator()
    item = ("Apples", 2, 4)
    order_calculator.add_item(item)
    # Execute main method to test
    res = order_calculator.calculate_subtotal()
    # Execute main method to test and test the functionality
    assert res == 8


def test_calculate_subtotal_multiple_items():
    order_calculator = OrderCalculator()

    item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)

    order_calculator.add_item(item1)
    order_calculator.add_item(item2)
    order_calculator.add_item(item3)

    res = order_calculator.calculate_subtotal()

    assert res == 16.7


def test_add_item_raises_error_if_item_less_than_len_3():
    order_calculator = OrderCalculator()
    item = ("Apples", 2)

    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_add_item_raises_error_if_none_first_in_item():
    order_calculator = OrderCalculator()

    item = (None, 2, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_add_item_raises_error_if_none_second_in_item():
    order_calculator = OrderCalculator()

    item = ("Apples", None, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)


def test_add_item_raises_error_if_none_third_in_item():
    order_calculator = OrderCalculator()

    item = ("Apples", 2, None)
    # Execute main method to test
    with pytest.raises(ValueError):
        order_calculator.add_item(item)

def test_apply_discount():
    order_calculator = OrderCalculator()
    order_calculator.set_discount(0.10)
    assert order_calculator._discount == 0.10

def test_discount_over1():
    order_calculator = OrderCalculator()

    with pytest.raises(ValueError):
        order_calculator.set_discount(1.1)

def test_discount_less0():
    order_calculator = OrderCalculator()

    with pytest.raises(ValueError):
        order_calculator.set_discount(-0.2)

def test_apply_discount():
    order_calculator = OrderCalculator()
    item = ("Orange", 2, 4)
    order_calculator.add_item(item)
    order_calculator.set_discount(0.1)
    res = order_calculator.apply_discount()
    assert res == 7.2

def test_tot_price_taxes_less0():
    order_calculator = OrderCalculator()

    with pytest.raises(ValueError):
        order_calculator.tot_price_with_taxes(-2)

def test_tot_price_taxes_string():
    order_calculator = OrderCalculator()

    with pytest.raises(TypeError):
        order_calculator.tot_price_with_taxes("-2")

def test_tot_price_taxes_correct():
    order_calculator = OrderCalculator()
    item = ("Orange", 2, 4)
    order_calculator.add_item(item)
    res = order_calculator.tot_price_with_taxes(0.15)
    assert res == 9.2

def test_retrieve_name_multiple_items():
    order_calculator = OrderCalculator()

    item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)

    order_calculator.add_item(item1)
    order_calculator.add_item(item2)
    order_calculator.add_item(item3)

    res = order_calculator.retrieve_name()

    assert res == ["Apples", "Pears", "Oranges"]