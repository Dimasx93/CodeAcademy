# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise Order Calculator with Fixtures

# tests/order_calculator/test_order_calculator_methods.py
from order_calculator import OrderCalculator
import pytest


def test_add_one_item_correct(new_order_calculator: OrderCalculator):
    # Each item is a tuple of name, price, and quantity
    item = ("Apples", 2, 4)
    # Execute main method to test
    new_order_calculator.add_item(item)
    # Test the functionality
    assert new_order_calculator.get_items() == [item]


def test_add_multiple_items_correct(new_order_calculator: OrderCalculator):
    item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)
    new_order_calculator.add_item(item1)
    new_order_calculator.add_item(item2)
    new_order_calculator.add_item(item3)
    assert new_order_calculator.get_items() == [item1, item2, item3]


def test_add_item_raises_error_if_item_less_than_len_3(new_order_calculator: OrderCalculator):
    new_order_calculator = OrderCalculator()
    item = ("Apples", 2)
    # Execute main method to test
    with pytest.raises(ValueError):
        new_order_calculator.add_item(item)


def test_add_item_raises_error_if_none_first_in_item(new_order_calculator: OrderCalculator):
    item = (None, 2, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        new_order_calculator.add_item(item)


def test_add_item_raises_error_if_none_second_in_item(new_order_calculator: OrderCalculator):
    item = ("Apples", None, 8)
    # Execute main method to test
    with pytest.raises(ValueError):
        new_order_calculator.add_item(item)


def test_add_item_raises_error_if_none_third_in_item(new_order_calculator: OrderCalculator):
    item = ("Apples", 2, None)
    # Execute main method to test
    with pytest.raises(ValueError):
        new_order_calculator.add_item(item)


def test_calculate_subtotal_one_item(order_calculator_with_one_item: OrderCalculator):
    res = order_calculator_with_one_item.calculate_subtotal()
    # Execute main method to test and test the functionality
    assert res == 8


def test_calculate_subtotal_multiple_items(order_calculator_with_multiple_items: OrderCalculator):
    res = order_calculator_with_multiple_items.calculate_subtotal()
    assert res == 16.7