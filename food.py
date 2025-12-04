import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("purple")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.refresh()

    def refresh(self):
        """Moves the food to a random position on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)