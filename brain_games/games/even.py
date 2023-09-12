import random


def get_question_and_answer():
    random_number = random.randint(0, 100)
    question = (f'Question: {random_number}')
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return question, correct_answer


def get_question_title():
    return 'Answer "yes" if the number is even, otherwise answer "no".'
