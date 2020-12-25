from flask import Flask

# MAC export FLASK_APP=Day_54_Flask.py
# Windows set FLASK_APP=Day_54_Flask.py
# flask run

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "<h1 style=text-align:center>Hello</h1> \
           <p> This is a paragraph</p>"

@app.route('/bye')
def bye():
    return 'bye'

@app.route("/username/<name>")
def greet(name):
    return f"Hello there, {name + 12}!"

if __name__ == "__main__":
    app.run(debug=1)


