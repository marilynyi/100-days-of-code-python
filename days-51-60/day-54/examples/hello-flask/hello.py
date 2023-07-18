from flask import Flask
import random

app = Flask(__name__)

# print(__name__)
# print(random.__name__)

@app.route("/") # python decorator; / denotes home
def hello_world():
    return "Hello, World!"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()



# on Mac, type 'export FLASK_APP=hello.py' in terminal
# on Windows, type 'set FLASK_APP=hello.py' in terminal

# then 'flask run'
# pip install python-dotenv to bypass having to type above cmd every time
