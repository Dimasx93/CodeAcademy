# Exercise: Tracking Urban Beekeeping Operations 🐝
# Step 1: SQLAlchemy Implementation
# from datetime import datetime, date
#
# from sqlalchemy import Column, Date, Float, Integer, String, create_engine, ForeignKey
# from sqlalchemy.orm import declarative_base, sessionmaker, relationship
#
# engine = create_engine("sqlite:///beekeeping.db")
# Base = declarative_base()
#
#
# class Beekeeper(Base):
#     __tablename__ = "beekeeper"
#     id = Column(Integer, primary_key=True)
#     name = Column("name", String)
#     email = Column("email", String)
#     experience_level = Column("experience_level", String)
#
#     beehives = relationship("Beehive", back_populates="beekeeper")
#
#     def __repr__(self):
#         return f"{self.name}, {self.email}, {self.experience_level}"
#
# class Beehive(Base):
#     __tablename__ = "beehive"
#     id = Column(Integer, primary_key=True)
#     location = Column("location", String)
#     beekeeper_id = Column(Integer, ForeignKey("beekeeper.id"))
#     honey_produced = Column("honey_produced", Float)
#     bee_species = Column("bee_species", String)
#
#     inspections = relationship("Inspection", back_populates="beehive")
#     beekeeper = relationship("Beekeeper", back_populates="beehives")
#
#     def __repr__(self):
#         return (f"{self.id}, {self.location}, beekeeper: {self.beekeeper},"
#                 f" honey produced: {self.honey_produced}, bee species {self.bee_species}")
#
# class Inspection(Base):
#     __tablename__ = "inspection"
#     id = Column(Integer, primary_key=True)
#     beehive_id = Column(Integer, ForeignKey("beehive.id"))
#     date = Column("date", Date, default=datetime.today())
#     health_status = Column("health_status", String)
#     notes = Column("notes", String)
#
#
#     beehive = relationship("Beehive", back_populates="inspections")
#
#     def __repr__(self):
#         return f"{self.date}, {self.health_status}, {self.notes}"
#
# if __name__ == "__main__":
#
#     Base.metadata.create_all(engine)
#
#     Session = sessionmaker(bind=engine)
#     session = Session()
#
#     beekeepers = [Beekeeper(id=1, name="Alice Johnson", email="alice@example.com", experience_level="Expert"),
#                   Beekeeper(id=2, name="Bob Smith", email="bob@example.com", experience_level="Intermediate"),
#                   Beekeeper(id=3, name="Charlie Davis", email="charlie@example.com", experience_level="Beginner"), ]
#     beehives = [Beehive(id=1, location="Central Park", beekeeper_id=1, honey_produced=12.5, bee_species="Apis mellifera"),
#                 Beehive(id=2, location="Brooklyn Botanical Garden", beekeeper_id=1, honey_produced=8.2,
#                         bee_species="Bombus terrestris"),
#                 Beehive(id=3, location="Downtown Rooftop", beekeeper_id=2, honey_produced=15.0,
#                         bee_species="Apis mellifera"),
#                 Beehive(id=4, location="Suburban Farm", beekeeper_id=2, honey_produced=5.5, bee_species="Apis dorsata"),
#                 Beehive(id=5, location="City Park", beekeeper_id=3, honey_produced=20.0, bee_species="Apis cerana"), ]
#     inspections = [
#         Inspection(id=1, beehive_id=1, date=date(2024, 2, 10), health_status="Healthy", notes="Good honey flow observed"),
#         Inspection(id=2, beehive_id=1, date=date(2024, 2, 25), health_status="Colony Collapse Disorder",
#                    notes="Bees mysteriously disappeared"),
#         Inspection(id=3, beehive_id=2, date=date(2024, 2, 15), health_status="Weak", notes="Small hive population"),
#         Inspection(id=4, beehive_id=3, date=date(2024, 2, 18), health_status="Healthy", notes="Hive is thriving"),
#         Inspection(id=5, beehive_id=4, date=date(2024, 2, 22), health_status="Healthy", notes="Strong brood patterns"),
#         Inspection(id=6, beehive_id=5, date=date(2024, 2, 28), health_status="Colony Collapse Disorder",
#                    notes="No bees present in hive"),
#         Inspection(id=7, beehive_id=5, date=date(2024, 3, 1), health_status="Weak",
#                    notes="Remaining bees are struggling"), ]
#
#     # session.add_all(beekeepers)
#     # session.add_all(beehives)
#     # session.add_all(inspections)
#     # session.commit()
#
#     beekeeper = session.get(Beekeeper, 2)
#     print(beekeeper.beehives)
#
#     # beehive = session.query(Beehive).filter(Beehive.honey_produced > 10)
#     # print(list(beehive))
#
#     # list_of_inspections = session.query(Inspection).filter(Inspection.health_status == "Colony Collapse Disorder")
#     # print(list(list_of_inspections))
#
#     session.close()

# Tasks for MongoDB

# Implement the equivalent MongoDB collections.
# Write scripts to:
# Insert sample data.
# Find all beehives for a specific beekeeper.
# Retrieve beehives that produced more than 10 kg of honey.
# Find inspections with a "Colony Collapse Disorder" status.

from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from datetime import datetime

from bson import ObjectId


def connect_to_mongodb(host: str, port: int, db_name: str) -> Database:
    client = MongoClient(host, port)
    database = client[db_name]
    return database


