from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

new_turtle = Turtle()
new_turtle.hideturtle()
start_pos = -100
count = 0
gap = 50

for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=start_pos + count*gap)
    count += 1
    turtles.append(new_turtle)


race_is_on = False
if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner.")
            else:
                print(f"You lose! The {winning_color} turtle is the winner.")
        rand_distance = random.randint(1,10)
        turtle.forward(rand_distance)



screen.exitonclick()