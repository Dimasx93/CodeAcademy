# #Lesson MongoDB: Aggregation Pipelines                                      date: 04/03/2025
#
# #Exercise n1 More Work with Products

# from typing import Any
#
# from pymongo import MongoClient
# from pymongo.collection import Collection
# from pymongo.cursor import Cursor
#
#
# client = MongoClient("mongodb://localhost:27017")
# db = client["storeDB"]
# collection = db["products"]
#
# sample_data_with_attributes: list[dict[str, Any]] = [
#     {"name": "Laptop", "category": "electronics", "price": 1200, "status": "active",
#      "attributes": {"brand": "Dell", "warranty": "2 years"}},
#     {"name": "Smartphone", "category": "electronics", "price": 800, "status": "active",
#      "attributes": {"brand": "Apple", "warranty": "1 year"}},
#     {"name": "Headphones", "category": "electronics", "price": 150, "status": "inactive",
#      "attributes": {"brand": "Logitech"}},
#     {"name": "T-Shirt", "category": "clothing", "price": 20, "status": "active",
#      "attributes": {"size": "M", "color": "Blue"}},
#     {"name": "Jeans", "category": "clothing", "price": 50, "status": "active",
#      "attributes": {"size": "32", "color": "Black"}},
#     {"name": "Blender", "category": "home appliances", "price": 100, "status": "inactive",
#      "attributes": {"brand": "Vitamix", "power": "500W"}},
#     {"name": "Coffee Maker", "category": "home appliances", "price": 80, "status": "active",
#      "attributes": {"brand": "Nespresso", "power": "800W"}},
#     {"name": "Microwave", "category": "home appliances", "price": 200, "status": "active",
#      "attributes": {"brand": "Panasonic", "power": "1200W"}},
#     {"name": "Sneakers", "category": "clothing", "price": 100, "status": "active",
#      "attributes": {"size": "10", "color": "White", "brand": "Nike"}},
#     {"name": "Microphone", "category": "electronics", "price": 150, "status": "inactive",
#      "attributes": {"brand": "Shure"}},
#     {"name": "Soundbar", "category": "electronics", "price": 300, "status": "active",
#      "attributes": {"brand": "Samsung", "warranty": "2 years"}},
#     {"name": "Vacuum Cleaner", "category": "home appliances", "price": 150, "status": "active",
#      "attributes": {"brand": "Dyson", "power": "700W"}},
# ]
#
# collection.delete_many({})
# collection.insert_many(sample_data_with_attributes)
#
# def project_documents(collection:Collection, projection_fields: dict[str,int]) -> Cursor:
#     pipeline: list[dict[str,Any]] = [{"$project": projection_fields}]
#     return collection.aggregate(pipeline)
#
# def group_documents(collection:Collection, group_fields: dict[str,Any]) -> Cursor:
#     pipeline: list[dict[str,Any]] = [{"$group" : group_fields}]
#     return collection.aggregate(pipeline)
#
# def aggregate_documents(collection:Collection, pipeline: list[dict[str,Any]]) -> Cursor:
#     return collection.aggregate(pipeline)
#
#  criteria = {"status": "inactive", "price": {"$gt": 50}}
# sort_criteria = {"name": 1}
#
# pipeline = [
#     {"$match": criteria},
#     {"$sort": sort_criteria}
# ]
#
# filter_sort_result = aggregate_documents(collection, pipeline)
#
# print("\nFiltered and Sorted Products:")
# for doc in filter_sort_result:
#     print(doc)
#
# projection = {
#     "_id" : 0,
#     "name" : 1,
#     "original_price" : "$price",
#     "discount_price" : {
#         "$multiply" : ["$price", 0.85]
#     }
# }
#
# projection_result = project_documents(collection, projection)
#
# print("\nProducts with Computed 'sale_price':")
# for doc in projection_result:
#     print(doc)
#
# grouping_criteria = {
#     "_id" : "$status",
#     "total_products": {"$sum" : 1},
#     "max_price" : {"$max": "$price"}
# }
#
# grouping_result = group_documents(collection, grouping_criteria)
#
# print("\nProducts Grouped by Status:")
# for doc in grouping_result:
#     print(doc)
#
# combining_criteria = [
#     {"$match" : {"category" : "electronics"}},
#     {"$sort":{"price":-1}},
#     {"$limit":3},
#     {
#         "$project": {
#             "_id" : 0,
#             "name" : 1,
#             "price" : 1,
#             "brand" : "$attributes.brand",
#         }
#     }
# ]
#
# combining_result = aggregate_documents(collection,combining_criteria)
#
# print("\nTop 3 Most Expensive Electronic Devices:")
# for doc in combining_result:
#     print(doc)

