from turtle import Turtle

ALIGN_SCORE = "center"
FONT = ("Courier", 24, "normal")
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as highest_score:
            self.high_score = int(highest_score.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN_SCORE,font = FONT)
        self.hideturtle()
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN_SCORE,font = FONT)
 
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highest_score.txt", "w") as highest_score:
                highest_score.write(f"{self.high_score}")
        self.score = 0   
        self.update_scoreboard()
