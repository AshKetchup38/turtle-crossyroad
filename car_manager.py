from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create(self):
        new_car = Turtle("square")
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shapesize(1, 2)
        rand_y = random.randint(-250,250)
        new_car.setposition(300, rand_y)
        self.all_cars.append(new_car)
    
    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT
