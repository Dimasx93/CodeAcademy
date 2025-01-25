#Lesson OOP Data Classes part1        21/01/2025

from dataclasses import dataclass
from typing import Optional, List


#Exercise n1 Create a Simple Coordinate Class
# @dataclass
# class GeoMarker:
#     latitude : float
#     longitude: float
#     description : str
#
# place = GeoMarker(34.0522, -118.2437, "Los Angeles")
# print(f"{place.description}: ({place.latitude}, {place.longitude})")

##########################################################################################

#Exercise n2 Managing Event Schedules

# @dataclass
# class Event:
#     event_name:str
#     start_time:str
#     duration_minutes:int
#     def end_time(self):
#         start_hour, start_minute = map(int, self.start_time.split(":"))
#         end_minute = start_minute + self.duration_minutes
#         end_hour = start_hour + end_minute // 60
#         end_minute = end_minute % 60
#         return f"{end_hour:02}:{end_minute:02}"
# event = Event("Tech Talk", "15:00", 90)
# print(event.end_time())

##########################################################################################

#Exercise n3 Inventory Management System

# @dataclass
# class Product:
#     id: int
#     name:str
#     price:float
#     quantity:int
#     description: Optional[str] = None
#     def calculate_tot_cost(self, discount:int):
#         discount = (self.quantity * self.price) * discount / 100
#         print(discount)
#         return (self.quantity * self.price) - discount
# p = Product(1, "onion", 2.5, 10)
# print(p.calculate_tot_cost(10))

##########################################################################################

#Exercise n4 Book Library

# @dataclass
# class Book:
#     title:str
#     author:str
#     publication_year:int
#     isbn:str
#
# class Library:
#     def __init__(self):
#         self.list_of_books = []
#     def add_book(self, book:Book):
#         self.list_of_books.append(book)
#     def remove_book(self, isbn:str):
#         for book in self.list_of_books:
#             if book.isbn == isbn:
#                 self.list_of_books.remove(book)
#                 print(f"The book {book.title} has been removed.")
#         print(f"The book {book.title} is not in this library.")
#     def display_books(self):
#         for book in self.list_of_books:
#             print(f"{book.title} by {book.author}, published in {book.publication_year}, ISBN: {book.isbn}")
#
#     def search_by_title(self, title:str):
#         for book in self.list_of_books:
#             if book.title == title:
#                 return book
#
#     def search_by_author(self, author):
#         for book in self.list_of_books:
#             if book.author == author:
#                 return book
#
#
# book1 = Book(
#     title="The Great Gatsby",
#     author="F. Scott Fitzgerald",
#     publication_year=1925,
#     isbn="9780141392461",
# )
# book2 = Book(
#     title="To Kill a Mockingbird",
#     author="Harper Lee",
#     publication_year=1960,
#     isbn="9780446310789",
# )
#
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
#
# library.display_books()
#
# book3 = Book(
#     title="Pride and Prejudice",
#     author="Jane Austen",
#     publication_year=1813,
#     isbn="9780486284736",
# )
# library.add_book(book3)
#
# print(library.search_by_title("To Kill a Mockingbird"))
# print(library.search_by_author("F. Scott Fitzgerald"))
#
# library.remove_book("9780446310789")
#
# library.display_books()

##########################################################################################

#Exercise n5 Advanced Traffic and Pedestrian Light Control System

@dataclass
class TrafficLight:
    street:str
    colour:str
    timer:int

    def switch(self):
        if self.colour == "red":
            self.colour = "green"
            self.timer = 60
        elif self.colour == "green":
            self.colour = "yellow"
            self.timer = 5
        elif self.colour == "yellow":
            self.colour = "red"
            self.timer = 60

    def advance_state(self):
        if self.timer >0:
            self.timer -= 1
        if self.timer == 0:
            self.switch()

@dataclass
class Pedestrians:
    street:str
    state: str

    def switch(self):
        if self.state == "walk":
            self.state = "wait"
        else:
            self.state = "walk"

@dataclass
class Intersection:
    traffic_lights  :List[TrafficLight]
    pedestrian_signals : List[Pedestrians]

    def update(self):
        for light in self.traffic_lights:
            light.advance_state()
            for signal in self.pedestrian_signals:
                if signal.street == light.street:
                    if light.colour == "red" and light.timer == 55:
                        signal.switch()

class TrafficController:
    def __init__(self, intersection):
        self.intersection = intersection

    def simulate(self, seconds):
        """Simulate the traffic and pedestrian light control system for a given
        number of seconds."""
        for _ in range(seconds):
            self.intersection.update()

    def print_status(self):
        """Print the current status of all traffic lights and pedestrian
        signals."""
        for light in self.intersection.traffic_lights:
            print(
                f"Traffic light at {light.street} is {light.colour} with {light.timer}"
                f" seconds remaining."
            )
        for signal in self.intersection.pedestrian_signals:
            print(f"Pedestrian signal at {signal.street} is {signal.state}.")

# Setting up the intersection with traffic lights and pedestrian signals
intersection = Intersection(
    traffic_lights=[
        TrafficLight("north-south", "red", 55),
        TrafficLight("east-west", "green", 45),
    ],
    pedestrian_signals=[
        Pedestrians("north-south crosswalk", "wait"),
        Pedestrians("east-west crosswalk", "walk"),
    ],
)

# Creating a controller for the simulation
controller = TrafficController(intersection)
controller.simulate(120)  # Simulate the intersection for 120 seconds
controller.print_status()  # Print the status of traffic lights and pedestrian signals