############################################################################################################

# Exercise n2 Student Management System

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from datetime import datetime
from typing import Any

from pymongo.errors import DuplicateKeyError, WriteError
from pymongo.errors import CollectionInvalid


def get_database():
    try:
        client = MongoClient(
            "mongodb://localhost:27017/", serverSelectionTimeoutMS=5000
        )
        # Test connection
        client.admin.command("ping")
        print("Connected to MongoDB.")
        db = client["schoolDB"]
        return db
    except ConnectionFailure as e:
        print(f"Connection failed: {e}")
        raise


def create_students_collection(db):
    current_year = datetime.now().year

    validation_rules = {
        "$jsonSchema": {
            "bsonType": "object",
            "required": [
                "student_id",
                "first_name",
                "last_name",
                "enrollment_year",
                "major",
                "courses",
            ],
            "properties": {
                "student_id": {
                    "bsonType": "int",
                    "description": "'student_id' must be an integer and is required.",
                },
                "first_name": {
                    "bsonType": "string",
                    "description": "'first_name' must be a string and is required.",
                },
                "last_name": {
                    "bsonType": "string",
                    "description": "'last_name' must be a string and is required.",
                },
                "enrollment_year": {
                    "bsonType": "int",
                    "minimum": 2000,
                    "maximum": current_year,
                    "description": f"'enrollment_year' must be between 2000 and {current_year}.",
                },
                "major": {
                    "bsonType": "string",
                    "description": "'major' must be a string and is required.",
                },
                "courses": {
                    "bsonType": "array",
                    "description": "'courses' must be an array of course objects.",
                    "items": {
                        "bsonType": "object",
                        "required": ["course_id", "course_name", "grade"],
                        "properties": {
                            "course_id": {
                                "bsonType": "string",
                                "description": "'course_id' must be a string and is required.",
                            },
                            "course_name": {
                                "bsonType": "string",
                                "description": "'course_name' must be a string and is required.",
                            },
                            "grade": {
                                "bsonType": "string",
                                "pattern": "^[A-F]$",
                                "description": "'grade' must be one of A, B, C, D, or F.",
                            },
                        },
                    },
                },
            },
        }
    }

    try:
        db.create_collection("students")
        print("Collection 'students' created.")
    except CollectionInvalid:
        print("Collection 'students' already exists.")

    db.command(
        "collMod", "students", validator=validation_rules, validationLevel="strict"
    )
    print("Schema validation applied to 'students' collection.")

    # Create unique index on 'student_id'
    db.students.create_index("student_id", unique=True)


