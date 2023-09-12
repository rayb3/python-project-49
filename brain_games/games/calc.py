import random
ARITHMETIC_OPERATORS = ['+', '-', '*']


def get_question_and_answer():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)
    operator = random.choice(ARITHMETIC_OPERATORS)
    if operator == '+':
        correct_answer = first_number + second_number
    elif operator == '-':
        correct_answer = first_number - second_number
    else:
        correct_answer = first_number * second_number
    question = (f'Question: {first_number} {operator} {second_number}')
    return question, correct_answer


def get_question_title():
    return 'What is the result of the expression?'
