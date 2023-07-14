from flask import Flask

app = Flask(__name__)

@app.route("/") # python decorator; / denotes home
def hello_world():
    return '<h1 style="text-align:center">Hello!</h1>' \
            '<p>This is a paragraph</p>' \
            '<img src="https://media3.giphy.com/media/b6roFb3iFdoPu/giphy.gif?cid=ecf05e47nypwopdnjxwrurn055p0taotf2h80w9or92xkzma&ep=v1_gifs_search&rid=giphy.gif&ct=g alt="cute black and brown chihuahua in purple sweater smiling">'

def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_emphasized(function):
    def wrapper():
        return f'<em>{function()}</em>'
    return wrapper

def make_underlined(function):
    def wrapper():
        return f'<u>{function()}</u>'
    return wrapper

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasized
@make_underlined
def bye():
    return "Bye"

# Creating variable paths and converting the path to a specified data type
# @app.route("/username/<path:name>")
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"

if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)

# If changes aren't being shown in the webpage, reload site using Ctrl + F5
# or right click webpage, go to 'Inspect' then the 'Network tab' and check 'Disable cache'