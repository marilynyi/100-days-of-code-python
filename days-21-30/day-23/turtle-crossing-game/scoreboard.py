from turtle import Turtle

FONT_SCOREBOARD = ("Courier", 24, "normal")
FONT_GAME_OVER = ("Courier", 44, "normal")
X_POS = -250
Y_POS = 250

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(X_POS, Y_POS)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.level}", font = FONT_SCOREBOARD)

    def increase_score(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align = "center", font = FONT_GAME_OVER)



