# Lesson Databases - FlaskSQLAlchemy       date 07/04/2025

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from typing import List, Optional

app: Flask = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']: str = 'sqlite:///example.db'
db: SQLAlchemy = SQLAlchemy(app)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#
# with app.app_context():
#     db.create_all()
#
#     # new_user: User = User(username='t', email='t@example.com')
#     # db.session.add(new_user)
#     # db.session.commit()
#
#     # Fetching all users
#     all_users: List[User] = User.query.all()
#
#     # Fetching a user by id
#     user_obj: User = db.session.get(User, 1)
#
#     if user_obj:
#         print(user_obj.email)
#
#     user_obj: User = db.session.get(User, 1)
#
#     if user_obj:
#         user_obj.email = 'new5_email@example.com'
#         db.session.commit()
#         print(user_obj.email)  # new5_email@example.com
#
#     # Fetching a user by id
#     user_obj: User = db.session.get(User, 1)
#
#     if user_obj:
#         db.session.delete(user_obj)
#         db.session.commit()

# Define the Student model
class Student(db.Model):
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(100), nullable=False)
    age: int = db.Column(db.Integer, nullable=False)
    grade: str = db.Column(db.String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<Student {self.name}>"

# Create the database and tables
with app.app_context():
    db.create_all()

# Helper functions for CRUD operations

def add_student(name: str, age: int, grade: str) -> None:
    student: Student = Student(name=name, age=age, grade=grade)
    db.session.add(student)
    db.session.commit()
    return student


def get_student_by_id(id: int) -> Optional[Student]:
    return db.session.get(Student, id)

def get_all_students() -> List[Student]:
    return Student.query.all()

def update_student(id: int, name: str, age: int, grade: str) -> None:
    student: Optional[Student] = db.session.get(Student, id)
    if student:
        student.name = name
        student.age = age
        student.grade = grade
        db.session.commit()
    return student

def delete_student(id: int) -> None:
    student: Optional[Student] = db.session.get(Student, id)
    if student:
        db.session.delete(student)
        db.session.commit()

if __name__ == '__main__':
    # Sample usage of the functions:
    with app.app_context():

        # Add students
        student1: Student = add_student('John Doe', 22, 'A')
        student2: Student = add_student('Jane Smith', 20, 'B')

        # Get students by ID
        print(get_student_by_id(student1.id))
        print(get_student_by_id(student2.id))
        # Get all students
        all_students: List[Student] = get_all_students()
        for student in all_students:
            print(student)

        # Update student
        update_student(student1.id, "Pino Daniele", 26, "B")
        updated_student: Optional[Student] = get_student_by_id(student1.id)
        if updated_student:
            print(updated_student)

        # Delete student
        delete_student(student2.id)