def add_student(db, student_data: dict[str, Any]):
    try:
        result = db.students.insert_one(student_data)
        print(f"Student added with _id: {result.inserted_id}")
    except DuplicateKeyError:
        print("Error: A student with this 'student_id' already exists.")
    except WriteError as e:
        print(f"Validation Error: {e.details['errmsg']}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def get_all_students(db):
    try:
        students = list(db.students.find())
        return students
    except Exception as e:
        print(f"An error occurred while retrieving students: {e}")
        return []


def get_student_by_id(db, student_id: int):
    try:
        student = db.students.find_one({"student_id": student_id})
        if student:
            return student
        else:
            print("Student not found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def update_student_major(db, student_id: int, new_major: str):
    try:
        result = db.students.update_one(
            {"student_id": student_id}, {"$set": {"major": new_major}}
        )
        if result.modified_count > 0:
            print("Student major updated successfully.")
        else:
            print("No changes made.")
    except WriteError as e:
        print(f"Validation Error: {e.details['errmsg']}")
    except Exception as e:
        print(f"An error occurred: {e}")


def add_course_to_student(db, student_id: int, course_data: dict[str, Any]):
    try:
        result = db.students.update_one(
            {"student_id": student_id}, {"$push": {"courses": course_data}}
        )
        if result.modified_count > 0:
            print("Course added to student.")
        else:
            print("Student not found.")
    except WriteError as e:
        print(f"Validation Error: {e.details['errmsg']}")
    except Exception as e:
        print(f"An error occurred: {e}")


def update_student_grade(db, student_id: int, course_id: str, new_grade: str):
    try:
        result = db.students.update_one(
            {"student_id": student_id, "courses.course_id": course_id},
            {"$set": {"courses.$.grade": new_grade}},
        )
        if result.modified_count > 0:
            print("Student grade updated successfully.")
        else:
            print("No changes made.")
    except WriteError as e:
        print(f"Validation Error: {e.details['errmsg']}")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_student(db, student_id: int):
    try:
        result = db.students.delete_one({"student_id": student_id})
        if result.deleted_count > 0:
            print("Student deleted successfully.")
        else:
            print("Student not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def find_students_by_enrollment_year(db, year: int):
    try:
        students = list(db.students.find({"enrollment_year": year}))
        return students
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def find_students_by_major(db, major: str):
    try:
        students = list(db.students.find({"major": major}))
        return students
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def find_students_by_grade(db, grade: str):
    try:
        students = list(db.students.find({"courses.grade": grade}))
        return students
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


def find_students_by_course(db, course_id: str):
    try:
        students = list(db.students.find({"courses.course_id": course_id}))
        return students
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def calculate_average_grade_per_course(db):
    pipeline = [
        {"$unwind": "$courses"},
        {
            "$project": {
                "course_id": "$courses.course_id",
                "grade_point": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$courses.grade", "A"]}, "then": 4},
                            {"case": {"$eq": ["$courses.grade", "B"]}, "then": 3},
                            {"case": {"$eq": ["$courses.grade", "C"]}, "then": 2},
                            {"case": {"$eq": ["$courses.grade", "D"]}, "then": 1},
                            {"case": {"$eq": ["$courses.grade", "F"]}, "then": 0},
                        ],
                        "default": None,
                    }
                },
            }
        },
        {
            "$group": {
                "_id": "$course_id",
                "average_grade_point": {"$avg": "$grade_point"},
                "student_count": {"$sum": 1},
            }
        },
        {"$sort": {"average_grade_point": -1}},
    ]
    result = db.students.aggregate(pipeline)
    print("\nAverage Grade per Course:")
    for doc in result:
        print(doc)


def count_students_per_major(db):
    pipeline = [
        {"$group": {"_id": "$major", "student_count": {"$sum": 1}}},
        {"$sort": {"student_count": -1}},
    ]
    result = db.students.aggregate(pipeline)
    print("\nStudents per Major:")
    for doc in result:
        print(doc)


def find_top_performing_students(db, threshold: float):
    pipeline = [
        {"$unwind": "$courses"},
        {
            "$project": {
                "student_id": 1,
                "first_name": 1,
                "last_name": 1,
                "grade_point": {
                    "$switch": {
                        "branches": [
                            {"case": {"$eq": ["$courses.grade", "A"]}, "then": 4},
                            {"case": {"$eq": ["$courses.grade", "B"]}, "then": 3},
                            {"case": {"$eq": ["$courses.grade", "C"]}, "then": 2},
                            {"case": {"$eq": ["$courses.grade", "D"]}, "then": 1},
                            {"case": {"$eq": ["$courses.grade", "F"]}, "then": 0},
                        ],
                        "default": None,
                    }
                },
            }
        },
        {
            "$group": {
                "_id": {
                    "student_id": "$student_id",
                    "first_name": "$first_name",
                    "last_name": "$last_name",
                },
                "average_grade_point": {"$avg": "$grade_point"},
            }
        },
        {"$match": {"average_grade_point": {"$gte": threshold}}},
        {"$sort": {"average_grade_point": -1}},
    ]
    result = db.students.aggregate(pipeline)
    print(f"\nTop Performing Students (Average GPA >= {threshold}):")
    for doc in result:
        print(doc)


