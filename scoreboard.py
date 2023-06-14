from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.print_score()

    def print_score(self):
        self.color("black")
        self.setposition(-210, 250)
        self.write(f"Level: {self.level}", False, ALIGNMENT, FONT)

    def print_gameover(self):
        self.color("black")
        self.setposition(0, 0)
        self.write(f"GAME OVER", False, ALIGNMENT, FONT)

    def update_score(self):
        self.level += 1
        self.clear()
        self.print_score()
