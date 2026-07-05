from turtle import Turtle


class SnakeSegment:

    def __init__(self, turtle_instance):
        self.turtle = turtle_instance
        self.turtle.shape("square")
        self.turtle.penup()
        self.turtle.speed(0)


class Snake:

    def __init__(self):
        self.body = []

    def create_body(self, length):
        x_cord = -21
        for x in range(length):
            clone = SnakeSegment(Turtle())
            clone.turtle.teleport(x_cord, 0)
            self.body.append(clone)
            x_cord -= 21

    def follow(self):
        pass


    def move_forward(self):
        [snake.turtle.forward(10) for snake in self.body]

    def move_backward(self):
        [snake.turtle.backward(10) for snake in self.body]