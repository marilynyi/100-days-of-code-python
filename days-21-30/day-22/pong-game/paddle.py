from turtle import Turtle, Screen


# Create and move a paddle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.clear()
        self.shape("square")
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + 35
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 35
        self.goto(self.xcor(), new_y)




