#Lesson Introduction to Flask         date: 26/03/2025

#Exercise n1 Customizing Flask Application

from flask import Flask, Response

# Create an instance of the Flask class
app: Flask = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/<name>')
def hello(name) -> Response:
    name = "Stefano"
    return f'Hello, {name}! This is my first Flask application.'

@app.route('/about')
def about() -> Response:
    return 'This is about my first Flask application.'

# User profiles data
user_profiles: dict = {
    'john': {'name': 'John Doe', 'email': 'john@example.com', 'bio': 'I am a web developer.'},
    'jane': {'name': 'Jane Smith', 'email': 'jane@example.com', 'bio': 'I love hiking and photography.'}
}

# Product details data
product_details: dict = {
    '1001': {'name': 'Laptop', 'description': 'High-performance laptop', 'price': '$999'},
    '1002': {'name': 'Smartphone', 'description': 'Latest smartphone model', 'price': '$699'}
}

@app.route('/user/<username>')
def user_profile(username: str) -> str:
    if username in user_profiles:
        user_info: dict = user_profiles[username]
        return f'<h1>Welcome, {user_info["name"]}!</h1><p>Email: {user_info["email"]}</p><p>Bio: {user_info["bio"]}</p>'
    else:
        return 'User not found'

@app.route('/product/<product_id>')
def product_info(product_id: str) -> str:
    if product_id in product_details:
        product_info: dict = product_details[product_id]
        return f'<h1>Product: {product_info["name"]}</h1><p>Description: {product_info["description"]}</p><p>Price: {product_info["price"]}</p>'
    else:
        return 'Product not found'

...

# Run the application
if __name__ == '__main__':
    app.run(debug=True)