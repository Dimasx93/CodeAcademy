#Lesson OOP: Magic Methods        20/01/2025

#Exercise n1 Product Representation

# class Product:
#     def __init__(self, name:str, price:float):
#         self.name = name
#         self.price = price
#     def __str__(self):
#         return f"Product: {self.name}, Price: {self.price}"
#     def __repr__(self):
#         return f"Product('{self.name}','{self.price}')"
# p = Product("Ham", 5)
# print(p)
# print(repr(p))

#######################################################################

#Exercise n2 MyQueue Class

# class MyQueue:
#     def __init__(self, queue:list):
#         self.queue = queue
#
#     def __bool__(self):
#         return bool(self.queue)
#     def __repr__(self):
#         return f"MyQueue({self.queue})"
#     def __len__(self):
#         return len(self.queue)
# my_queue = MyQueue([0,1,2])
# print(repr(my_queue))
# print(bool(my_queue))
# print(len(my_queue))

#######################################################################

#Exercise n3 Building a Custom String Class

# class MyString:
#     def __init__(self, sentence:str):
#         self.sentence = sentence
#     def __getitem__(self, idx):
#         return self.sentence[idx]
#     def __len__(self):
#         return len(self.sentence)
#     def __invert__(self):
#         return self.sentence[::-1]
#     def __repr__(self):
#         return f"MyString({self.sentence})"
# s = MyString("hello")
# print(s[1])  # Output: e
# print(len(s))  # Output: 5
# print(~s)  # Output: olleh
# print(repr(s))

#######################################################################

#Exercise n4 Container

# class Container:
#     def __init__(self, container:list):
#         self.container = container
#     def __eq__(self, other:"Container"):
#         if isinstance(other, Container):
#             return set(self.container) == set(other.container)
#         return False
#     def __contains__(self, item):
#         return item in self.container
#     def __repr__(self):
#         return f"Container: ({self.container})"
# c1 = Container([1, 2, 3])
# c2 = Container([3, 2, 1])
# print(1 in c1)  # Output: True
# print(c1 == c2)  # Output: True

#######################################################################

#Exercise n5 Book

# class Book:
#     def __init__(self, title:str, author:str, isbn:str, pages:int):
#         self.title = title
#         self.author = author
#         self.isbn = isbn
#         self.pages = pages
#     def __bool__(self):
#         return bool(self.title)
#     def __repr__(self):
#         return f"Book({self.title},{self.author},{self.isbn})"
#     def __len__(self):
#         return self.pages
#     def __str__(self):
#         return f"{self.title} by {self.author} ({self.isbn})"
#     def __eq__(self, other:"Book"):
#         if isinstance(other, Book):
#             return self.isbn == other.isbn
#         raise TypeError("unsupported operand type(s) for ==: 'Book' and '{}'".format(type(other).__name__))
#     def __add__(self, other):
#         if isinstance(other, Book):
#             new_pages = self.pages + other.pages
#             return Book(self.title,self.author + " and " + other.author,self.isbn , new_pages)
#     def __getitem__(self, index):
#         if index == 0:
#             return self.title
#         elif index == 1:
#             return self.author
#         else:
#             raise IndexError("Invalid index")
# book1 = Book("ciao","ste", "asdasd", 75)
# book2 = Book("hello", "Gino", "qweqwe", 100)
# book3 = book1 + book2
# print(repr(book1))
# print(book3)
# print(len(book1))
# print(book2[1])
# print(book1 == book2)
# print(bool(book1))

#Exercise n6 Implement a Polynomial Class

class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients  # list of numbers

    def __call__(self, x):
        return sum(coef * x**i for i, coef in enumerate(self.coefficients))

    def __add__(self, other):
        max_len = max(len(self.coefficients), len(other.coefficients))
        result = [0] * max_len
        for i in range(max_len):
            coef1 = self.coefficients[i] if i < len(self.coefficients) else 0
            coef2 = other.coefficients[i] if i < len(other.coefficients) else 0
            result[i] = coef1 + coef2
        return Polynomial(result)

    def __mul__(self, other):
        result = [0] * (len(self.coefficients) + len(other.coefficients) - 1)
        for i, a in enumerate(self.coefficients):
            for j, b in enumerate(other.coefficients):
                result[i + j] += a * b
        return Polynomial(result)

    def __repr__(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                if i == 0:
                    terms.append(f"{coef}")
                elif i == 1:
                    terms.append(f"{coef}x")
                else:
                    terms.append(f"{coef}x^{i}")
        return " + ".join(terms) if terms else "0"