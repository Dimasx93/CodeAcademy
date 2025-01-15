#Lesson OOP: Method Chaining & super() Function    14/01/2025

#Exercise n1 Person Class

# class Person:
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age
#
#     def set_name(self, name: str) -> "Person":
#         self.name = name
#         return self
#
#     def set_age(self, age: int) -> "Person":
#         self.age = age
#         return self
#
# person = Person("Poppy", 22)
# person.set_age(10).set_name("Pippo")
# print(person.age)
# print(person.name)

#########################################################################

#Exercise n2 Dogs and Cats

# class Animal:
#     def speak(self):
#         print("Animal can't speak.")
#
# class Dog(Animal):
#     def speak(self):
#         print("Woof woof.")
#
# class Cat(Animal):
#     def speak(self):
#         super().speak()
#         print("Meow meow.")
#
# cat = Cat()
# dog = Dog()
# cat.speak()
# dog.speak()

############################################################################

#Exercise n3 Currency

# class Currency:
#     def __init__(self,code:str, amount:float, exchange_rate:float) -> None:
#         self.code = code
#         self.amount = amount
#         self.exchange_rate = exchange_rate
#
#     def set_code(self, code:str) -> "Currency":
#         self.code = code
#         return self
#     def set_amount(self,amount:float) -> "Currency":
#         self.amount = amount
#         return self
#     def set_exchange_rate(self, exchange_rate:float) -> "Currency":
#         self.exchange_rate = exchange_rate
#         return self
#
#     def convert(self, new_code:str, new_exchange_rate:float) -> "Currency":
#         self.amount = (self.amount * new_exchange_rate) / self.exchange_rate
#         self.code = new_code
#         self.exchange_rate = new_exchange_rate
#         return self
#
#     def __str__(self):
#         return f"{self.code}: {self.amount:.2f}"
#
# currency = Currency("USD", 100, 1.0)
# print(currency.set_code("EUR").set_amount(200).set_exchange_rate(0.9))  # Method chaining
# print(currency.convert("GBP", 0.8))  # Convert from EUR to GBP using a new exchange rate

#############################################################################

#Exercise n4 Student

# class Person:
#     def __init__(self,name:str, age:int):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#     def __str__(self):
#         return f"{self.name} is {self.age} years old."
#
# class Student(Person):
#     def __init__(self, name:str, age:int ,student_id:int, major:str):
#         super().__init__(name,age)
#         self.student_id = student_id
#         self.major = major
#
#     def get_student_id(self):
#         return self.student_id
#
#     def get_major(self):
#         return self.major
#
#     def __str__(self):
#         return f"{super().__str__()} is a student of {self.major} major. Student id: {self.student_id}."
#
# class GraduateStudent(Student):
#     def __init__(self, name:str, age:int ,student_id:int, major:str, program:str, advisor: str):
#         super().__init__(name,age,student_id,major)
#         self.program = program
#         self.advisor = advisor
#
#     def get_program(self):
#         return self.program
#     def get_advisor(self):
#         return self.advisor
#     def __str__(self) -> str:
#         return f"{super().__str__()} program: {self.program} and advisor {self.advisor}"
#
# graduate_student = GraduateStudent("Stefano Di Mauro", 31, 2205, "Python", "Game Developer", "Paulius")
# print(graduate_student.get_student_id())
# print(graduate_student.__str__())



