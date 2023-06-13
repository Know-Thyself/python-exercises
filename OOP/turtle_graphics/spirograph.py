import turtle
import random

artist = turtle.Turtle()
directions = [0, 90, 180, 270]
artist.color('white')
artist.pensize(2)
artist.speed('fastest')
turtle.colormode(255)


def generate_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


turtle.colormode(255)
screen = turtle.Screen()
screen.bgcolor('midnight blue')


def draw_spirograph(tint):
    for _ in range(int(360/tint)):
        current_heading = artist.heading()
        artist.pencolor(generate_rgb())
        artist.circle(80)
        artist.setheading(current_heading + tint)
        # also possible to turn left
        # artist.left(tint)


draw_spirograph(5)
artist.hideturtle()
screen.exitonclick()


