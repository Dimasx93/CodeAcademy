#Lesson SQL Introduction, SQLite             date: 18/02/2025

#Exercise n1  Database: Part 1

# import sqlite3
#
# conn = sqlite3.connect("employees_1.sqlite")
# c = conn.cursor()
#
# data = c.execute("SELECT * FROM employees")
# for column in data.description:
#     print(column[0])
#
# query = """SELECT * FROM employees"""
# query = """SELECT birthdate FROM employees"""
# query = """SELECT name,surname,position FROM employees"""
# query = """SELECT DISTINCT department FROM employees"""
# query = """SELECT * FROM employees WHERE department = 'Production'"""
# query = """SELECT position FROM employees WHERE name = 'George'"""
# query = """SELECT * FROM employees WHERE birthdate = DATE('1986-09-19')"""
# query = """SELECT * FROM employees WHERE surname = 'Mitchell'"""
# query = """SELECT name, surname FROM employees WHERE position = 'Programmer' AND department = 'Production'"""
# query = """INSERT INTO employees (name,surname,birthdate) VALUES ('Stefano','Di Mauro', DATE('1998-01-10'))"""
# query = """UPDATE employees SET position='Python Dev', department='Production' WHERE name = 'Stefano'"""
# query = """SELECT * FROM employees WHERE surname = 'Di Mauro'"""
# query = """DELETE FROM employees WHERE birthdate = DATE('1998-01-10')"""
# query = """INSERT INTO employees (name, surname, birthdate, position, department)
# VALUES ('Alice', 'Mitchell', DATE=('1992-03-05'), 'Programmer', 'Production'),
#        ('Bob', 'Mitchell', DATE=('1989-09-12'), 'Programmer', 'Production')"""
# query = """UPDATE employees SET position='Tester' WHERE surname = 'Mitchell'"""
# query = """SELECT COUNT(*) FROM employees WHERE position = 'Tester'"""
#
# with conn:
#     c.execute(query)
#     print(c.fetchall())

########################################################################################

#Exercise n2 Employee Database: Part 2

# import sqlite3
#
# conn = sqlite3.connect("employees_2.sqlite")
# c = conn.cursor()
#
# data = c.execute("""SELECT * FROM employee""")
# for column in data.description:
#     print(column[0])

# query = """SELECT name,surname,birthdate,social_security_number FROM employee WHERE birthdate = DATE('1988-07-20')"""
# query = """SELECT social_security_number,start_date FROM employee WHERE start_date BETWEEN DATE('2009-10-30') AND DATE('2012-11-12')"""
# query = """SELECT name,department_id,project_id FROM employee WHERE department_id IN ('2','3')"""
# query = """SELECT * FROM employee WHERE birthdate LIKE('____-__-12')"""
# query = """SELECT * FROM project WHERE name LIKE('_a%')"""
# query = """SELECT * FROM employee WHERE position IS NULL"""
# query = """SELECT name,surname,start_date,position FROM employee WHERE start_date > DATE('2011-02-12') AND position ='Programmer'"""
# query = """SELECT name,surname,department_id,project_id FROM employee WHERE department_id='2' OR project_id ='1'"""
# query = """SELECT name FROM employee WHERE name NOT LIKE ('A%')"""
# query = """SELECT name,surname,start_date FROM employee ORDER BY start_date"""
# query = """SELECT name,surname,start_date FROM employee ORDER BY start_date DESC"""
# query = """SELECT MIN(project_id), MAX(project_id) FROM employee"""
# query = """SELECT project_id ,COUNT(*) AS number_of_employees FROM employee GROUP BY project_id"""
# query = """SELECT project_id ,COUNT(*) AS number_of_employees FROM employee GROUP BY project_id HAVING COUNT(*) > 3"""
# query = """SELECT project_id ,position='Programmer', COUNT(*) AS number_of_employees FROM employee GROUP BY project_id, position"""
# query = """SELECT employee.project_id,
#        employee.position,
#        COUNT(employee.id) AS number_of_employees
# FROM employee
# WHERE employee.position = 'Programmer'
# GROUP BY employee.project_id, employee.position"""

# with conn:
#     c.execute(query)
#     print(c.fetchall())

########################################################################################

#Exercise n3 Employee Database: Part 3

import sqlite3

conn = sqlite3.connect("employees_3.sqlite")
c = conn.cursor()

c.execute("SELECT name FROM sqlite_master WHERE type='table';")
table_names = c.fetchall()
for table_name in table_names:
    table_name = table_name[0]
    print(f"\nColumns in {table_name} table:")
    data = c.execute(f"SELECT * FROM {table_name}")
    for column in data.description:
        print(column[0])

# query = """SELECT employee.name, employee.surname, project.name AS project_name FROM employee JOIN project ON employee.project_id = project.id"""
# query = """SELECT employee.name, employee.surname, project.name AS project_name FROM employee JOIN project ON employee.project_id = project.id
# WHERE project.name = 'Gallery'"""
# query = """SELECT employee.*
# FROM employee
# JOIN project ON employee.project_id = project.id
# JOIN department ON employee.department_id = department.id
# WHERE project.name = 'Project Management'
#   AND department.name = 'Sales'"""
# query = """SELECT department.name, COUNT(employee.id) AS number_of_employee FROM employee
# JOIN department ON employee.department_id = department.id
# GROUP BY department.name"""
# query = """SELECT department.name, COUNT(employee.id) AS number_of_employee FROM employee
# JOIN department ON employee.department_id = department.id
# GROUP BY department.name HAVING COUNT(employee.id) >=5"""
# query = """SELECT employee.name, employee.surname, employee.position, department.name AS list_of_employees
# FROM employee JOIN department ON employee.department_id = department.id
# WHERE employee.position != 'Director'"""
# query="""INSERT INTO employee(name,surname,social_security_number,start_date)
# VALUES('Frank','Lewis',523847291,'2009-11-12')"""
# query="""SELECT employee.name,employee.surname,department.name FROM employee LEFT JOIN department
# ON employee.department_id = department.id"""
# query = """SELECT employee.name, employee.surname, project.name AS project_name FROM employee
# JOIN project ON employee.project_id = project.id WHERE employee.project_id IN(
#     SELECT project_id
#     FROM employee
#     GROUP BY project_id
#     HAVING COUNT(employee.id) > 4
# )"""
# query="""ALTER TABLE employee ADD COLUMN base_plus_bonuses REAL;"""
# query ="""    UPDATE employee SET base_plus_bonuses = base_salary + bonuses;"""
query="""SELECT SUM(employee.base_salary),SUM(employee.bonuses),MAX(employee.base_salary),MIN(employee.base_salary),
AVG(employee.base_salary) FROM employee"""

with conn:
    c.execute(query)
    print(c.fetchall())