#Example for Flask app

from flask import Flask, Response, render_template

# Create an instance of the Flask class
app: Flask = Flask(__name__)

posts = [
    {
        'date': '2011-11-11',
        'author': 'Author1',
        'title': 'Title1',
        'content': 'lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum lorem ipsum'
    },
    {
        'date': '2012-10-11',
        'author': 'Author2',
        'title': 'Title2',
        'content': 'test test test test test test test test test test test test test test'
    },
    {
        'date': '2022-05-25',
        'author': 'Author3',
        'title': 'Title3',
        'content': 'content content content content content content content content content content'
    }
]

# Define a route for the root URL ("/")
@app.route('/')
def index() -> Response:
    name = 'Stefano'
    return render_template('index.html', name=name,  posts=posts)


@app.route('/profile')
def profile() -> Response:
    return render_template('profile.html')

# Run the application
if __name__ == '__main__':
    app.run(debug=True)