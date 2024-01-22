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
@app.route('/python/<text>')
def display_python():
    text = "is_cool"
    formatted_text = text.replace("_", " ")
    message = f"Python {formatted_text}"
    return render_template_string(message)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)