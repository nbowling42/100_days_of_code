from random import randint
from turtle import Turtle

class Food:

    def __init__(self):
        self.t = Turtle()
        self.t.color("blue")
        self.t.shape("circle")
        self.t.shapesize(0.75, 0.75, 1)
        x_cor = randint(-430, 430)
        y_cor = randint(-380, 380)
        self.t.teleport(x_cor, y_cor)


    def detect_collision(self, snake_body):
        for snake in snake_body:
            if self.t.distance(snake.turtle) < 21:
                x_cor = randint(-430, 430)
                y_cor = randint(-380, 380)
                self.t.teleport(x_cor, y_cor)
                return True
        return False
