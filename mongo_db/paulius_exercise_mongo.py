#MongoDB Practice Exercise: Movie Database with Schema Validation

from pymongo import MongoClient, errors as pymongo_errors
from datetime import datetime


class MovieDatabase:
    def __init__(self, host: str, port: int, db_name: str, collection_name: str):
        try:
            self.client = MongoClient(host, port, serverSelectionTimeoutMS=5000)
            self.db = self.client[db_name]

            current_year = datetime.now().year  # Get the current year dynamically

            # Define schema validation rules
            validation_rules = {
                "$jsonSchema": {
                    "bsonType": "object",
                    "required": ["title", "year", "genre", "director", "actors"],
                    "properties": {
                        "title": {
                            "bsonType": "string",
                            "description": "'title' must be a string and is required."
                        },
                        "year": {
                            "bsonType": "int",
                            "minimum": 1900,
                            "maximum": current_year,
                            "description": f"'year' must be an int between 1900 and {current_year}."
                        },
                        "genre": {
                            "bsonType": "array",
                            "items": {
                                "bsonType": "string"
                            },
                            "description": "'genre' must be an array of strings and is required."
                        },
                        "director": {
                            "bsonType": "object",
                            "required": ["name"],
                            "properties": {
                                "name": {
                                    "bsonType": "string",
                                    "description": "'name' must be a string and is required."
                                },
                                "birthYear": {
                                    "bsonType": "int",
                                    "minimum": 1900,
                                    "description": "'birthYear' must be an int greater than 1900."
                                }
                            }
                        },
                        "actors": {
                            "bsonType": "array",
                            "description": "'actors' must be an array of objects, each containing 'name' and optionally 'age'.",
                            "items": {
                                "bsonType": "object",
                                "required": ["name"],
                                "properties": {
                                    "name": {
                                        "bsonType": "string",
                                        "description": "'name' must be a string and is required."
                                    },
                                    "age": {
                                        "bsonType": "int",
                                        "minimum": 1,
                                        "description": "'age' must be an int bigger than 0."
                                    }
                                }
                            }
                        },
                        "rating": {
                            "bsonType": "double",
                            "minimum": 0,
                            "maximum": 10,
                            "description": "'rating' must be a number between 0 and 10."
                        }
                    }
                }
            }

            existing_collections = self.db.list_collection_names()
            if collection_name in existing_collections:
                self.db.command(
                    "collMod",
                    collection_name,
                    validator={"$jsonSchema": validation_rules["$jsonSchema"]}
                )
                print(f"Schema validation applied to existing collection '{collection_name}'.")
            else:
                self.collection = self.db.create_collection(
                    collection_name,
                    validator={"$jsonSchema": validation_rules["$jsonSchema"]}
                )
                print(f"Collection '{collection_name}' created with schema validation.")

            self.collection = self.db[collection_name]
            self.client.admin.command("ping")
            print("Connected to MongoDB successfully.")
        except pymongo_errors.ConnectionFailure as e:
            print(f"Connection failure: {e}")
            raise
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred during initialization: {e}")
            raise

    def add_movies(self, movies):
        try:
            result = self.collection.insert_many(movies)
            return [str(id) for id in result.inserted_ids]
        except pymongo_errors.DuplicateKeyError as e:
            print(f"Duplicate key error: {e}")
            return []
        except pymongo_errors.WriteError as e:
            print(f"Write error (validation failed): {e.details['errmsg']}")
            return []
        except pymongo_errors.PyMongoError as e:
            print(f"An error occurred while adding movies: {e}")
            return []


# Connection details
mongodb_host = "localhost"
mongodb_port = 27017
database_name = "movieDB"
collection_name = "movies"

# Connect to MongoDB
client = MongoClient(mongodb_host, mongodb_port)
db = client[database_name]
collection = db[collection_name]


# Function to insert movies
def insert_movies():
    new_movies = [
        {
            "title": "Inception",
            "year": 2010,
            "genre": ["Sci-Fi", "Action"],
            "director": {
                "name": "Christopher Nolan",
                "birthYear": 1970
            },
            "actors": [
                {"name": "Leonardo DiCaprio", "age": 49},
                {"name": "Joseph Gordon-Levitt", "age": 42}
            ],
            "rating": 8.8
        },
        {
            "title": "The Dark Knight",
            "year": 2008,
            "genre": ["Action", "Crime"],
            "director": {
                "name": "Christopher Nolan",
                "birthYear": 1970
            },
            "actors": [
                {"name": "Christian Bale", "age": 50},
                {"name": "Heath Ledger", "age": 28}
            ],
            "rating": 9.0
        }
    ]

    result = collection.insert_many(new_movies)
    print(f"Inserted movie IDs: {result.inserted_ids}")


# Query functions
def find_movies_after_2005():
    return list(collection.find({"year": {"$gt": 2005}}, {"_id": 0}))


def find_movies_by_genre(genre):
    return list(collection.find({"genre": {"$in": [genre]}}, {"_id": 0}))


def find_movies_by_director(director_name):
    return list(collection.find({"director.name": {"$eq": director_name}}, {"_id": 0}))


def find_movies_with_rating_above(min_rating):
    return list(collection.find({"rating": {"$gt": min_rating}}, {"_id": 0}))


def list_actors_in_movie(movie_title):
    result = collection.find_one({"title": {"$eq": movie_title}}, {"actors": 1, "_id": 0})
    return result.get("actors", []) if result else []


def find_movies_with_actor_younger_than(max_age):
    return list(collection.find({"actors.age": {"$lt": max_age}}, {"_id": 0}))


def update_movie_rating(movie_title, new_rating):
    result = collection.update_one({"title": {"$eq": movie_title}}, {"$set": {"rating": new_rating}})
    return result.modified_count > 0


def delete_movies_before_2000():
    result = collection.delete_many({"year": {"$lt": 2000}})
    return result.deleted_count


# Execute functions
try:
    # Insert movies (Only run once, otherwise it will duplicate entries)
    #insert_movies()

    print("Movies after 2005:", find_movies_after_2005())
    print("Action movies:", find_movies_by_genre("Action"))
    print("Movies directed by Christopher Nolan:", find_movies_by_director("Christopher Nolan"))
    print("Movies with rating > 8.5:", find_movies_with_rating_above(8.5))
    print("Actors in Inception:", list_actors_in_movie("Inception"))
    print("Movies with actors younger than 30:", find_movies_with_actor_younger_than(30))

    if update_movie_rating("The Dark Knight", 9.1):
        print("Updated rating of The Dark Knight successfully!")

    deleted_count = delete_movies_before_2000()
    print(f"Deleted {deleted_count} movies released before 2000.")

except Exception as e:
    print(f"Error: {e}")






