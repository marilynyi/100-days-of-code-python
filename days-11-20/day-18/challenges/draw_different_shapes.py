from turtle import Turtle, Screen

tim = Turtle()

# degrees = 180 * (sides - 2) / sides
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple", "pink"]

for i in range(3,11):
    degrees = 180 * (i - 2) / i
    color = colors[i-3]
    for j in range(0,i):
        tim.color(color)
        tim.right(180 - degrees)
        tim.forward(100)



screen = Screen()
screen.exitonclick()