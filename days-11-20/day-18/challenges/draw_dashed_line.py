from turtle import Turtle, Screen

tim = Turtle()
tim.color("seagreen3")
tim.shape("turtle")

for _ in range(50):
    tim.forward(5)
    tim.up()
    tim.forward(5)
    tim.down()


screen = Screen()
screen.exitonclick()