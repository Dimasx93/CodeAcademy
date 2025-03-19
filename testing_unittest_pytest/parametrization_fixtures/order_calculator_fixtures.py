# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise Order Calculator with Fixtures

import pytest
from order_calculator import OrderCalculator


@pytest.fixture
def new_order_calculator() -> OrderCalculator:
    return OrderCalculator()


@pytest.fixture
def order_calculator_with_one_item() -> OrderCalculator:
    calc = OrderCalculator()
    item1 = ("Apples", 2, 4)
    calc.add_item(item1)
    return calc


@pytest.fixture
def order_calculator_with_multiple_items() -> OrderCalculator:
    calc = OrderCalculator()
    item1 = ("Apples", 2, 4)
    item2 = ("Pears", 2.5, 3)
    item3 = ("Oranges", 1.2, 1)
    calc.add_item(item1)
    calc.add_item(item2)
    calc.add_item(item3)
    return calc
