from paddles import Paddle
from turtle import Turtle, Screen


class GameBoard:

    def __init__(self):
        self.s = Screen()
        self.s.setup(width=800, height=700)
        self.s.bgcolor("black")
        self.s.title("Pong")
        self.s.listen()
        self.s.tracer(0)


    def make_board(self):
        player_paddle = Paddle()
        computer_paddle = Paddle()

        x_cor = (self.s.window_width() / 2) - 50
        player_paddle.t.teleport((x_cor * -1), 0)
        computer_paddle.t.teleport(x_cor, 0)
        self.s.update()

        self.make_dashed_line()



    
    def make_dashed_line(self):
        y_cor = (self.s.window_height())

        line = Turtle()
        line.color("white")
        line.hideturtle()
        line.teleport(0, y_cor / 2)
        line.setheading(270)

        for _ in range(int(y_cor)):
            line.forward(10)
            line.penup()
            line.forward(10)
            line.pendown()
        
        self.s.update()