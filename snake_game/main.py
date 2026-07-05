from turtle import Turtle, Screen
from snake import Snake


screen = Screen()
screen.setup(width=900, height=800)
screen.title("Snake")
screen.listen()
screen.tracer(3)

snake = Snake()
snake.create_body(3)


key_states = {
    "w": False,
    "a": False,
    "s": False,
    "d": False
}


screen.onkeypress(key="w", fun=snake.move_forward)
screen.onkeypress(key="s", fun=snake.move_backward)
screen.exitonclick()
