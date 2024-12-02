# Recap lesson

# Exercise n5 Expense Tracker

# class ExpenseTracker:
#     def __init__(self):
#         self.expenses = []
#
#     def add_expense(self, name: str, amount: float, category: str):
#         self.expenses.append((name, amount, category))
#
#     def remove_expense(self, description):
#         for index, expense in enumerate(self.expenses):
#             if description == expense[0]:
#                 self.expenses.pop(index)
#                 return
#         print(f"Expense with description '{description}' not found.")
#
#     def display_expenses(self):
#         if not self.expenses:
#             print("No expenses recorded.")
#         for expense in self.expenses:
#             print(f"Expense: {expense[0]}, Amount: ${expense[1]}, Category: {expense[2]}")
#
#     def filter_by_category(self, param):
#         filtered = [f"{expense[0]}: ${expense[1]:.2f}" for expense in self.expenses if expense[2] == param]
#         if not filtered:
#             return f"No expenses found for category '{param}'."
#         return " ".join(filtered)
#
#     def total_expenses(self):
#         total = sum(expense[1] for expense in self.expenses)
#         return f"{total:.2f}"
#
#
# tracker = ExpenseTracker()
# tracker.add_expense("Coffee", 5.00, "Food")
# tracker.add_expense("Taxi", 15.00, "Transport")
# tracker.add_expense("Book", 20.00, "Education")
# tracker.add_expense("Pizza", 12.00, "Food")
# tracker.remove_expense("Coffee")
# tracker.add_expense("Tea", 4.00, "Food")
# tracker.display_expenses()
#
# print(f"Total Expenses: ${tracker.total_expenses()}")
# print("Food Expenses:", tracker.filter_by_category("Food"))

#Exercise n1 Handling Exceptions

# class InvalidAgeError(Exception):
#     def __init__(self, age):
#         self.age = age
#         super().__init__(f"InvalidAgeError: Age is {self.age}. Minimum age is 18.")
#
# def validate_age(age, min_age=18):
#     if age < min_age:
#         raise InvalidAgeError(age)
#
# try:
#     validate_age(15)  # Assuming the valid age for the action is 18
# except InvalidAgeError as e:
#     print(e)

#Exercise n2 Sort Employee Records

# def sort_employees_by_salary(employees):
#     return sorted(employees, key=lambda x: x['salary'], reverse=True)
#
# employees = [
#     {'name': 'Alice', 'age': 30, 'salary': 70000},
#     {'name': 'Bob', 'age': 25, 'salary': 50000},
#     {'name': 'Charlie', 'age': 35, 'salary': 60000}
# ]
#
# sorted_employees = sort_employees_by_salary(employees)
# for emp in sorted_employees:
#     print(f"Name: {emp['name']}, Age: {emp['age']}, Salary: ${emp['salary']}")

#Exercise n3 Top N Items

# items = [10, 20, 5, 7, 35, 12, 15]
#
# def top_n_items(items:list, param:int):
#     return sorted(items, reverse=True)[:param]
#
# top_items = top_n_items(items, 3)
# print(top_items)

#Exercise n4 Grouping by First Letter

# strings = ["apple", "banana", "apricot", "blueberry", "cherry"]
#
# def group_by_first_letter(strings):
#     grouped = {}
#     for string in strings:
#         key = string[0].lower()
#         if key in grouped:
#             grouped[key].append(string)
#         else:
#             grouped[key] = [string]
#     return grouped
#
# grouped = group_by_first_letter(strings)
# for letter, words in grouped.items():
#     print(f"{letter}: {words}")

#Exercise n6 Employee/Manager

class Employee:
    def __init__(self, name:str, age:int, salary:int):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: ${self.salary}")

class Manager(Employee):
    def __init__(self,name:str, age:int, salary:int, department:str):
        super().__init__(name, age, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")

emp = Employee('John Doe', 30, 50000)
mgr = Manager('Jane Smith', 40, 70000, 'HR')
emp.display_details()
mgr.display_details()