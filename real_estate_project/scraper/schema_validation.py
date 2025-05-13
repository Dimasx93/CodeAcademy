# Define schema validation rules
validation_rules = {
    "$jsonSchema": {
        "bsonType": "object",
        "required": ["city", "district", "street", "price", "price_per_m2", "number_of_rooms"],
        "properties": {
            "city": {
                "bsonType": "string",
                "description": "'city' must be a string and is required."
            },
            "district": {
                "bsonType": "string",
                "description": "'district' must be a string and is required."
            },
            "street": {
                "bsonType": "string",
                "description": "'street' must be a string and is required."
            },
            "price": {
                "bsonType": "double",
                "description": f"'price' must be a string and is required."
            },
            "price_per_m2": {
                "bsonType": "int",
                "description": f"'price_per_m2' must be a string and is required."
            },

            "number_of_rooms": {
                "bsonType": "int",
                "description": f"'price_per_m2' must be a string and is required."
            },
            "size_m2": {
                "bsonType": "double",
                "description": f"'price_per_m2' must be a string and is required."
            }
        }
    }
}
