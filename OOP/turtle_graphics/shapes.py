from turtle import Turtle, Screen

master_oogway = Turtle()
master_oogway.shape('turtle')
master_oogway.color('DarkCyan')
master_oogway.pensize(2)
master_oogway.pencolor("brown")

# Draw a dashed line
# for _ in range(20):
#     master_oogway.pendown()
#     master_oogway.forward(10)
#     master_oogway.penup()
#     master_oogway.forward(10)

master_oogway.penup()
master_oogway.setx(-50)
master_oogway.sety(150)
colors = ['brown', 'green', 'red', 'blue', 'dark orange', 'black', 'gray', 'indigo']
number_of_sides = 3
color_index = 0
# Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon
master_oogway.pendown()


def draw_shapes(sides, color):
    angle = 360 / sides
    for _ in range(sides):
        master_oogway.pencolor(color)
        master_oogway.forward(100)
        master_oogway.right(angle)


while color_index < len(colors):
    shape_color = colors[color_index]
    draw_shapes(number_of_sides, shape_color)
    number_of_sides += 1
    color_index += 1

screen = Screen()
screen.exitonclick()
