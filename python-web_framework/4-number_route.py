"""Basic flask web server using flask"""
from flask import Flask ,render_template_string

app = Flask(__name__)
#home
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
#first route within a route
@app.route('/hbnb',strict_slashes=False)
def hbnb():
    return "HBNB"
#dynamic routes
@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # Replace underscores with spaces in the text variable
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"
#python parameters
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_python(text="is_cool"):
    formatted_text = text.replace("_", " ")
    return f"Python {formatted_text}"

# n is a number" only if n is an integer
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)