from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("classic")
tim.pensize(10)
tim.speed("fastest")

colors = [
    "rosybrown", 
    "slategray", 
    "wheat2", 
    "salmon1", 
    "seagreen4", 
    "thistle", 
    "skyblue", 
    "yellow3", 
    "tan1", 
    "violet"
]

angles = [-90, 0, 90, 180]

for i in range(300):
    if i % 10 == 0:
        count = 0
    tim.color(colors[count])
    tim.forward(25)
    tim.setheading(random.choice(angles))
    count += 1

    
screen = Screen()
screen.exitonclick()