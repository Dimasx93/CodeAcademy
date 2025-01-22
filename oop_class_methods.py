# Lesson OOP: Class Methods 16/01/2025


# Exercise n1 Factorial

# class MathOperation:
#     @classmethod
#     def factorial(cls,n: int) -> int:
#         if n == 0:
#             return 1
#         else:
#             return n * cls.factorial(n -1)
# print(MathOperation.factorial(5))

############################################################

# Exercise n2 Reversed String

# class ReversedString:
#     @classmethod
#     def reverse_str(cls, string:str) -> str:
#         return string[::-1]
#
# print(ReversedString.reverse_str("Hello"))

############################################################

# Exercise n3 List Prime Numbers

# class MathOperations:
#     @classmethod
#     def is_prime(cls, n: int) -> bool:
#         if n <= 1:
#             return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0:
#                 return False
#         return True
#
#     @classmethod
#     def primes(cls, n: int) -> list[int]:
#         primes_list = []
#         for i in range(2, n + 1):
#             if cls.is_prime(i):
#                 primes_list.append(i)
#         return primes_list
#
# print(MathOperations.primes(20))

############################################################

# Exercise n4 BankAccount Class

# class BankAccount:
#     def __init__(self, balance:float= 0):
#         self.balance = balance
#     def deposit(self, amount:float):
#          self.balance += amount
#
#     def withdraw(self, amount:float):
#         if self.balance < amount:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount
#
#     @classmethod
#     def from_balance(cls: type["BankAccount"], balance:float):
#         return cls(balance)
#     @staticmethod
#     def transfer(b_account:"BankAccount", b_account2:"BankAccount", amount:float):
#         if b_account.balance < amount:
#             print("Insufficient funds")
#         else:
#             b_account.withdraw(amount)
#             b_account2.deposit(amount)
# account1 = BankAccount.from_balance(100)
# account2 = BankAccount.from_balance(50)
#
# BankAccount.transfer(account2,account1, 30)
# print(account1.balance)
# print(account2.balance)

############################################################

# Exercise n5 SpaceStation Class

# from typing import Dict, List, Optional, Type
#
# class Astronaut:
#     def __init__(self, name: str, nationality: str, mission_duration: int) -> None:
#         self.name = name
#         self.nationality = nationality
#         self.mission_duration = mission_duration
#
# class SpaceStation:
#     def __init__(self, astronauts: List[Astronaut]) -> None:
#         self.astronauts = astronauts
#
#     def add_astronaut(self, name:str, nationality:str, mission_duration:int):
#         astronaut = Astronaut(name, nationality, mission_duration)
#         self.astronauts.append(astronaut)
#
#     def find_astronaut(self, name:str) -> Optional[Astronaut]:
#         for astronaut in self.astronauts:
#             if astronaut.name == name:
#                 return astronaut
#         return None
#
#     @classmethod
#     def from_astronaut_list(cls: Type["SpaceStation"],astronauts: List[Dict[str,str]]) -> "SpaceStation":
#         astronaut_obj = [Astronaut(**astronaut) for astronaut in astronauts]
#         return cls(astronaut_obj)
#
#     @staticmethod
#     def is_long_term_mission(astronaut:Astronaut) -> bool:
#         return astronaut.mission_duration > 6
#
#     def remove_astronaut(self, name:str) -> None:
#         self.astronauts = [astronaut for astronaut in self.astronauts if astronaut.name != name]

############################################################

# Exercise n6 Class to Represent a Library System
from typing import List


class Book:
    def __init__(self, title: str, author: str, isbn: str, num_copies: int):
        self.title = title
        self.author = author
        self.num_copies = num_copies
        self.isbn = isbn


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.books_borrowed: List[Book] = []


class LibrarySystem:
    books: List[Book] = []
    users: List[User] = []

    @classmethod
    def add_book(cls, book: Book):
        cls.books.append(book)

    @classmethod
    def register_user(cls, user: User):
        cls.users.append(user)

    @classmethod
    def borrow_book(cls, user: User, isbn: str):
        for book in cls.books:
            if book.isbn == isbn:
                if book.num_copies > 0:
                    book.num_copies -= 1
                    user.books_borrowed.append(book)
                    print(f"{user.name} has borrowed {book.title}.")
                    return
                else:
                    print("Sorry, no copies of this book are available.")
                    return
        print("Sorry, the book with the given ISBN is not available in the library system.")

    @classmethod
    def return_book(cls, user: User, isbn: str):
        for book in user.books_borrowed:
            if book.isbn == isbn:
                book.num_copies += 1
                user.books_borrowed.remove(book)
                print(f"{user.name} has returned {book.title}.")
                return
        print("Sorry, the user has not borrowed the book with the given ISBN.")

    @classmethod
    def list_books(cls) -> List[Book]:
        return cls.books

    @classmethod
    def list_users(cls) -> List[User]:
        return cls.users


book1 = Book("The Hobbit", "J.R.R. Tolkien", "1234", 5)
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", "5678", 3)
book3 =Book("LOTR", "Pino Daniele", "1574", 4)
LibrarySystem.add_book(book1)
LibrarySystem.add_book(book2)
LibrarySystem.add_book(book3)

user1 = User("John Doe", "johndoe@example.com")
user2 = User("Jane Doe", "janedoe@example.com")
LibrarySystem.register_user(user1)
LibrarySystem.register_user(user2)

LibrarySystem.borrow_book(user1, "1574")
LibrarySystem.borrow_book(user1, "1234")
LibrarySystem.borrow_book(user2, "5678")
LibrarySystem.borrow_book(user1, "5678")


LibrarySystem.return_book(user1, "1234")
LibrarySystem.return_book(user1, "5678")
LibrarySystem.return_book(user2, "5678")

books = LibrarySystem.list_books()
for book in books:
    print(
        f"{book.title} by {book.author}, ISBN: {book.isbn}, Copies available: "
        f"{book.num_copies}"
    )

users = LibrarySystem.list_users()
for user in users:
    print(f"{user.name} ({user.email}) has borrowed:")
    for book in user.books_borrowed:
        print(f"- {book.title} by {book.author}, ISBN: {book.isbn}")
