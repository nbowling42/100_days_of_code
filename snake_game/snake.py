from turtle import Turtle


class SnakeSegment:
    """ A class representing a segment of the snake's body. Each segment is represented by a turtle instance."""
    def __init__(self):
        self.turtle = Turtle()
        self.turtle.shape("square")
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.speed(1)
    

class Snake:
    """ A class representing the snake. The snake is composed of multiple segments, each represented by a SnakeSegment instance."""
    def __init__(self):
        self.body = []


    def create_body(self, length):
        x_cord = -21
        for x in range(length):
            clone = SnakeSegment()
            clone.turtle.teleport(x_cord, 0)
            self.body.append(clone)
            x_cord -= 21


    def follow(self):
        current_index = -1
        leader_index = -2

        for _ in range(1, len(self.body)):
            current_snake = self.body[current_index]
            leader_snake = self.body[leader_index]

            x_cor = leader_snake.turtle.xcor()
            y_cor = leader_snake.turtle.ycor()
            current_snake.turtle.teleport(x_cor, y_cor)

            current_index -= 1
            leader_index -= 1


    def move_forward(self):
        self.follow()
        self.body[0].turtle.forward(21)


    def turn_right(self):
        if self.body[0].turtle.heading() != 180:
            self.follow()
            self.body[0].turtle.setheading(0)
            self.body[0].turtle.forward(21)

    
    def turn_left(self):
        if self.body[0].turtle.heading() != 0:
            self.follow()
            self.body[0].turtle.setheading(180)
            self.body[0].turtle.forward(21)


    def move_up(self):
        if self.body[0].turtle.heading() != 270:
            self.follow()
            self.body[0].turtle.setheading(90)
            self.body[0].turtle.forward(21)


    def move_down(self):
        if self.body[0].turtle.heading() != 90:
            self.follow()
            self.body[0].turtle.setheading(270)
            self.body[0].turtle.forward(21)


    def detect_collision_wall(self):
        if abs(self.body[0].turtle.xcor()) >= 450:
            return True
        elif abs(self.body[0].turtle.ycor()) >= 400:
            return True
        return False
    

    def detect_collision_self(self):
        for snake in self.body[1:]:
            if self.body[0].turtle.distance(snake.turtle) < 20:
                return True
        return False
    

    def increase_length(self):
        clone = SnakeSegment()
        x_cor = self.body[-1].turtle.xcor()
        y_cor = self.body[-1].turtle.ycor()
        clone.turtle.teleport(x_cor, y_cor)
        self.body.append(clone)
