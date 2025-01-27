#Lesson OOP Data Classes part2        21/01/2025

#Exercise n1 Immutable Coordinate System

from dataclasses import dataclass, field
from typing import List

# @dataclass(frozen=True)
# class Point3D:
#     x:int
#     y:int
#     z:int
# p1 = Point3D(1, 2, 3)
# print(p1)  # Output: Point3D(x=1, y=2, z=3)
# p1.z=3

#########################################################################################

#Exercise n2 Designing a Media Library With Data Classes

# @dataclass
# class MediaItem:
#     title:str
#     creator:str
#     year_published: int
#     media_type: str = field(default="Unknown", init=False)
#
# @dataclass
# class Book(MediaItem):
#     number_of_pages : int
#     author:str = field(default=None)
#     def __post_init__(self):
#         if self.author is None:
#             self.author = self.creator
#         self.media_type = "Book"
#
# @dataclass
# class Movie(MediaItem):
#     duration:int
#     director:str = field(default=None)
#     def __post_init__(self):
#         if self.director is None:
#             self.director = self.creator
#         self.media_type = "Movie"
#
# @dataclass
# class Album(MediaItem):
#     number_of_tracks : int
#     artist: str = field(default=None)
#     def __post_init__(self):
#         if self.artist is None:
#             self.artist = self.creator
#         self.media_type = "Album"
#
# book = Book(
#     title="1984", creator="George Orwell", year_published=1949, number_of_pages=328
# )
# movie = Movie(
#     title="Inception", creator="Christopher Nolan", year_published=2010, duration=148
# )
# album = Album(
#     title="Thriller", creator="Michael Jackson", year_published=1982, number_of_tracks=9
# )
#
# print(book)
# print(movie)
# print(album)

#########################################################################################

#Exercise n3 Employee Management System

# @dataclass
# class Employee:
#     employee_id:int
#     name:str
#     age:int
#     salary:float
#     department:str
#
# @dataclass
# class Department:
#     department_id : int
#     name: str
#     employees : List[Employee]
#
#     def average_salary(self):
#             return sum(employee.salary
#                        for employee in self.employees)/ len(self.employees)
#
# @dataclass
# class EmployeeManagement:
#     departments: List[Department]
#
#     def total_salary(self):
#                 return sum(employee.salary
#                            for department in self.departments
#                     for employee in department.employees
#                 )
#
#     def get_employees_in_age_range(self, min_age:int, max_age:int):
#         return [
#             employee
#             for department in self.departments
#             for employee in department.employees
#             if min_age <= employee.age <= max_age
#         ]
#
#     def sort_employees_by_salary(self):
#         all_employees = [
#             employee
#             for department in self.departments
#             for employee in department.employees
#         ]
#         return sorted(all_employees, key=lambda x: x.salary, reverse=True)
#
#     def filter_employees_by_department(self, name:str):
#         for department in self.departments:
#             if department.name == name:
#                 return department.employees
#
#         return []
#
# # Test cases
# if __name__ == "__main__":
#     # Sample employees and departments
#     employees1 = [
#         Employee(1, "John Doe", 30, 60000, "Engineering"),
#         Employee(2, "Jane Smith", 25, 65000, "Engineering"),
#     ]
#     employees2 = [
#         Employee(3, "Alice Johnson", 35, 70000, "HR"),
#         Employee(4, "Bob Brown", 45, 80000, "HR"),
#     ]
#
#     dept1 = Department(101, "Engineering", employees1)
#     dept2 = Department(102, "HR", employees2)
#     management = EmployeeManagement([dept1, dept2])
#
#     # Testing
#     print("Total salary:", management.total_salary())
#     print("Average salary in Engineering:", dept1.average_salary())
#     print(
#         "Employees in age range 20-40:",
#         [e.name for e in management.get_employees_in_age_range(20, 40)],
#     )
#     print(
#         "Employees sorted by salary:",
#         [(e.name, e.salary) for e in management.sort_employees_by_salary()],
#     )
#     print(
#         "Employees in HR department:",
#         [e.name for e in management.filter_employees_by_department("HR")],
#     )

#########################################################################################

#Exercise n4 Flight Ticketing System

import random
from dataclasses import dataclass


@dataclass
class Aircraft:
    model: str
    economy: dict
    business: dict
    first: dict
    departure_times: list  # List of possible departure times


@dataclass
class FlightOption:
    aircraft: Aircraft
    departure_time: str
    base_price: float
    distance: float

    def calculate_final_cost(self):
        # Cost influenced by departure time and aircraft age (older models cost more)
        time_cost_multiplier = {"Morning": 1.1, "Afternoon": 1.05, "Evening": 1.0}
        base_multiplier = time_cost_multiplier[self.departure_time]
        return self.base_price * base_multiplier + 0.1 * self.distance


def create_aircrafts():
    return [
        Aircraft(
            "Airbus A330-300",
            {"count": 250, "pitch": 31, "price": 200},
            {"count": 48, "pitch": 42, "price": 750},
            {"count": 8, "pitch": 60, "price": 1300},
            ["Morning", "Afternoon", "Evening"],
        ),
        Aircraft(
            "Boeing 747-400",
            {"count": 345, "pitch": 31, "price": 195},
            {"count": 52, "pitch": 40, "price": 800},
            {"count": 10, "pitch": 62, "price": 1400},
            ["Morning", "Evening"],
        ),
        Aircraft(
            "Boeing 777-300",
            {"count": 315, "pitch": 32, "price": 210},
            {"count": 40, "pitch": 42, "price": 790},
            {"count": 12, "pitch": 61, "price": 1500},
            ["Afternoon", "Evening"],
        ),
    ]


def main():
    city_distances = {
        ("New York", "Los Angeles"): 2451,
        ("New York", "Chicago"): 790,
        ("Chicago", "Los Angeles"): 1744,
        ("Miami", "New York"): 1287,
        ("Seattle", "Miami"): 2734,
    }

    aircrafts = create_aircrafts()
    print("Available cities: New York, Los Angeles, Chicago, Miami, Seattle")
    departure = input("Enter departure city: ")
    destination = input("Enter destination city: ")

    if (departure, destination) not in city_distances:
        print("Flight route not available.")
        return

    print("\nAvailable Flights:")
    for i, aircraft in enumerate(aircrafts, start=1):
        # Randomly select a departure time
        departure_time = random.choice(aircraft.departure_times)
        print(
            f"{i}. {aircraft.model} - Departure Time: {departure_time}, Economy Price: "
            f"${aircraft.economy['price']}"
        )

    choice = int(input("Select your flight (1-3): "))
    selected_aircraft = aircrafts[choice - 1]
    selected_departure_time = random.choice(selected_aircraft.departure_times)

    flight_option = FlightOption(
        selected_aircraft,
        selected_departure_time,
        selected_aircraft.economy["price"],
        city_distances[(departure, destination)],
    )
    final_cost = flight_option.calculate_final_cost()

    print(f"\nFinal cost of your flight: ${final_cost:.2f}")


if __name__ == "__main__":
    main()
