#Lesson OOP: Abstract Clases and Methods    09/01/2025

#Exercise n1 Dog and Cat

from abc import ABC, abstractmethod



# class Animal(ABC):
#     def __init__(self, name:str):
#         self.name = name
#
#     @abstractmethod
#     def speak(self):
#         pass
#
#     def get_name(self):
#         return self.name
#
# class Dog(Animal):
#     def speak(self):
#         return f"Dog says Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return f"Cat says Meow!"
#
# dog = Dog("Pipolo")
# cat = Cat("Briciola")
# print(dog.speak())
# print(dog.get_name())
# print(cat.speak())
# print(cat.get_name())

######################################################

#Exercise n2 Refactor Shape, Rectangle, and Square

# class Shape(ABC):
#
#     def __init__(self, name: str, sides: int) -> None:
#         self.name = name
#         self.sides = sides
#
#     @abstractmethod
#     def area(self) -> float:
#         pass
#
#
# class Rectangle(Shape):
#
#     def __init__(self, width: float, height: float) -> None:
#         super().__init__("Rectangle", 4)  # Call to the abstract superclass
#         self.width = width
#         self.height = height
#
#     def area(self) -> float:
#         return self.width * self.height
#
#
# class Square(Rectangle):
#
#     def __init__(self, side_length: float) -> None:
#         super().__init__(side_length, side_length)
#         self.side_length = side_length
#
#
# square = Square(5)
# print(square.name)
# print(square.sides)
# print(square.area())

##############################################################################################

#Exercise n3 Money

# from abc import ABC, abstractmethod
# from typing import Dict
#
#
# class Money(ABC):
#     def __init__(self, currency: str, value: float):
#         self.currency = currency
#         self.value = value
#
#     def get_value(self) -> float:
#         return self.value
#
#     def get_currency(self) -> str:
#         return self.currency
#
#     @abstractmethod
#     def convert_to_currency(
#         self, target_currency: str, conversion_rate: Dict[str, float]
#     ) -> None:
#         pass
#
#
# class Cash(Money):
#     def __init__(self, currency: str, value: float, denomination: int):
#         super().__init__(currency, value)
#         self.denomination = denomination
#
#     def convert_to_currency(
#         self, target_currency: str, conversion_rate: Dict[str, float]
#     ) -> None:
#         self.value = round(
#             self.value
#             * conversion_rate[self.currency]
#             * conversion_rate[target_currency],
#             2,
#         )
#         self.currency = target_currency
#         for _ in range(int(self.value / self.denomination)):
#             self.value -= self.denomination
#
#
# class Card(Money):
#     def __init__(self, currency: str, value: float, credit_limit: float):
#         super().__init__(currency, value)
#         self.credit_limit = credit_limit
#
#     def convert_to_currency(
#         self, target_currency: str, conversion_rate: Dict[str, float]
#     ) -> None:
#         self.value = round(
#             min(self.value, self.credit_limit)
#             * conversion_rate[self.currency]
#             * conversion_rate[target_currency],
#             2,
#         )
#         self.currency = target_currency

#########################################################################################

#Exercise Building a Smart Home System



# class SmartDevice(ABC):
#     def __init__(self, location):
#         self.location = location
#         self.power_state = False
#
#     @abstractmethod
#     def turn_on(self):
#         pass
#
#     @abstractmethod
#     def turn_off(self):
#         pass
#
#     @abstractmethod
#     def status_report(self):
#         pass
#
#
# class SmartLight(SmartDevice):
#     def __init__(self, location, color="White"):
#         super().__init__(location)
#         self.color = color
#         self.brightness = 100
#
#     def turn_on(self):
#         self.power_state = True
#         print(f"Light in {self.location} turned on.")
#
#     def turn_off(self):
#         self.power_state = False
#         print(f"Light in {self.location} turned off.")
#
#     def dim(self, level):
#         self.brightness = level
#         print(f"Light in {self.location} dimmed to {self.brightness}% brightness.")
#
#     def change_color(self, color):
#         self.color = color
#         print(f"Light in {self.location} color changed to {self.color}.")
#
#     def status_report(self):
#         return (
#             f"Smart Light in {self.location} - State: "
#             f"{'On' if self.power_state else 'Off'}, Color: {self.color}, Brightness: "
#             f"{self.brightness}%"
#         )
#
#
# class SmartThermostat(SmartDevice):
#     def __init__(self, location, temperature=23):
#         super().__init__(location)
#         self.temperature = temperature
#
#     def turn_on(self):
#         self.power_state = True
#         print(f"Thermostat in {self.location} turned on.")
#
#     def turn_off(self):
#         self.power_state = False
#         print(f"Thermostat in {self.location} turned off.")
#
#     def set_temperature(self, temperature):
#         self.temperature = temperature
#         print(f"Temperature set to {self.temperature}°C in {self.location}.")
#
#     def status_report(self):
#         return (
#             f"Smart Thermostat in {self.location} - State: "
#             f"{'On' if self.power_state else 'Off'}, Temperature: {self.temperature}°F"
#         )
#
#
# class SmartSecurityCamera(SmartDevice):
#     def __init__(self, location):
#         super().__init__(location)
#         self.recording = False
#
#     def turn_on(self):
#         self.power_state = True
#         self.start_recording()
#
#     def turn_off(self):
#         self.power_state = False
#         self.stop_recording()
#
#     def start_recording(self):
#         self.recording = True
#         print(f"Camera in {self.location} started recording.")
#
#     def stop_recording(self):
#         self.recording = False
#         print(f"Camera in {self.location} stopped recording.")
#
#     def status_report(self):
#         return (
#             f"Smart Security Camera in {self.location} - State: "
#             f"{'On' if self.power_state else 'Off'}, Recording: "
#             f"{'Yes' if self.recording else 'No'}"
#         )
#
#
# class SmartHomeController:
#     def __init__(self):
#         self.devices = []
#
#     def add_device(self, device):
#         self.devices.append(device)
#
#     def all_on(self):
#         for device in self.devices:
#             device.turn_on()
#
#     def all_off(self):
#         for device in self.devices:
#             device.turn_off()
#
#     def system_report(self):
#         for device in self.devices:
#             print(device.status_report())
#
# home = SmartHomeController()
# home.add_device(SmartLight("Living Room", "Blue"))
# home.add_device(SmartThermostat("Hallway", 70))
# home.add_device(SmartSecurityCamera("Front Door"))
#
# home.all_on()
# home.system_report()
# home.all_off()
# home.system_report()

