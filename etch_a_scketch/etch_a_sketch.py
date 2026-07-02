from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
screen.listen()

def move_forward():
    turtle.forward(3)

def move_backward():
    turtle.backward(3)

def turn_right():
    turtle.right(3)

def turn_left():
    turtle.left(3)

def clear_screen():
    screen.resetscreen()


screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="d", fun=turn_right)
screen.onkeypress(key="a", fun=turn_left)
screen.onkeyrelease(key="c", fun=clear_screen)
screen.mainloop()
