# Lesson n16 Object-Oriented Programming part2

#Exercise n3 Electronics Store

from datetime import date

class ElectronicDevice:
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        password: str = "manager123",
    ):
        self._brand: str = brand
        self._price: float = price
        self._warranty_period: int = warranty_period
        self._stock: int = stock
        self._store_password: str = password
        self._discount: int = 0
        self._is_discount_applied: bool = False

    def get_details(self) -> str:
        return (
            f"Brand: {self._brand}, Price: ${self._price:.2f}, Warranty: "
            f"{self._warranty_period} years, Stock: {self._stock} units"
        )

    def purchase(self) -> None:
        if self._stock > 0:
            self._stock -= 1
            print(f"Purchase successful! Stock left: {self._stock}")
        else:
            print("This item is out of stock!")

    def restock(self, quantity: int, password: str) -> None:
        if password == self._store_password:
            self._stock += quantity
            print(f"Restocked {quantity} units. New stock: {self._stock}")
        else:
            print("Unauthorized access: incorrect password.")

    def _is_warranty_valid(self, year_of_purchase: int) -> bool:
        current_date = date.today()
        current_year = int(current_date.year)
        if year_of_purchase + self._warranty_period >= current_year:
            return True
        return False

    def return_device(self, year_of_purchase: int) -> None:
        if self._is_warranty_valid(year_of_purchase):
            self._stock += 1
            print(f"Device returned successfully! Stock updated: {self._stock}")
        else:
            print("Warranty expired. Device cannot be returned.")

    def apply_discount(self, discount: int = None) -> None:
        if self._is_discount_applied:
            print("Discount already applied.")
        else:
            if discount is None:
                discount = self._discount
            self._price = round(self._price * (1 - discount / 100), 2)
            self._is_discount_applied = True
            print(f"Discount of {discount}% applied. New price: ${self._price:.2f}")


class Laptop(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        ram: int,
        storage: int,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._ram = ram
        self._storage = storage
        self._discount = 5

    def get_details(self) -> str:
        return (
            super().get_details()
            + f", RAM: {self._ram} GB, Storage: {self._storage} GB"
        )

    def upgrade_ram(self, new_ram: int) -> None:
        if new_ram > self._ram:
            self._ram = new_ram
            print(f"RAM successfully upgraded to {self._ram} GB.")
        else:
            print("New RAM must be greater than the current RAM.")


class Smartphone(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        screen_size: float,
        battery_capacity: int,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._screen_size = screen_size
        self._battery_capacity = battery_capacity
        self._discount = 3

    def get_details(self) -> str:
        return (
            super().get_details()
            + f", Screen Size: {self._screen_size} inches, Battery: {self._battery_capacity} mAh"
        )

    def upgrade_battery(self, new_battery_capacity: int) -> None:
        if new_battery_capacity > self._battery_capacity:
            self._battery_capacity = new_battery_capacity
            print(f"Battery upgraded to {self._battery_capacity} mAh.")
        else:
            print("New battery capacity must be greater than the current capacity.")


class Television(ElectronicDevice):
    def __init__(
        self,
        brand: str,
        price: float,
        warranty_period: int,
        stock: int,
        screen_size: float,
        resolution: str,
        password: str = "manager123",
    ):
        super().__init__(brand, price, warranty_period, stock, password)
        self._screen_size = screen_size
        self._resolution = resolution
        self._discount = 10

    def get_details(self) -> str:
        return (
            super().get_details()
            + f", Screen Size: {self._screen_size} inches, Resolution: {self._resolution}"
        )

    def upgrade_resolution(self, new_resolution: str) -> None:
        if new_resolution != self._resolution:
            self._resolution = new_resolution
            print(f"Resolution upgraded to {self._resolution}.")
        else:
            print("New resolution must be different from the current one.")

laptop = Laptop(
    brand="Dell",
    price=1200.00,
    warranty_period=3,
    stock=10,
    ram=16,
    storage=512,
    password="admin123",
)

smartphone = Smartphone(
    brand="iPhone",
    price=999.99,
    warranty_period=2,
    stock=20,
    screen_size=6.1,
    battery_capacity=4000,
    password="verysafepassword",
)

television = Television(
    brand="Samsung",
    price=1500.00,
    warranty_period=5,
    stock=5,
    screen_size=55,
    resolution="4K",
)

print(laptop.get_details())
# Brand: Dell, Price: $1200.00, Warranty: 3 years, Stock: 10 units, RAM: 16 GB, Storage: 512 GB
print(smartphone.get_details())
# Brand: iPhone, Price: $999.99, Warranty: 2 years, Stock: 20 units, Screen Size: 6.1 inches, Battery: 4000 mAh
print(television.get_details())
# Brand: Samsung, Price: $1500.00, Warranty: 5 years, Stock: 5 units, Screen Size: 55 inches, Resolution: 4K

for device in [laptop, smartphone, television]:
    device.apply_discount()
# Discount of 5% applied. New price: $1140.00
# Discount of 3% applied. New price: $969.99
# Discount of 10% applied. New price: $1350.00

laptop.apply_discount(15)
# Discount already applied.

laptop.purchase()
# Purchase successful! Stock left: 9
smartphone.purchase()
# Purchase successful! Stock left: 19
television.purchase()
# Purchase successful! Stock left: 4

smartphone.return_device(2022)
# Device returned successfully! Stock updated: 20
television.return_device(2016)
# Warranty expired. Device cannot be returned.

laptop.upgrade_ram(32)
# RAM successfully upgraded to 32 GB.
television.upgrade_resolution("8K")
# Resolution upgraded to 8K.

television.restock(quantity=5, password="wrong_password")
# Unauthorized access: incorrect password.
television.restock(quantity=5, password="manager123")
# Restocked 5 units. New stock: 9