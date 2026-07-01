from turtle import Turtle, Screen
from random import choice
# from colorgram import extract

# colors = extract("spots.jpg", 20)
# color_list = [color.rgb for color in colors]
# rgb_list = [(r, g, b) for r, g, b in color_list]
# del rgb_list[:3]

turtle = Turtle()
turtle.penup()

screen = Screen()
screen.colormode(255)

rgb_list = [(198, 13, 32), (248, 236, 25), (40, 76, 188), (244, 247, 253), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120),(68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62)]


y = 0
for column in range(10):
    for row in range(10):
        turtle.dot(20, choice(rgb_list))
        turtle.forward(50)
    y += 50
    turtle.teleport(0, y)


screen.mainloop()
