import random


def get_question_and_answer():
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    question = (f'Question: {first_num} {second_num}')
    if first_num <= second_num:
        lowest_num = first_num
    else:
        lowest_num = second_num
    divisor = 1
    while lowest_num + 1 != divisor:
        if (first_num % divisor == 0) and (second_num % divisor == 0):
            greatest_divisor = divisor
            divisor += 1
        else:
            divisor += 1
    return question, greatest_divisor


def get_question_title():
    return 'Find the greatest common divisor of given numbers.'
