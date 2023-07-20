from turtle import Turtle

ALIGN_SCORE = "center"
LEFT_SCORE_POS = (-200, 230)
RIGHT_SCORE_POS = (200, 230)
FONT_SCOREBOARD = ("Courier", 54, "normal")
FONT_GAME_OVER = ("Courier", 34, "normal")
    
class Scoreboard(Turtle):
    def __init__(self, points_to_win):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.max_points = points_to_win
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(LEFT_SCORE_POS)
        self.write(f"{self.left_score}", align=ALIGN_SCORE,font = FONT_SCOREBOARD)
        self.goto(RIGHT_SCORE_POS)
        self.write(f"{self.right_score}", align=ALIGN_SCORE,font = FONT_SCOREBOARD)
 
    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self, points_to_win):
        if self.left_score == points_to_win:
            winner = "Left paddle"
        elif self.right_score == points_to_win:
            winner = "Right paddle"
        self.goto(0,100)
        self.write(f"{winner} has won!", align=ALIGN_SCORE,font = FONT_GAME_OVER)
    
