# Lesson MongoDB Schema validation                                 date 27/02/2025

#Exercise n1 Valid Customers Only

from pymongo import MongoClient
from pymongo.errors import CollectionInvalid, OperationFailure, WriteError


def main():
    # Connect to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    print("Connected to MongoDB on localhost.")

    # Create database and collection
    db = client["shopDB"]
    collection_name = "customers"

    # Define the schema validation rules
    validation_rules = {
        "validator": {
            "$jsonSchema": {
                "bsonType": "object",
                "required": ["name", "age", "email", "address"],
                "properties": {
                    "name": {
                        "bsonType": "string",
                        "description": "'name' must be a string and is required.",
                    },
                    "age": {
                        "bsonType": "int",
                        "minimum": 18,
                        "maximum": 99,
                        "description": "'age' must be an integer between 18 and 99 and is required.",
                    },
                    "email": {
                        "bsonType": "string",
                        "pattern": "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$",
                        "description": "'email' must be a valid email address and is required.",
                    },
                    "address": {
                        "bsonType": "object",
                        "required": ["street", "city", "postal_code"],
                        "properties": {
                            "street": {
                                "bsonType": "string",
                                "description": "'street' must be a string and is required.",
                            },
                            "city": {
                                "bsonType": "string",
                                "description": "'city' must be a string and is required.",
                            },
                            "postal_code": {
                                "bsonType": "string",
                                "description": "'postal_code' must be a string and is required.",
                            },
                        },
                        "description": "'address' must be an object and is required.",
                    },
                },
            }
        }
    }

    # Create the collection with validation rules
    try:
        collection = db.create_collection(
            collection_name, validator=validation_rules["validator"]
        )
        print(f"Collection '{collection_name}' created with schema validation.")
    except CollectionInvalid:
        collection = db[collection_name]
        print(f"Collection '{collection_name}' already exists.")
        # Apply validation rules to existing collection
        try:
            db.command(
                "collMod", collection_name, validator=validation_rules["validator"]
            )
            print(
                f"Schema validation applied to existing collection '{collection_name}'."
            )
        except OperationFailure as e:
            print(f"Failed to apply schema validation: {e}")

    # Insert a valid document
    valid_document = {
        "name": "Alice Johnson",
        "age": 30,
        "email": "alice.johnson@example.com",
        "address": {
            "street": "123 Maple Street",
            "city": "Springfield",
            "postal_code": "12345",
        },
    }

    try:
        collection.insert_one(valid_document)
        print("Valid document inserted successfully.")
    except WriteError as e:
        print(f"Error inserting valid document: {e.details['errmsg']}")

    # Insert an invalid document (missing required fields)
    invalid_document_1 = {
        "name": "Bob Smith",
        "age": 25,
        # Missing 'email' and 'address'
    }

    try:
        collection.insert_one(invalid_document_1)
    except WriteError as e:
        print(f"Error inserting invalid document 1: {e.details['errmsg']}")

    # Insert an invalid document (incorrect data types and values)
    invalid_document_2 = {
        "name": "Carol Williams",
        "age": 17,  # Age below minimum
        "email": "carol.williams[at]example.com",  # Invalid email format
        "address": {
            "street": 456,  # Should be a string
            "city": True,  # Should be a string
            "postal_code": None,  # Should be a string
        },
    }

    try:
        collection.insert_one(invalid_document_2)
    except WriteError as e:
        print(f"Error inserting invalid document 2: {e.details['errmsg']}")

    # Print all documents in the collection
    print("\nDocuments in the 'customers' collection:")
    for doc in collection.find():
        print(doc)

    # Close the MongoDB connection
    client.close()


if __name__ == "__main__":
    main()
