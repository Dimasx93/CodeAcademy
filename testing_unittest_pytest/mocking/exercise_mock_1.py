#Lesson Mocking                     date 18/03/2025

#Exercise mocking n1: Mocking Class Methods

import pytest
from unittest.mock import patch

from order_processor import OrderProcessor

@patch("order_processor.OrderProcessor.process_order")
def test_mock_return_50(mock_write):
    mock_write.return_value = 50.0
    order_process = OrderProcessor()
    result = order_process.process_order("apple", 25, 2)
    assert result == 50

def test_order_process():
    with patch("order_processor.OrderProcessor", autospec=True) as order_process:
        order_pr = order_process()
        order_pr.process_order.return_value = 50
        assert order_pr.process_order("apple", 25, 2) == 50

@patch("order_processor.OrderProcessor.get_processed_orders")
def test_mock_get_processed_orders(mock_write):
    mock_write.return_value = ["apple"]
    order_process = OrderProcessor()
    result = order_process.get_processed_orders()
    assert result == ["apple"]

def test_order_process_get_processed_orders():
    with patch("order_processor.OrderProcessor", autospec=True) as order_process:
        order_pr = order_process()
        order_pr.get_processed_orders.return_value = ["apple"]
        assert order_pr.get_processed_orders() == ["apple"]