# Lesson MongoDB Querying                                 date 27/02/2025

#Exercise n1 Querying Store Product Information

from datetime import datetime

from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["storeDB"]
collection = db["sales"]


# Insert sample data (if not already inserted)
def insert_sample_data():
    sample_data = [
        {
            "product": "Laptop",
            "brand": "Dell",
            "price": 1200,
            "quantity": 15,
            "category": ["Electronics", "Computers"],
            "sales_date": datetime(2024, 11, 10),
            "rating": 4.5,
        },
        {
            "product": "Smartphone",
            "brand": "Samsung",
            "price": 800,
            "quantity": 30,
            "category": ["Electronics", "Mobile"],
            "sales_date": datetime(2024, 10, 5),
            "rating": 4.7,
        },
        {
            "product": "Headphones",
            "brand": "Sony",
            "price": 150,
            "quantity": 50,
            "category": ["Electronics", "Audio"],
            "sales_date": datetime(2024, 11, 15),
            "rating": 4.2,
        },
        {
            "product": "Coffee Maker",
            "brand": "Keurig",
            "price": 100,
            "quantity": 20,
            "category": ["Appliances", "Kitchen"],
            "sales_date": datetime(2024, 9, 12),
            "rating": 4.0,
        },
        {
            "product": "Electric Kettle",
            "brand": "Philips",
            "price": 40,
            "quantity": 40,
            "category": ["Appliances", "Kitchen"],
            "sales_date": datetime(2024, 8, 20),
            "rating": 3.8,
        },
    ]
    collection.insert_many(sample_data)


# Queries
def products_with_specific_rating(rating):
    return list(collection.find({"rating": {"$eq": rating}}))


def products_from_specific_brands(brands):
    return list(collection.find({"brand": {"$in": brands}}))


def products_not_in_category(excluded_category):
    return list(collection.find({"category": {"$ne": excluded_category}}))


def electronics_excluding_mobile():
    return list(
        collection.find({"category": {"$in": ["Electronics"], "$nin": ["Mobile"]}})
    )


def sold_since_and_high_rating(date, min_rating):
    return list(
        collection.find(
            {
                "sales_date": {"$gte": date},
                "rating": {"$gt": min_rating},
            }
        )
    )


def priced_between_exclude_quantity(min_price, max_price):
    return list(
        collection.find(
            {"price": {"$gte": min_price, "$lte": max_price}},
            {"quantity": 0},
        )
    )


def exclude_brands(brands):
    return list(collection.find({"brand": {"$nin": brands}}))


def expensive_products(min_price):
    return list(
        collection.find(
            {"price": {"$gt": min_price}},
            {"_id": 0, "product": 1, "price": 1},
        )
    )


# Example usage
if __name__ == "__main__":
    insert_sample_data()

    print("1. Products with a rating of 4.5:")
    print(products_with_specific_rating(4.5))

    print("2. Products from Samsung or Sony brands:")
    print(products_from_specific_brands(["Samsung", "Sony"]))

    print("3. Products not in the Appliances category:")
    print(products_not_in_category("Appliances"))

    print("4. Electronics excluding Mobile:")
    print(electronics_excluding_mobile())

    print("5. Sold since 2024-10-01 with rating > 4.0:")
    print(sold_since_and_high_rating(datetime(2024, 10, 1), 4.0))

    print("6. Priced between $50 and $1000, excluding quantity:")
    print(priced_between_exclude_quantity(50, 1000))

    print("7. Products excluding Keurig and Philips brands:")
    print(exclude_brands(["Keurig", "Philips"]))

    print("8. Products priced above $1000 (name and price only):")
    print(expensive_products(1000))