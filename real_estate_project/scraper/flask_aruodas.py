from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB URI
app.config["MONGO_URI"] = "mongodb://localhost:27017/aruodas_apartments"  # Change as needed

mongo = PyMongo(app)

# Access your MongoDB collection
collection = mongo.db.properties

# Example route to insert data
@app.route('/add_property', methods=['POST'])
def add_property():
    data = request.json
    result = collection.insert_one(data)
    return jsonify({"inserted_id": str(result.inserted_id)}), 201

# Example route to fetch data
@app.route('/properties', methods=['GET'])
def get_properties():
    properties = list(collection.find({}, {"_id": 0}))
    return (properties)

@app.route('/properties/<city>', methods=['GET'])
def get_property_city(city:str):
    # Query MongoDB for properties in the specified city
    properties = list(collection.find({"city": city}, {"_id": 0}))
    return jsonify(properties)

@app.route('/properties/<int:number_of_rooms>', methods=['GET'])
def get_property_rooms(number_of_rooms:int):
    # Query MongoDB for properties in the specified city
    properties = list(collection.find({"number_of_rooms": number_of_rooms}, {"_id": 0}))
    return jsonify(properties)

@app.route('/properties/<float:price_per_m2>', methods=['GET'])
def get_property_price_per_m2(price_per_m2:float):
    # Query MongoDB for properties in the specified city
    # db.student.find({u1: { $gt: 30, $lt: 60}});   #TO USE FOR LATER
    properties = list(collection.find({"price_per_m2": {"$lt" : price_per_m2}}, {"_id": 0}))
    return jsonify(properties)


if __name__ == '__main__':
    app.run(debug=True)
