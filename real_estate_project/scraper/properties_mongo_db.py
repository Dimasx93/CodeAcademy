from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from pymongo.errors import OperationFailure, WriteError, ConnectionFailure, DuplicateKeyError, PyMongoError
from schema_validation import validation_rules


# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["aruodas_apartments"]
collection_name = "properties"
collection = db[collection_name]
dblist = client.list_database_names()

# Apply schema validation
existing_collections = db.list_collection_names()
if collection_name in existing_collections:
    db.command(
        "collMod",
        collection_name,
        validator={"$jsonSchema": validation_rules["$jsonSchema"]}
    )
    print(f"Schema validation applied to existing collection '{collection_name}'.")
else:
    db.create_collection(
        collection_name,
        validator={"$jsonSchema": validation_rules["$jsonSchema"]}
    )
    print(f"Collection '{collection_name}' created with schema validation.")

def save_property(property_data):
    #Insert or update property by URL.
    collection.update_one(
        {"url": property_data["url"]},
        {"$set": property_data},
        upsert=True
    )
    # collection.insert_one(property_data)


