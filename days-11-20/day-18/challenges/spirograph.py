from turtle import Turtle, Screen
import turtle as t
import random

tim = Turtle()
tim.shape("turtle")
t.colormode(255)
tim.speed("fastest")

def color_code():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

gap_size = 2
for _ in range(int(360 / gap_size)):
    tim.color(color_code())
    tim.circle(100)
    tim.setheading(tim.heading() + gap_size)


screen = Screen()
screen.exitonclick()