def analyze_enrollment_trends(db):
    pipeline = [
        {"$group": {"_id": "$enrollment_year", "student_count": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
    ]
    result = db.students.aggregate(pipeline)
    print("\nEnrollment Trends:")
    for doc in result:
        print(doc)

def main():
    db = get_database()
    create_students_collection(db)

    # Sample data
    students = [
        {
            "student_id": 1001,
            "first_name": "Alice",
            "last_name": "Johnson",
            "enrollment_year": 2021,
            "major": "Computer Science",
            "courses": [
                {"course_id": "CS101", "course_name": "Intro to CS", "grade": "A"},
                {"course_id": "CS102", "course_name": "Data Structures", "grade": "B"},
            ],
        },
        {
            "student_id": 1002,
            "first_name": "Bob",
            "last_name": "Smith",
            "enrollment_year": 2020,
            "major": "Mathematics",
            "courses": [
                {"course_id": "MATH201", "course_name": "Calculus I", "grade": "A"},
                {"course_id": "MATH202", "course_name": "Calculus II", "grade": "A"},
            ],
        },
        {
            "student_id": 1003,
            "first_name": "Carol",
            "last_name": "Williams",
            "enrollment_year": 2019,
            "major": "Physics",
            "courses": [
                {
                    "course_id": "PHYS101",
                    "course_name": "General Physics",
                    "grade": "B",
                },
                {"course_id": "MATH201", "course_name": "Calculus I", "grade": "C"},
            ],
        },
        {
            "student_id": 1004,
            "first_name": "David",
            "last_name": "Brown",
            "enrollment_year": 2021,
            "major": "Computer Science",
            "courses": [
                {"course_id": "CS101", "course_name": "Intro to CS", "grade": "B"},
                {"course_id": "CS103", "course_name": "Algorithms", "grade": "A"},
            ],
        },
        {
            "student_id": 1005,
            "first_name": "Eve",
            "last_name": "Davis",
            "enrollment_year": 2022,
            "major": "Mathematics",
            "courses": [
                {"course_id": "MATH201", "course_name": "Calculus I", "grade": "B"},
                {"course_id": "CS101", "course_name": "Intro to CS", "grade": "A"},
            ],
        },
    ]

    # Insert sample data
    for student in students:
        add_student(db, student)

    # Perform CRUD operations
    print("\nAll Students:")
    for student in get_all_students(db):
        print(student)

    print("\nGet Student by ID (1001):")
    print(get_student_by_id(db, 1001))

    print("\nUpdate Student Major (1001 to 'Data Science'):")
    update_student_major(db, 1001, "Data Science")
    print(get_student_by_id(db, 1001))

    print("\nAdd Course to Student (1001):")
    new_course = {"course_id": "DS201", "course_name": "Data Analysis", "grade": "A"}
    add_course_to_student(db, 1001, new_course)
    print(get_student_by_id(db, 1001))

    print("\nUpdate Student Grade (1001, Course 'CS102' to 'A'):")
    update_student_grade(db, 1001, "CS102", "A")
    print(get_student_by_id(db, 1001))

    print("\nDelete Student (1005):")
    delete_student(db, 1005)
    print(get_all_students(db))

    # Advanced querying
    print("\nStudents Enrolled in 2021:")
    for student in find_students_by_enrollment_year(db, 2021):
        print(student)

    print("\nStudents Majoring in 'Mathematics':")
    for student in find_students_by_major(db, "Mathematics"):
        print(student)

    print("\nStudents Who Received an 'A' Grade:")
    for student in find_students_by_grade(db, "A"):
        print(student)

    print("\nStudents Enrolled in 'CS101':")
    for student in find_students_by_course(db, "CS101"):
        print(student)

    # Aggregation pipelines
    calculate_average_grade_per_course(db)
    count_students_per_major(db)
    find_top_performing_students(db, threshold=3.5)
    analyze_enrollment_trends(db)

    # Clean up
    # db.students.drop()  # (optional)
    # print("\nCollection 'students' dropped.")
    db.client.close()
    print("MongoDB connection closed.")


if __name__ == "__main__":
    main()