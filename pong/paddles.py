from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=4)
        self.color("white")
        self.shape("square")
        self.setheading(90)