#######################################################################################################

#Exercise with Paulius


from typing import Tuple


class Database(ABC):
    @abstractmethod
    def add_user(self, user: Tuple[str, str]):
        pass

    @abstractmethod
    def delete_user(self, user_id: int):
        pass

    @abstractmethod
    def add_location(self, location: str):
        pass

    @abstractmethod
    def delete_location(self, location_id: int):
        pass


class StoreDatabase(Database):
    def __init__(self, name: str):
        self.store_name = name
        self.users = []
        self.locations = []
        self.total_users = 0
        self.id_location = 0

    def add_user(self, user: Tuple[str, str]):
        self.total_users += 1
        # Add (unique id, user) into database
        self.users.append((self.total_users, user))
        # self.users =
        # [(1, ("john", "smth")), (123, ("mary", "sue"), ...]
        print(f"{user} was added to the database.")

    def delete_user(self, user_id: int):
        for user_list_idx, user in enumerate(self.users):
            # user = (1, ("john", "smth"))
            if user[0] == user_id:
                self.users.pop(user_list_idx)
                print(f"User with id {user_id} was deleted.")
                return

        print(f"User with id {user_id} is not in the database.")

    def add_location(self, location: Tuple[str, str]):
        self.id_location += 1
        self.locations.append((self.id_location,location))
        print(f"{location} was added to the database.")


    def delete_location(self, location_id: int):
        for idx_location, location in enumerate(self.locations):
            if location[0] == location_id:
                self.locations.pop(idx_location)
                print(f"Location with id {location_id} was deleted.")
                return
        print(f"Location with id {location_id} is not in the database.")


class PropertyRentingDatabase(Database):
    def __init__(self):
        self.information = {"users": {}, "locations": {}}
        self.total_users = 0
        self.id_location = 0

    def add_user(self, user: Tuple[str, str]):
        self.total_users += 1
        self.information["users"][self.total_users] = user
        print(f"User {user} was added to the database.")
        # self.users =
        # {
        #   "users": {
        #       1: ("john", "smith"),
        #       2: ("mary", "sue")
        #   },
        #   "locations": {...}
        # }

    def delete_user(self, user_id: int):
        if user_id in self.information["users"]:
            self.information["users"].pop(user_id)
            print(f"User with id {user_id} was deleted.")
        else:
            print(f"User with id {user_id} is not in the database.")

    def add_location(self, location: Tuple[str, str]):
        self.id_location += 1
        self.information["locations"][self.id_location] = location
        print(f"{location} was added to the database.")


    def delete_location(self, location_id: int):
        if location_id in self.information["locations"]:
            self.information["locations"].pop(location_id)
            print(f"The location with {location_id} was deleted.")
        else:
            print(f"The location with {location_id} is not in the database.")

store_database = StoreDatabase("hello")
store_database.add_location(("Lentini", "A city in Italy"))
store_database.add_user(("Pino", "Daniele"))
store_database.delete_location(1)
store_database.delete_user(1)

property_db = PropertyRentingDatabase()
property_db.add_user(("Peppino", "Di Fli"))
property_db.add_location(("Augusta", "A city in Sicily"))
property_db.delete_user(1)
property_db.delete_location(1)