def insert_document(collection: Collection, document) -> str:
    result = collection.insert_many(document)
    return str(result.inserted_ids)


def find_documents(collection: Collection, query: dict) -> list[dict]:
    documents = collection.find(query)
    return list(documents)


def get_database_collection(database: Database, collection_name: str) -> Collection:
    collection = database[collection_name]
    return collection

def find_beehives_by_beekeeper(collection: Collection, beekeeper_id: dict):
    return list(collection.find(beekeeper_id))

def find_beehives_producing_more_than(collection: Collection, min_honey: dict):
    return list(collection.find(min_honey))

def find_colony_collapse_inspections(collection: Collection, colony_situation: dict):
    return list(collection.find(colony_situation))


if __name__ == "__main__":
    # Connection details
    mongodb_host = "localhost"
    mongodb_port = 27017
    database_name = "beekeepingDB"
    collection_name = "beekeeping"

    client = MongoClient(mongodb_host, mongodb_port)
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)

    collection = get_database_collection(db, collection_name)
    print(f"Retrieved collection: {collection_name}")

    beekeepers = [
        {"_id": ObjectId("65a7d7b8f3a9f4b2c6a8e1a1"), "name": "Alice Johnson", "email": "alice@example.com", "experience_level": "Expert"},
        {"_id": ObjectId("65a7d7b8f3a9f4b2c6a8e1a2"), "name": "Bob Smith", "email": "bob@example.com", "experience_level": "Intermediate"},
        {"_id": ObjectId("65a7d7b8f3a9f4b2c6a8e1a3"), "name": "Charlie Davis", "email": "charlie@example.com", "experience_level": "Beginner"},
    ]
    beehives = [
        {"_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a1"), "location": "Central Park", "beekeeper_id": ObjectId("65a7d7b8f3a9f4b2c6a8e1a1"), "honey_produced": 12.5, "bee_species": "Apis mellifera"},
        {"_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a2"), "location": "Downtown Rooftop", "beekeeper_id": ObjectId("65a7d7b8f3a9f4b2c6a8e1a2"), "honey_produced": 15.0, "bee_species": "Apis mellifera"},
    ]
    inspections = [
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a1"), "date": datetime(2024, 2, 10),
         "health_status": "Healthy", "notes": "Good honey flow observed"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a1"), "date": datetime(2024, 2, 25),
         "health_status": "Colony Collapse Disorder", "notes": "Bees mysteriously disappeared"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a2"), "date": datetime(2024, 2, 18),
         "health_status": "Healthy", "notes": "Hive is thriving"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a3"), "date": datetime(2024, 3, 7),
         "health_status": "Weak", "notes": "Signs of mite infestation"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a4"), "date": datetime(2024, 3, 9),
         "health_status": "Healthy", "notes": "Pollen stores look good"},
        {"date": datetime(2024, 2, 18), "health_status": "Healthy", "notes": "Hive is thriving"},
        {"date": datetime(2024, 3, 7), "health_status": "Weak", "notes": "Signs of mite infestation"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a1"), "date": datetime(2024, 2, 10),
         "health_status": "Healthy", "notes": "Good honey flow observed"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a1"), "date": datetime(2024, 2, 25),
         "health_status": "Colony Collapse Disorder", "notes": "Bees mysteriously disappeared"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a2"), "date": datetime(2024, 2, 15),
         "health_status": "Weak", "notes": "Small hive population"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a3"), "date": datetime(2024, 2, 18),
         "health_status": "Healthy", "notes": "Hive is thriving"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a4"), "date": datetime(2024, 2, 22),
         "health_status": "Healthy", "notes": "Strong brood patterns"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a5"), "date": datetime(2024, 2, 28),
         "health_status": "Colony Collapse Disorder", "notes": "No bees present in hive"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a5"), "date": datetime(2024, 3, 1),
         "health_status": "Weak", "notes": "Remaining bees are struggling"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a2"), "date": datetime(2024, 3, 5),
         "health_status": "Healthy", "notes": "Queen laying well"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a3"), "date": datetime(2024, 3, 7),
         "health_status": "Weak", "notes": "Signs of mite infestation"},
        {"_id": ObjectId(), "beehive_id": ObjectId("65a7d7b8f3a9f4b2c6a8e2a4"), "date": datetime(2024, 3, 9),
         "health_status": "Healthy", "notes": "Pollen stores look good"}
    ]

    # inserted_beekeepers = insert_document(collection, beekeepers)
    # print(f"Inserted Beekeepers: {inserted_beekeepers}")
    #
    # inserted_beehives = insert_document(collection, beehives)
    # print(f"Inserted Beehives: {inserted_beehives}")
    #
    # inserted_inspections = insert_document(collection, inspections)
    # print(f"Inserted Inspections: {inserted_inspections}")

    beekeeper_id_to_search = {"beekeeper_id" : ObjectId("65a7d7b8f3a9f4b2c6a8e1a1")}  # Alice Johnson
    print("\n🐝 Beehives for Alice Johnson:")
    print(find_beehives_by_beekeeper(collection, beekeeper_id_to_search))

    honey_minimum = {"honey_produced" : {"$gt" : 10}}
    print("\n🍯 Beehives producing more than 10 kg of honey:")
    print(find_beehives_producing_more_than(collection, honey_minimum))

    colony_situation = {"health_status":"Colony Collapse Disorder"}
    print("\n⚠️ Inspections with 'Colony Collapse Disorder':")
    print(find_colony_collapse_inspections(collection, colony_situation))
