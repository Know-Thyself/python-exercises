from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()


def move_forwards():
    pen.forward(20)


def move_backwards():
    pen.backward(20)


def move_counter_clockwise():
    pass


def turn_left():
    pen.left(20)


def turn_right():
    pen.right(20)


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.exitonclick()
