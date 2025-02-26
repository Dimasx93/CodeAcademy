from datetime import datetime

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from bson.objectid import ObjectId


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def get_database_collection(database: Database, collection_name: str) -> Collection:
    collection = database[collection_name]
    return collection


def list_databases(client: MongoClient) -> list[str]:
    return client.list_database_names()


def list_collections(database: Database) -> list[str]:
    return database.list_collection_names()

def insert_document(collection: Collection, document: dict) -> str:
    result = collection.insert_one(document)
    return str(result.inserted_id)

def find_documents(collection: Collection, query: dict) -> list[dict]:
    documents = collection.find(query)
    return list(documents)

def update_document(collection: Collection, query: dict, update: dict) -> int:
    result = collection.update_many(query, {"$set": update})
    return result.modified_count

def delete_documents(collection: Collection, query: dict) -> int:
    result = collection.delete_many(query)
    return result.deleted_count

# Example usage
if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "blogDB"
    collection_name = "posts"

    # Connect to MongoDB
    client = MongoClient(mongodb_host, mongodb_port)
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    # Retrieve a specific collection
    collection = get_database_collection(db, collection_name)
    print(f"Retrieved collection: {collection_name}")

    # document = {
    #     "title": "Understanding MongoDB Aggregation",
    #     "content": "Aggregation in MongoDB allows you to process and transform data "
    #     "effectively...",
    #     "author": {"name": "Alice Johnson", "email": "alicejohnson@example.com"},
    #     "tags": ["MongoDB", "Aggregation", "Data Processing"],
    #     "createdAt": datetime(2024, 10, 15, 8, 45, 0),
    #     "updatedAt": datetime(2024, 10, 16, 14, 20, 0),
    # }
    #
    # inserted_id = insert_document(collection, document)
    # print(f"Inserted document with ID: {inserted_id}")


    # Update Operation
    # query = {"title": "Understanding MongoDB Aggregation"}
    # update = {"updatedAt": datetime.now(), "author.name": "Steponas Ponas"}   #just to change the name
    # modified_count = update_document(collection, query, update)
    # print(f"Modified {modified_count} document(s)")

    # Delete Operation
    query = {"_id": ObjectId("67bf4f14ac117144f7efddbe")}
    deleted_count = delete_documents(collection, query)
    print(f"Deleted {deleted_count} document(s)")

    # Read (Query) Operation
    query = {"title": "Understanding MongoDB Aggregation"}
    results = find_documents(collection, query)
    print("Matching documents:")
    for result in results:
        print(result)

    # List all databases
    databases = list_databases(client)
    print("List of databases:")
    for db_name in databases:
        print(f"- {db_name}")

    # List collections in the connected database
    collections = list_collections(db)
    print("Collections in the connected database:")
    for collection_name in collections:
        print(f"- {collection_name}")


# Output:
# -------
# Retrieved collection: posts
# List of databases:
# - admin
# - blogDB
# - config
# - local
# Collections in the connected database:
# - posts