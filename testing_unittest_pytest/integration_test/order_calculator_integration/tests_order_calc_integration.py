#Lesson Integration tests

#tests order_calc_integration
import pytest
from order_calc_integration import OrderCalculator


def test_full_order_workflow():
    """Test adding items, applying discount, and calculating the final total with tax."""
    order = OrderCalculator()
    order.add_item(("Apple", 1.5, 2))  # 2 Apples at $1.5 each
    order.add_item(("Banana", 1.0, 3))  # 3 Bananas at $1.0 each

    order.set_discount(0.1)  # 10% discount
    discounted_total = order.apply_discount()

    tax_rate = 0.07  # 7% tax
    final_price = order.tot_price_with_taxes(tax_rate)

    assert round(final_price, 2) == 6.42


def test_discount_application():
    """Test applying a discount correctly affects the final price."""
    order = OrderCalculator()
    order.add_item(("Laptop", 1000, 1))
    order.add_item(("Mouse", 50, 2))

    order.set_discount(0.2)  # 20% discount
    discounted_total = order.apply_discount()

    expected_total = (1000 + (50 * 2)) * 0.8  # (1000 + 100) * 0.8
    assert round(discounted_total, 2) == round(expected_total, 2)


def test_tax_calculation():
    """Test calculating tax on the subtotal."""
    order = OrderCalculator()
    order.add_item(("Monitor", 200, 2))
    order.add_item(("Keyboard", 80, 1))

    subtotal = order.calculate_subtotal()
    tax_rate = 0.05  # 5% tax
    total_with_tax = order.tot_price_with_taxes(tax_rate)

    expected_total = subtotal * (1 + tax_rate)
    assert round(total_with_tax, 2) == round(expected_total, 2)


def test_adding_invalid_items():
    """Ensure that invalid items raise appropriate errors."""
    order = OrderCalculator()

    with pytest.raises(ValueError, match="The item consists of 3 values"):
        order.add_item(("OnlyName", 2))  # Missing quantity

    with pytest.raises(ValueError, match="There must be no None in the item!"):
        order.add_item(("Milk", None, 1))  # Price is None

    with pytest.raises(ValueError, match="There must be no None in the item!"):
        order.add_item((None, 5.0, 2))  # Name is None


def test_retrieve_names():
    """Ensure that retrieving item names returns the correct list."""
    order = OrderCalculator()
    order.add_item(("Pencil", 1.0, 3))
    order.add_item(("Notebook", 5.0, 2))
    order.add_item(("Eraser", 0.5, 4))

    names = order.retrieve_name()
    assert names == ["Pencil", "Notebook", "Eraser"]
