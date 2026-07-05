from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=900, height=800)
screen.title("Snake")
screen.bgcolor("black")
screen.listen()
screen.tracer(0)


food = Food()
snake = Snake()
snake.create_body(5)
scoreboard = Scoreboard()
screen.onkeypress(key="w", fun=snake.move_up)
screen.onkeypress(key="s", fun=snake.move_down)
screen.onkeypress(key="a", fun=snake.turn_left)
screen.onkeypress(key="d", fun=snake.turn_right)
screen.onkeypress(key="Up", fun=snake.move_up)
screen.onkeypress(key="Down", fun=snake.move_down)
screen.onkeypress(key="Left", fun=snake.turn_left)
screen.onkeypress(key="Right", fun=snake.turn_right)


def play_game():
    snake.move_forward()
    if food.detect_collision(snake.body):
        snake.increase_length()
        scoreboard.add_point()
    screen.update()
    if snake.detect_collision_wall() or snake.detect_collision_self():
        scoreboard.game_over()
        return
    
    screen.ontimer(fun=play_game, t=100)


play_game()
screen.mainloop()
