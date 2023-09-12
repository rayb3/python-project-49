import random


def get_question_and_answer():
    list_len = random.randint(5, 10)
    hidden_number = random.randint(0, list_len - 1)
    array_list = []
    array_number = 0
    for i in range(0, list_len):
        array_list.append(array_number)
        array_number += 2
    correct_answer = array_list[hidden_number]
    array_list[hidden_number] = ".."
    array_str = (' '.join(str(x) for x in array_list))
    question = (f'Question: {array_str}')

    return question, correct_answer


def get_question_title():
    return 'What number is missing in the progression?'
