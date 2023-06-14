import colorgram
import turtle
import random

painter = turtle.Turtle()
screen = turtle.Screen()
turtle.colormode(255)
painter.penup()

rgb_colors = []
colors = colorgram.extract('colorful_img.jpg', 78)

for color in colors:
    rgb_colors.append(color.rgb)

screen.bgcolor(random.choice(rgb_colors))


def draw_dots(dots, x, y, size, space):
    for _ in range(dots):
        painter.goto(x, y)
        for _ in range(dots):
            painter.dot(size, random.choice(rgb_colors))
            painter.forward(space)
        y -= space


def draw_dot_painting(space, num_of_dots):
    for _ in range(num_of_dots):
        for _ in range(num_of_dots):
            painter.dot(20, random.choice(rgb_colors))
            painter.forward(space)
        painter.backward(space * num_of_dots)
        painter.right(90)
        painter.forward(space)
        painter.left(90)


def draw_hirst_painting(num_of_dots, size, space):
    direction = 'right'
    for _ in range(num_of_dots):
        for _ in range(num_of_dots):
            painter.dot(size, random.choice(rgb_colors))
            painter.forward(space)
        if direction == 'right':
            painter.right(90)
            painter.forward(space)
            painter.right(90)
            painter.forward(space)
            direction = 'left'
        else:
            painter.left(90)
            painter.forward(space)
            painter.left(90)
            painter.forward(space)
            direction = 'right'


painter.home()
# draw_hirst_painting(10, 20, 30)
# draw_dot_painting(30, 10)
draw_dots(10, -140, 150,20, 30)
painter.hideturtle()
screen.exitonclick()

