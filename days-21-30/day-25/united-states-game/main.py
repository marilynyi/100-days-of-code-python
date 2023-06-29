from turtle import Turtle, Screen
import pandas as pd

image = Turtle()
screen = Screen()
screen.title("Name the States")

image_link = "blank_states_img.gif"
screen.addshape(image_link)
image.shape(image_link)

data = pd.read_csv("50_states.csv")
coordinates = pd.DataFrame(data)

all_states = data["state"].to_list()

guessed_states = []
missing_states = []
while len(guessed_states)< 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="Name a state: ").title()

    if answer_state == "Exit":
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        missing_states = pd.DataFrame(missing_states)
        missing_states.to_csv("missing_states.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        state_data = coordinates[coordinates["state"] == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        turtle = Turtle()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x, y)
        turtle.write(answer_state)


screen.exitonclick()