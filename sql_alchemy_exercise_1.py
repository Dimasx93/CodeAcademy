# Lesson SQLAlchemy ORM                                    Date 24/02/2025

# Exercise n1 Employee Database

# import datetime
#
# from sqlalchemy import Column, Date, Float, Integer, String, create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
#
# engine = create_engine("sqlite:///employees.db")
# Base = declarative_base()
#
#
# class Employee(Base):
#     __tablename__ = "employee"
#     id = Column(Integer, primary_key=True)
#     name = Column("name", String)
#     surname = Column("surname", String)
#     birthdate = Column("birthdate", Date)
#     position = Column("position", String)
#     salary = Column("salary", Float)
#     start_date = Column("start_date", Date, default=datetime.date.today)
#
#     def __repr__(self):
#         return (
#             f"ID: {self.id}, Name: {self.name} {self.surname}, Birthdate: "
#             f"{self.birthdate}, Position: {self.position}, Salary: {self.salary:.2f}, "
#             f"Start Date: {self.start_date}"
#         )
#
#
# def create_employee(name, surname, birthdate, position, salary, start_date=None):
#     birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d").date()
#
#     if start_date:
#         start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
#     else:
#         start_date = datetime.date.today()
#
#     new_employee = Employee(
#         name=name,
#         surname=surname,
#         birthdate=birthdate,
#         position=position,
#         salary=salary,
#         start_date=start_date,
#     )
#     session.add(new_employee)
#     session.commit()
#     print(f"Employee {name} {surname} added successfully with start date {start_date}.")
#
#
# def read_all_employees():
#     employees = session.query(Employee).all()
#     if employees:
#         for emp in employees:
#             print(emp)
#     else:
#         print("No employees found.")
#
#
# # Dynamically updates specific attributes of an employee in the database.
# #
# # The `**kwargs` syntax packs any number of keyword arguments (field-value
# # pairs) into a dictionary-like format, allowing flexible updates for any
# # combination of fields.
# #
# # The function uses `hasattr` to check if the `Employee` object has the
# # specified attribute (field) before applying the update. This prevents errors
# # in case an invalid field name is passed.
# #
# # The `setattr` function is used to dynamically set the value of the specified
# # attribute on the `Employee` object. This allows updates to be applied without
# # hardcoding specific field names.
# def update_employee(emp_id, **kwargs):
#     employee = session.get(Employee, emp_id)
#     if employee:
#         for key, value in kwargs.items():
#             if hasattr(employee, key):
#                 setattr(employee, key, value)
#         session.commit()
#         print(f"Employee ID {emp_id} updated successfully.")
#     else:
#         print(f"Employee ID {emp_id} not found.")
#
#
# def delete_employee(emp_id):
#     employee = session.get(Employee, emp_id)
#     if employee:
#         session.delete(employee)
#         session.commit()
#         print(f"Employee ID {emp_id} deleted successfully.")
#     else:
#         print(f"Employee ID {emp_id} not found.")
#
#
# def main():
#     while True:
#         print(
#             "\n"
#             "Options:\n"
#             "1. Add employee\n"
#             "2. View all employees\n"
#             "3. Update employee\n"
#             "4. Delete employee\n"
#             "5. Quit"
#         )
#
#         choice = int(input("Enter your choice: "))
#
#         match choice:
#             case 1:
#                 name = input("Enter employee's first name: ")
#                 surname = input("Enter employee's surname: ")
#                 birthdate = input("Enter employee's birthdate (YYYY-MM-DD): ")
#                 position = input("Enter employee's position: ")
#                 salary = float(input("Enter employee's salary: "))
#                 start_date = input(
#                     "Enter employee's start date (YYYY-MM-DD) or press Enter to use "
#                     "today's date: "
#                 )
#
#                 if start_date == "":
#                     start_date = None
#
#                 create_employee(name, surname, birthdate, position, salary, start_date)
#             case 2:
#                 read_all_employees()
#             case 3:
#                 emp_id = int(input("Enter employee ID to update: "))
#                 updates = {}
#                 name = input("Enter new name (leave blank to skip): ")
#                 surname = input("Enter new surname (leave blank to skip): ")
#                 position = input("Enter new position (leave blank to skip): ")
#                 salary = input("Enter new salary (leave blank to skip): ")
#                 if name:
#                     updates["name"] = name
#                 if surname:
#                     updates["surname"] = surname
#                 if position:
#                     updates["position"] = position
#                 if salary:
#                     updates["salary"] = float(salary)
#                 # The `**updates` syntax unpacks the dictionary of field-value
#                 # pairs into keyword arguments, allowing them to be processed
#                 # dynamically inside the function.
#                 update_employee(emp_id, **updates)
#             case 4:
#                 emp_id = int(input("Enter employee ID to delete: "))
#                 delete_employee(emp_id)
#             case 5:
#                 print("Goodbye!")
#                 break
#             case _:
#                 print("Invalid option. Please try again.")
#
#
# if __name__ == "__main__":
#     Base.metadata.create_all(engine)
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#
#     main()
#
#     session.close()
