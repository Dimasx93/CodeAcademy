# Lesson n15 Object-Oriented Programming
#Exercise n1 Your First Class
#
# class Shoes:
#     def __init__(self, brand:str , cost:int, distance:int):
#         self.brand = brand
#         self.cost = cost
#         self.distance = distance
#         print("New shoes created!")
#
#     def walk(self, distance:int):
#         if distance < 0:
#             print("You cannot unwalk yourself!!")
#         else:
#             self.distance += distance
#
#     def shoes_info(self):
#         return  f"You have a pair of {self.brand}, that costs {self.cost}$ and you walked {self.distance}km."
#
# shoes = Shoes("Nike", 60, 10)
# print(shoes.shoes_info())
#
#Exercise n2 A little library
#
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#
#     def get_title(self):
#         return f"Title: {self.title}."
#
#     def get_author(self):
#         return f"Author: {self.author}."
# # Testing the class
# pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen")
# hamlet = Book("Hamlet", "William Shakespeare")
# war_and_peace = Book("War and Peace", "Leo Tolstoy")
# harry_potter = Book("Harry Potter", "J.K. Rowling")
#
# print(harry_potter.title)  # Harry Potter
# print(harry_potter.author)  # J.K. Rowling
# print(harry_potter.get_title())  # Title: Harry Potter
# print(harry_potter.get_author())  # Author: J.K. Rowling
#
# print(pride_and_prejudice.get_title())  # Title: Pride and Prejudice
# print(pride_and_prejudice.get_author())  # Author: Jane Austen
#
# print(hamlet.get_title())  # Title: Hamlet
# print(hamlet.get_author())  # Author: William Shakespeare
#
# print(war_and_peace.get_title())  # Title: War and Peace
# print(war_and_peace.get_author())  # Author: Leo Tolstoy
#
#Exercise n3 New Employees
#
# class NewEmployee:
#
#     def __init__(self,  fullname="", email=""):
#         self.fullname = fullname
#         self.email = email
#
#     def get_info(self):
#         name = input("Enter your name: ")
#         surname = input("Enter your surname: ")
#         self.fullname = name + " " + surname
#         self.email = (name + "." + surname + "@company.com").lower()
#         return self.fullname, self.email
#
# new_employee = NewEmployee()
# employee_info = new_employee.get_info()
# print(employee_info)
#
#Exercise n4 Object-Oriented Calculator
#
# class Calculator:
#     def __init__(self):
#         self.result = 0
#
#     def add(self, num:int):
#         self.result += num
#
#     def divide(self, num:int):
#         if num != 0:
#             self.result /= num
#         else:
#             print("Error: Cannot divide by zero.")
#
#     def multiply(self, num:int):
#         self.result *= num
#
#     def subtract(self, num:int):
#         self.result -= num
#
#     def reset_result(self):
#         self.result = 0
#
#     def get_result(self):
#         return self.result
#
# calculator = Calculator()
# calculator.add(30)
# calculator.multiply(2)
# calculator.subtract(3)
# calculator.divide(3)
# print(calculator.get_result())
#
#Exercise n5 Comparing Countries
#
class Country:
    def __init__(self, name: str, population: int, area: float):
        self.name = name
        self.population = population
        self.area = area

    def is_big(self):
        if self.population > 20_000_000 or self.area > 3_000_000:
            return True
        else:
            return False

    def compare_pd(self, other: "Country") -> str :
        if self.name == other.name:
            print(f"{self.name} and {other.name} are the same country.")
        pd1 = self.population / self.area
        pd2 = other.population / other.area
        if pd1 > pd2:
            return f"{self.name} has a larger population density than {other.name}"
        elif pd1 < pd2:
            return f"{self.name} has a smaller population density than {other.name}"
        else:
            return f"{self.name} has a the same population density of {other.name}"

australia = Country("Australia", 23_545_500, 7_692_024)
andorra = Country("Andorra", 76_098, 468)

print(australia.is_big())  # True
print(andorra.is_big())  # False
print(australia.compare_pd(andorra))  # Andorra has a larger population density than Australia