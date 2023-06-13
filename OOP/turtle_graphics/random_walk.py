import turtle
import random

random_walker = turtle.Turtle()
directions = [0, 90, 180, 270]
random_walker.pensize(10)
random_walker.speed('fastest')
turtle.colormode(255)


def generate_rgb():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple


for _ in range(300):
    random_walker.pencolor(generate_rgb())
    random_walker.forward(40)
    random_walker.setheading(random.choice(directions))

# screen = turtle.Screen()
# screen.exitonclick()
