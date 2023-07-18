from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import sys

# Create the screen
screen = Screen()
screen.setup(width=800, height = 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Run while player wishes to continue playing
continue_playing = True
while continue_playing:

    # Ask user how many points to score before winning
    points_to_win = int(screen.textinput(title="Play the Pong Game!", prompt="How many points to win?"))

    # Define Turtle objects
    left_paddle = Paddle((-350, 0))
    right_paddle = Paddle((350, 0))
    ball = Ball()
    scoreboard = Scoreboard(points_to_win)

    # Instantiate keyboard inputs
    screen.listen()
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")

    # Run until maximum score to win is reached
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()

        # Detect collision with top or bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.y_bounce()

        # Detect collision with right or left paddle
        if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
            ball.x_bounce()

        # Detect if left paddle scores a point
        if ball.xcor() > 380:
            ball.reset_pos()
            scoreboard.left_point()

        # Detect if right paddle scores a point
        if ball.xcor() < -380:
            ball.reset_pos()
            scoreboard.right_point()

        # Detect winner if first to score 
        if scoreboard.left_score == points_to_win or scoreboard.right_score == points_to_win:
            scoreboard.game_over(points_to_win)
            game_is_on = False

    # Prompt user if they want to play again
    user_plays_again = (screen.textinput(title="Play the Pong Game!", prompt="Play again? Y or N")).lower()
    if user_plays_again == "yes" or user_plays_again == "y":
        screen.reset()
        game_is_on = True
    else:
        sys.exit()
    
screen.exitonclick()
