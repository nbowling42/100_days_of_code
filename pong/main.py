from turtle import Screen
from gameboard import ScoreBoard


screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

scoreboard = ScoreBoard(screen)











screen.update()
screen.exitonclick()
