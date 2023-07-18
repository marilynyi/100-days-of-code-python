from flask import Flask
import random

app = Flask(__name__)

# print(__name__)
# print(random.__name__)

@app.route("/") # python decorator; / denotes home
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://media3.giphy.com/media/b6roFb3iFdoPu/giphy.gif?cid=ecf05e47nypwopdnjxwrurn055p0taotf2h80w9or92xkzma&ep=v1_gifs_search&rid=giphy.gif&ct=g alt="cute black and brown chihuahua in purple sweater smiling">'

# Different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "Bye"

# Creating variable paths and converting the path to a specified data type
# @app.route("/username/<path:name>")
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)



# on Mac, type 'export FLASK_APP=hello.py' in terminal
# on Windows, type 'set FLASK_APP=hello.py' in terminal

# then 'flask run'
# pip install python-dotenv to bypass having to type above cmd every time
