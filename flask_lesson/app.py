#Example for Flask app

from flask import Flask, Response

# Create an instance of the Flask class
app: Flask = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello() -> Response:
    return 'Hello, World! This is my first Flask application.'

# Run the application
if __name__ == '__main__':
    app.run(debug=True)