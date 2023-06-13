from question_model import QuestionAndAnswer
from data import question_data
from api_data import general_knowledge_q_and_a
import random
import html


class QuestionsAndAnswers:
    def __init__(self):
        self.list = []
        for index, item in enumerate(general_knowledge_q_and_a):
            q = html.unescape(item['question'])
            a = item['correct_answer']
            new_question = QuestionAndAnswer(index + 1, q, a)
            self.list.append(new_question)

    def get_questions(self):
        return self.list

    def get_first_question(self):
        return self.list[0]

    def get_next_question(self, current_question):
        if self.list.index(current_question) == len(self.list) - 1:
            return self.list[0]
        else:
            return self.list[self.list.index(current_question) + 1]

    def get_random_question(self):
        random_question = random.choice(self.list)
        return random_question

    def check_answer(self, q, a):
        question_to_check = self.list[self.list.index(q)]
        return question_to_check.answer.lower() == a.lower()
