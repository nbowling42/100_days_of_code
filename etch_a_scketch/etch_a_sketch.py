from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()

def forward_press():
    key_strokes["w"] = True
def forward_release():
    key_strokes["w"] = False

def backward_press():
    key_strokes["s"] = True
def backward_release():
    key_strokes["s"] = False

def left_press():
    key_strokes["a"] = True
def left_release():
    key_strokes["a"] = False

def right_press():
    key_strokes["d"] = True
def right_release():
    key_strokes["d"] = False

def clear_screen():
    screen.resetscreen()

def move_turtle():
        speed = 5
        if key_strokes["w"]:
            turtle.forward(speed)
        if key_strokes["s"]:
            turtle.backward(speed)
        if key_strokes["a"]:
            turtle.left(speed)
        if key_strokes["d"]:
            turtle.right(speed)

        screen.ontimer(move_turtle, 10)

key_strokes = {
    "w": False,
    "a": False,
    "s": False,
    "d": False,
}

screen.onkeypress(key="w", fun=forward_press)
screen.onkeyrelease(key="w", fun=forward_release)
screen.onkeypress(key="s", fun=backward_press)
screen.onkeyrelease(key="s", fun=backward_release)
screen.onkeypress(key="d", fun=right_press)
screen.onkeyrelease(key="d", fun=right_release)
screen.onkeypress(key="a", fun=left_press)
screen.onkeyrelease(key="a", fun=left_release)
screen.onkeyrelease(key="c", fun=clear_screen)

move_turtle()
screen.mainloop()
