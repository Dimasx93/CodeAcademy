# Lesson Introduction to testing: Unittest Testing                       date: 12/03/2025

# Exercise n2 Testing the prime check function

# def is_prime(num: int) -> bool:
#     """Checks if a number is prime (greater than 1 and only divisible by 1 and itself)."""
#     if not isinstance(num, int):
#         raise TypeError("Input must be an integer")
#
#     if num <= 1:
#         return False
#     if num <= 3:
#         return True
#     if num % 2 == 0 or num % 3 == 0:
#         return False
#     i = 5
#     while i * i <= num:
#         if num % i == 0 or num % (i + 2) == 0:
#             return False
#         i += 6
#     return True
#
#
# import unittest
#
# class TestIsPrime(unittest.TestCase):
#     def test_negative_numbers(self):
#         self.assertFalse(is_prime(-1))
#         self.assertFalse(is_prime(-10))
#
#     def test_zero_and_one(self):
#         self.assertFalse(is_prime(0))
#         self.assertFalse(is_prime(1))
#
#     def test_small_primes(self):
#         primes = [2, 3, 5, 7, 11]
#         for num in primes:
#             self.assertTrue(is_prime(num))
#
#     def test_small_non_primes(self):
#         non_primes = [4, 6, 8, 9, 10]
#         for num in non_primes:
#             self.assertFalse(is_prime(num))
#
#     def test_large_prime(self):
#         self.assertTrue(is_prime(7919))
#
#     def test_large_non_prime(self):
#         self.assertFalse(is_prime(1001))
#
#     def test_float_input(self):
#         with self.assertRaises(TypeError):
#             is_prime(19.5)
#
#     def test_string_input(self):
#         with self.assertRaises(TypeError):
#             is_prime("23")
#
#     def test_very_large_prime(self):
#         # This might need adjustment based on practical limits of the testing environment
#         self.assertTrue(is_prime(104729))  # 10000th prime
#
#     def test_edge_case_near_square_root_boundary(self):
#         # Testing just below and above the square of 31 (which is 961)
#         self.assertTrue(is_prime(953))  # Prime just below the square
#         self.assertFalse(is_prime(962))  # Non-prime just above the square
#
# if __name__ == "__main__":
#     unittest.main()

#############################################################################################

#Exercise n3 Testing Advanced Classes Using unittest

from dataclasses import dataclass


@dataclass
class Product:
    """
    A simple Product class to store product information.
    """
    product_id: int
    name: str
    price: float


class POSSystem:
    """
    A simple Point of Sale (POS) system to manage products and sales.
    """
    def __init__(self):
        # Dictionary to store products (product_id: Product object)
        self.products = {}
        # List to hold items in the current shopping cart
        self.current_cart = []

    @classmethod
    def get_all_products(cls) -> dict:
        """
        Class method to retrieve a dictionary of all products.
        """
        # Return a copy to avoid modifying original data
        return dict(cls().products)

    def add_product(self, product_id: int, name: str, price: float) -> Product | None:
        """
        Adds a new product to the system and returns the product object.
        """
        if price < 0:
            return None
        if product_id in self.products:
            print(f"Error: Product ID {product_id} already exists.")
            return None
        self.products[product_id] = Product(product_id, name, price)
        return self.products[product_id]

    def remove_product(self, product_id: int) -> Product | None:
        """
        Removes a product from the system and returns the removed product object (or None if not found).
        """
        if product_id not in self.products:
            print(f"Error: Product ID {product_id} not found.")
            return None
        removed_product = self.products.pop(product_id)
        return removed_product

    def add_to_cart(self, product_id: int, quantity: int) -> str:
        """
        Adds a product to the current shopping cart and returns a success message (or error message).
        """
        if product_id not in self.products:
            return f"Error: Product ID {product_id} not found."
        if quantity <= 0:
            return f"Error: Invalid quantity. Please enter a positive number."
        self.current_cart.append((product_id, quantity))
        return "Product added to cart successfully."

    def remove_from_cart(self, product_id: int, quantity: int) -> str:
        """
        Removes a product from the current shopping cart and returns a success message (or error message).
        """
        if not self.current_cart:
            return "Error: Cart is empty."

        for i, (cart_id, cart_quantity) in enumerate(self.current_cart):
            if cart_id == product_id:
                if quantity > cart_quantity:
                    return f"Error: Requested quantity ({quantity}) exceeds cart quantity ({cart_quantity})"
                self.current_cart.pop(i)
                if quantity < cart_quantity:
                    self.current_cart[i] = (cart_id, cart_quantity - quantity)
                return "Product removed from cart successfully."
        return f"Error: Product ID {product_id} not found in cart."

    def view_cart(self) -> float:
        """
        Displays the items in the current shopping cart and their total price, returning the total price as a float.
        """
        if not self.current_cart:
            print("Cart is empty.")
            return 0.0

        total_price = 0
        print("Shopping Cart:")
        for product_id, quantity in self.current_cart:
            product = self.products[product_id]
            price = product.price * quantity
            total_price += price
            print(
                f"\t- {quantity}x {product.name} (${product.price:.2f}) - ${price:.2f}")
        print(f"Total: ${total_price:.2f}")
        return total_price

    def checkout(self) -> float:
        """
        Finalizes the current sale, clears the cart, and returns the total price.
        """
        if not self.current_cart:
            print("Cart is empty.")
            return 0.0
        # Call view_cart to calculate total before clearing
        total_price = self.view_cart()
        print("Checkout Successful!")
        self.current_cart = []
        return total_price

