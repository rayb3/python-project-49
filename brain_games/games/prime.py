import random


def get_question_and_answer():
    random_number = random.randint(0, 50)
    question = (f'Question: {random_number}')
    count = 0
    for i in range(1, random_number + 1):
        if random_number % i == 0:
            count += 1
    if count == 2:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return question, correct_answer


def get_question_title():
    return 'Answer "yes" if given number is prime. Otherwise answer "no".'
