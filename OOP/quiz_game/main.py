from question_model import QuestionsAndAnswers

questions_and_answers = QuestionsAndAnswers()


def start_quiz():
    is_game_on = True
    score = 0
    number_of_questions = 0
    while is_game_on:
        random_question = questions_and_answers.get_random_question()
        user_answer = input(f"Q.{number_of_questions + 1}. {random_question.question} Type 'True' or 'False': ")
        is_correct = questions_and_answers.check_answer(random_question, user_answer)
        number_of_questions += 1
        if is_correct:
            score += 1
            print(f"You got it right!\nYour score is: {score}/{number_of_questions}")
            print(f"The correct answer was: {random_question.answer}")
        else:
            print(f"Wrong answer!\nYour score is {score}/{number_of_questions}")
            print(f"The correct answer was: {random_question.answer}")
        next_question = input("Type 'n' to go to the next question or 'e' to exit: ")
        if next_question != "n":
            is_game_on = False


start_quiz()
