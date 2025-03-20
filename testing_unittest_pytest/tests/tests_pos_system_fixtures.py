# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise redo POSSystem exercise(unittest exercise)

import pytest
from unittest_exercises import POSSystem, Product

def test_add_new_product(new_pos_system):
    """Test adding a new product to the system."""
    result = new_pos_system.add_product(2, "Tea", 1.99)
    assert isinstance(result, Product)
    assert result.name == "Tea"

def test_add_product_existing_id(populated_pos_system):
    """Test adding a product with an existing ID should fail."""
    result = populated_pos_system.add_product(1, "Green Tea", 2.50)
    assert result is None

def test_add_product_invalid_price(new_pos_system):
    """Test that adding a product with a negative price returns None."""
    result = new_pos_system.add_product(3, "Bagel", -1.00)
    assert result is None

def test_remove_existing_product(populated_pos_system):
    """Test removing an existing product from the system."""
    result = populated_pos_system.remove_product(1)
    assert isinstance(result, Product)
    assert result.name == "Coffee"

def test_remove_non_existing_product(new_pos_system):
    """Test that removing a non-existent product returns None."""
    result = new_pos_system.remove_product(99)
    assert result is None
