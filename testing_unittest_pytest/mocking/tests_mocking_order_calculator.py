#Lesson Mocking                     date 18/03/2025

# tests_mocking_order_calculator.py

from unittest.mock import patch

from order_calc_mocking import OrderCalculator

def test_calculate_subtotal():
    with patch("order_calc_mocking.OrderCalculator", autospec=True) as order_calculator:
        order = order_calculator()
        order.add_item(("apple", 2 , 2))
        order.calculate_subtotal.return_value = 4
        assert order.calculate_subtotal() == 4

def test_tot_price_with_taxes():
    order = OrderCalculator()

    with patch.object(order, "calculate_subtotal", return_value=100):  # Pretend subtotal is $100
        total_with_taxes = order.tot_price_with_taxes(0.07)  # 7% tax → $107

    assert total_with_taxes == 107

def test_apply_discount():
    order = OrderCalculator()
    order.set_discount(0.1)  # 10% discount

    with patch.object(order, "calculate_subtotal", return_value=100):  # Mock subtotal to $100
        discounted_total = order.apply_discount()  # Should be 100 - (100 * 0.1) = 90

    assert discounted_total == 90
