from quiz_brain import QuestionsAndAnswers

questions_and_answers = QuestionsAndAnswers()
q_and_a_list = questions_and_answers.get_questions()


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
            print(f"The correct answer was: {current_question.answer}\n")
        else:
            print(f"Sorry, wrong answer!\nYour score is {score}/{current_question.question_number}")
            print(f"The correct answer was: {current_question.answer}\n")
        if current_question.question_number == len(q_and_a_list):
            print(f"You've finished all the questions! Your final score is: {score}/{current_question.question_number}")
            is_repeating = input("Would you like to go again? Type 'y' for yes or 'e' to exit: ")
            if is_repeating != "y":
                is_game_on = False
            else:
                current_question = questions_and_answers.get_first_question()
                score = 0
        else:
            current_question = questions_and_answers.get_next_question(current_question)


start_quiz()
