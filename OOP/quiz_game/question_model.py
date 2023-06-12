from data import question_data
import random


class QuestionAndAnswer:
    def __init__(self, q, a):
        self.question = q
        self.answer = a


class QuestionsAndAnswers:
    def __init__(self):
        self.list = []
        for item in question_data:
            q = item['text']
            a = item['answer']
            new_question = QuestionAndAnswer(q, a)
            self.list.append(new_question)

    def get_questions(self):
        return self.list

    def get_random_question(self):
        random_question = random.choice(self.list)
        return random_question

    def check_answer(self, q, a):
        question_to_check = self.list[self.list.index(q)]
        return question_to_check.answer == a
