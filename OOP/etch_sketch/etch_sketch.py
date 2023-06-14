from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(10)


def move_backwards():
    pen.backward(20)


def move_counter_clockwise():
    pass


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.exitonclick()
