import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
states_df = pandas.read_csv("50_states.csv")

score = 0
while score < 50:
    user_answer = screen.textinput(title="Enter a state", prompt="Type a name of a state: ")
    for index, row in states_df.iterrows():
        if row['state'] == user_answer.title():
            turtle.penup()
            turtle.goto(row['x'], row['y'])
            turtle.write(user_answer)
            score += 1

turtle.mainloop()

