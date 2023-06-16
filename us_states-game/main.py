import turtle
import pandas
screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgpic("blank_states_img.gif")
states_df = pandas.read_csv("50_states.csv")
user_score = 0
correct_answers = []
missing_states = []


def main(score):
    user_answer = screen.textinput(title=f"Your score is: {score} / 50", prompt="Type a name of a state: ")
    if user_answer:
        for _, row in states_df.iterrows():
            if row['state'] == user_answer.title():
                turtle.penup()
                turtle.goto(row['x'], row['y'])
                turtle.write(row['state'])
                score += 1
                correct_answers.append(row['state'])
                if row['state'] in missing_states:
                    missing_states.remove(row['state'])
            elif row['state'] not in missing_states and row['state'] not in correct_answers:
                missing_states.append(row['state'])
        if score == 50:
            screen.textinput(title=f"Congratulations! Your score is: {score} / 50", prompt="")
        else:
            main(score)
    else:
        states_to_learn = pandas.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        print(states_to_learn)
        screen.bye()
        return


main(user_score)
