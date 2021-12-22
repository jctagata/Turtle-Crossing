import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Class Instantiation
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen Listener
screen.listen()
screen.onkey(player.go_up, "Up")

# Set Game is On
game_is_on = True

# Run Game
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Create Car
    car_manager.create_car()

    # Move Cars
    car_manager.move_cars()

    # Detect Car Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Successful Crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()

# Preserve Screen
screen.exitonclick()