import unittest

class TestProduct(unittest.TestCase):
    def test_create_product_valid(self):
        product = Product(1, "Coffee", 2.99)
        self.assertEqual(product.product_id, 1)
        self.assertEqual(product.name, "Coffee")
        self.assertEqual(product.price, 2.99)

    def test_create_product_with_negative_price(self):
        product = Product(2, "Bagel", -1.00)
        self.assertEqual(product.price, -1.00)  # Expecting that it creates but captures logic flaw

    def test_create_product_with_string_id(self):
        product = Product("1a", "Tea", 1.50)
        self.assertEqual(product.product_id, "1a")  # Expecting that it creates but captures type error possibility

class TestPOSSystemAddProduct(unittest.TestCase):
    def setUp(self):
        self.pos = POSSystem()

    def test_add_new_product(self):
        result = self.pos.add_product(1, "Coffee", 2.99)
        self.assertIsInstance(result, Product)
        self.assertEqual(result.name, "Coffee")

    def test_add_product_existing_id(self):
        self.pos.add_product(1, "Coffee", 2.99)
        result = self.pos.add_product(1, "Tea", 1.99)
        self.assertIsNone(result)

    def test_add_product_invalid_price(self):
        result = self.pos.add_product(2, "Bagel", -1.00)
        self.assertIsNone(result)

class TestPOSSystemRemoveProduct(unittest.TestCase):
    def setUp(self):
        self.pos = POSSystem()
        self.pos.add_product(1, "Coffee", 2.99)

    def test_remove_existing_product(self):
        result = self.pos.remove_product(1)
        self.assertIsInstance(result, Product)
        self.assertEqual(result.name, "Coffee")

    def test_remove_non_existing_product(self):
        result = self.pos.remove_product(2)
        self.assertIsNone(result)

#############################################################################################

#Exercise n4

def make_chocolate(small: int, big: int, goal: int) -> int:
    max_big_use = min(big, goal // 5)
    remainder = goal - (max_big_use * 5)
    if remainder <= small:
        return remainder
    return -1


import unittest

class TestMakeChocolate(unittest.TestCase):
    def test_basic_functionality(self):
        self.assertEqual(make_chocolate(5, 2, 15), 5)

    def test_insufficient_bars(self):
        self.assertEqual(make_chocolate(3, 1, 10), -1)

    def test_excess_big_bars(self):
        self.assertEqual(make_chocolate(3, 10, 28), 3)

    def test_exact_big_bars(self):
        self.assertEqual(make_chocolate(0, 3, 15), 0)

    def test_no_big_bars_used(self):
        self.assertEqual(make_chocolate(10, 1, 3), 3)

    def test_no_small_bars_available(self):
        self.assertEqual(make_chocolate(0, 3, 14), -1)

    def test_boundary_conditions(self):
        self.assertEqual(make_chocolate(0, 0, 0), 0)

if __name__ == "__main__":
    unittest.main()