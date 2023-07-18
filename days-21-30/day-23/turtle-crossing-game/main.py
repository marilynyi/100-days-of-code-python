import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Create the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")
screen.tracer(0)

# Define the Turtle objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Instantiate keyboard inputs
screen.listen()
screen.onkey(player.up, "w")

# Run while turtle doesn't hit a car
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful crossing
    if player.at_finish_line():
        player.go_to_start()
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        

screen.exitonclick()