#Lesson OOP: Instance and Static Methods   15/01/2025

#Exercise n1  Temperature Converter Class

# class Temperature:
#     def __init__(self, temperature:float):
#         self.temperature = temperature
#
#     @staticmethod
#     def kelvin_to_celsius(temperature):
#         return round(temperature - 273.15, 1)
#     @staticmethod
#     def kelvin_to_fahrenheit(temperature):
#         return round((temperature - 273.15) * 9 / 5 + 32, 1)
#     def __str__(self):
#         celsius = Temperature.kelvin_to_celsius(self.temperature)
#         fahrenheit = Temperature.kelvin_to_fahrenheit(self.temperature)
#         return f"Temperature: {self.temperature}K, {celsius}°C, {fahrenheit}°F"
# temp = Temperature(300)
# print(temp)
# print(Temperature.kelvin_to_celsius(300))
# print(Temperature.kelvin_to_fahrenheit(300))

####################################################################################

#Exercise n2 Imperial to Metric System

# class ImperialToMetric:
#     @staticmethod
#     def inches_to_centimeters(inches:float):
#         return round(inches * 2.54, 2)
#     @staticmethod
#     def feet_to_meters(feet:float):
#         return round(feet * 0.3048, 2)
#     @staticmethod
#     def miles_to_kilometers(miles):
#         return round(miles * 1.60934, 2)
#     @staticmethod
#     def pounds_to_kilograms(pounds):
#         return round(pounds * 0.453592, 2)
#     @staticmethod
#     def gallons_to_liters(gallons):
#         return round(gallons * 3.78541, 2)
# print(ImperialToMetric.feet_to_meters(6))
# print(ImperialToMetric.pounds_to_kilograms(270))

####################################################################################

#Exercise n3 TimeUtils

# class TimeUtils:
#     @staticmethod
#     def time_to_seconds(time_strings:str):
#         # time_seconds = time_strings.split(":")
#         # hours = int(time_seconds[0]) * 3600
#         # minutes = int(time_seconds[1]) * 60
#         # seconds = int(time_seconds[2]) + minutes + hours
#         # return seconds
#     # Split the time string into hours, minutes, and seconds
#         hours, minutes, seconds = map(int, time_strings.split(":"))
#     # Calculate the total seconds
#         total_seconds = hours * 3600 + minutes * 60 + seconds
#         return total_seconds
#
# time_string = "01:02:03"  # 1 hour, 2 minutes, and 3 seconds
# seconds = TimeUtils.time_to_seconds(time_string)
# print(f"Total seconds in '{time_string}' is {seconds} seconds.")

####################################################################################

#Exercise n4 Employee Payroll

# class Employee:
#     def __init__(self,name:str, salary:float):
#         self.name = name
#         self.salary = salary
#
#     @staticmethod
#     def calculate_payroll(employees:list):
#         salaries = 0
#         for employee in employees:
#             salaries += employee.salary
#         return salaries
#
# employees = [
#     Employee("Alice", 5000.0),
#     Employee("Bob", 6000.0),
#     Employee("Charlie", 7000.0),
# ]
# print(Employee.calculate_payroll(employees))

####################################################################################

#Exercise n5 Complex Employee Management System

class Employee:
    raise_amt = 1.03

    def __init__(self, name:str, emp_id, salary:float):
        self.name = name
        self.emp_id = emp_id
        self._salary = salary

    def give_raise(self):
        self._salary *= self.raise_amt

    @classmethod
    def set_raise_amt(cls, percentage:float):
        cls.raise_amt = percentage

    @staticmethod
    def standard_performance_index(score:int):
        return score / 100

class Manager(Employee):
    def __init__(self,name:str, emp_id, salary:float):
        super().__init__(name, emp_id, salary)
        self.subordinates = []

    def add_subordinate(self,emp:Employee):
        self.subordinates.append(emp)

    def remove_subordinate(self,emp_id):
        self.subordinates = [emp for emp in self.subordinates if emp.emp_id != emp_id]

mgr = Manager("Jane Doe", "001", 90000)
emp = Employee("John Smith", "002", 50000)
mgr.add_subordinate(emp)

# Applying changes and displaying information
mgr.give_raise()
print(mgr._salary)  # Output: 92700.0
