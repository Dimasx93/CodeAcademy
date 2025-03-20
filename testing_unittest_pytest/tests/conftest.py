# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise redo POSSystem exercise(unittest exercise)

import pytest
from unittest_exercises import POSSystem,Product



@pytest.fixture
def new_pos_system() -> POSSystem:
    return POSSystem()

@pytest.fixture
def simple_product() -> Product:
    return Product(1, "Coffee", 2.99)

@pytest.fixture
def populated_pos_system(new_pos_system) -> POSSystem:
    pos = POSSystem()
    pos.add_product(1, "Coffee", 2.99)
    return pos

######################################################################################

#Exercise Order Calculator with Fixtures

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
