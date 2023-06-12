from quiz_brain import QuestionsAndAnswers

questions_and_answers = QuestionsAndAnswers()


def start_quiz():
    is_game_on = True
    score = 0
    current_question = questions_and_answers.get_first_question()
    while is_game_on:
        user_answer = input(
            f"Q{current_question.question_number}. {current_question.question} Type 'True' or 'False': ")
        is_correct = questions_and_answers.check_answer(current_question, user_answer)
        if is_correct:
            score += 1
            print(f"You got it right!\nYour score is: {score}/{current_question.question_number}")
            print(f"The correct answer was: {current_question.answer}")
        else:
            print(f"Wrong answer!\nYour score is {score}/{current_question.question_number}")
            print(f"The correct answer was: {current_question.answer}")
        next_question = input("Type 'n' to go to the next question or 'e' to exit: ")
        if next_question != "n":
            is_game_on = False
        else:
            current_question = questions_and_answers.get_next_question(current_question)


start_quiz()
