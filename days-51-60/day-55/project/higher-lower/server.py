import random
import logging
from flask import Flask

logging.basicConfig(level=logging.CRITICAL)

app = Flask(__name__, static_url_path='/static')

# Giphy GIFs
# Counter: https://giphy.com/gifs/counter-z1HdiobjzYIrm
# Dog in toilet: https://giphy.com/gifs/dog-pug-poor-puppy-E9uxGrsyXjnSU
# Astronaut dog: https://giphy.com/gifs/space-9tx0gy37p7oXu
# Smiling dog: https://giphy.com/gifs/chihuahua-b6roFb3iFdoPu

@app.route("/")
def counter():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="/static/giphy.gif" alt="calendar style counter from 0 to 9">'

random_number = random.randint(0,9)
logging.critical(f"{random_number=}")
           
@app.route("/<int:guess>")
def number(guess):
    if guess < random_number:
        return f'<h1 style="color: red">Too low, try again!</h1>'\
                '<img src="/static/too_low.gif" alt="pug stuck in toilet" width=400>'
    elif guess > random_number:
        return f'<h1 style="color: purple">Too high, try again!</h1>' \
                '<img src="/static/too_high.gif" alt="astronaut dog floating inside space shuttle" width=600>'
    else:
        return f'<h1 style="color: green">You found me!</h1>' \
                '<img src="/static/just_right.gif" alt="cute smiling black and brown chihuahua in purple sweater" width=400>'
        
if __name__ == "__main__":
    app.run(debug=False)
    
