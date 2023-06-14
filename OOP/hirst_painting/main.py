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


draw_hirst_painting(10, 20, 30)
# draw_dot_painting(30, 10)
painter.hideturtle()
screen.exitonclick()

