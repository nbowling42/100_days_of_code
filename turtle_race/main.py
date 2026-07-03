from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.title("Turtle Race")
screen.setup(900, 800)


def create_turtle(color):
    t = Turtle(shape="turtle")
    t.speed(10)
    t.color(color)
    return t

def set_starting_position(instances):
    # Set the starting position of the turtles on the screen
    spacing = 40
    starting_x = (screen.window_width() / 2 - 50) * -1
    starting_y = ((len(instances) - 1) * spacing) / 2

    offset = 0
    for t in instances:
        t.penup()
        t.goto(starting_x, starting_y + offset)
        offset -= spacing

def create_turtle_list(colors):
    turtles = [create_turtle(color) for color in colors]
    return turtles

def race_turtles(turtle_list):
        while True:
            for turtle in turtle_list:
                turtle.forward(randint(5, 10))
                if turtle.xcor() >= 280.0:
                    return turtle.pencolor()
                
def check_results(bet, winning_color):
    if winning_color == bet:
        return "win"
    return "lose"


game_over = False
while not game_over:
    screen.bgpic("turtle_race_background.gif")
    user_bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:").lower()

    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle_list = create_turtle_list(colors)
    set_starting_position(turtle_list)
    winner = race_turtles(turtle_list)
    result = check_results(user_bet, winner)

    play_again = screen.textinput("Results", f"You {result}. The {winner} turtle is the winner. \nType 'yes' to play again or 'no' to quit.").lower()
    if play_again == "no":
        game_over = True
    else:
        screen.clearscreen()
