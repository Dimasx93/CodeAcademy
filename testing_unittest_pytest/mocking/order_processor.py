#Lesson Mocking                     date 18/03/2025

#Exercise mocking n1: Mocking Class Methods

class OrderProcessor:
    def __init__(self):
        self._processed_orders = []

    def get_processed_orders(self) -> list:
        return self._processed_orders

    def process_order(self, item_name: str, quantity: int, unit_price: float) -> float:
        self._processed_orders.append(item_name)
        total_price = quantity * unit_price
        return total_price