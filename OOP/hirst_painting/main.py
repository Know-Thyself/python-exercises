import colorgram
import turtle
import random

painter = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
painter.penup()
painter.setx(-140);
painter.sety(150)
screen.bgcolor('medium slate blue')

rgb_colors = []
colors = colorgram.extract('colorful_img.jpg', 78)

for color in colors:
    rgb_colors.append(color.rgb)


def draw_dot_painting(space, num_of_dots):
    for _ in range(num_of_dots):
        for _ in range(num_of_dots):
            painter.dot(20, random.choice(rgb_colors))
            painter.forward(space)
        painter.backward(space * num_of_dots)
        painter.right(90)
        painter.forward(space)
        painter.left(90)


painter.penup()
painter.hideturtle()
draw_dot_painting(30, 10)
screen.exitonclick()

