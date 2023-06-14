from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=400)

turtle_colors = ["purple", "green", "red", "blue", "orange", "brown"]
turtles = []


def create_turtles(colors, x, y):
    for i in range(len(colors)):
        racer = Turtle(shape="turtle")
        racer.color(colors[i])
        racer.penup()
        racer.goto(x, y)
        turtles.append(racer)
        y -= 40


create_turtles(turtle_colors, -280, 100)


def start_race(racers):
    x = -280
    while x < 280:
        for racer in racers:
            racer.forward(random.randint(5, 10))
            if x < racer.xcor():
                x = racer.xcor()
                winner_color = racer.pencolor()
    return winner_color


user_bet = screen.textinput(title="Make a bet", prompt="Which turtle will win? \nEnter your prediction: purple/green/red/blue/orange/brown ")
if user_bet:
    winner = start_race(turtles)
    if user_bet == winner:
        print(f"You've won! {winner} is the winner.")
    else:
        print(f"You've lost {winner} is the winner.")

screen.exitonclick()
