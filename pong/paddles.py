from turtle import Turtle

class Paddle:
    
    def __init__(self):
        self.t = Turtle()
        self.t.color("white")
        self.t.shape("square")
        self.t.shapesize(stretch_len=4)
        self.t.setheading(90)
        self.t.penup()


    def move_up(self):
        self.t.forward(20)


    def move_down(self):
        self.t.backward(20)