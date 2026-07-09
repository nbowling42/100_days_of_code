from turtle import Turtle


class ScoreBoard:
    def __init__(self, screen):
        self.draw_center_line(screen)
        self.player = self.display_score(-80, screen, 0)
        self.computer = self.display_score(80, screen, 0)
        self.player_score = 0
        self.computer_score = 0 


    def draw_center_line(self, screen):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.color("white")
        self.t.setheading(270)
        self.t.teleport(0, screen.window_height() / 2)


        for _ in range(int(screen.window_height() / 20)):
            self.t.forward(10)
            self.t.penup()
            self.t.forward(10)
            self.t.pendown()


    def display_score(self, screen_x, screen, score):
        self.t = Turtle()
        self.t.hideturtle()
        self.t.color("white")
        self.t.teleport(screen_x, (screen.window_height() / 2) - 100)
        self.t.write(f"{score}", font=('Monospace', 64, 'normal'), align="center")


    def add_point(self):
        pass
