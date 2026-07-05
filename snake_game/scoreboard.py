from turtle import Turtle

class Scoreboard:

    def __init__(self):
        self.t = Turtle()
        self.t.color("white")
        self.t.hideturtle()
        self.t.teleport(0, 350)
        self.score = 0
        self.t.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))


    def add_point(self):
        self.score += 1
        self.t.clear()
        self.t.write(f"Score: {self.score}", align="center", font=('Arial', 16, 'normal'))


    def game_over(self):
        self.t.teleport(0, 0)
        self.t.color("red")
        self.t.write("Game Over.", align="center", font=('Arial', 24, 'normal'))
