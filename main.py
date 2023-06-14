import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
count = 0

turtle = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    cars.move()
    count+=1
    time.sleep(0.1)
    screen.update()
    if count % 6 == 0:
        cars.create()
        cars.move()
    for car in cars.all_cars:
        if car.distance(turtle) < 25:
            game_is_on = False
            scoreboard.print_gameover()
    if turtle.ycor() > 280:
        scoreboard.update_score()
        turtle.start()
        cars.increase_speed()

screen.exitonclick()
