#!/usr/bin/env python3
import random
from brain_games.main_func import welcome_user, get_answer, compare_answer


def main():
    name = welcome_user()
    for i in range(0, 3):
        first_num = random.randint(0, 50)
        second_num = random.randint(0, 50)
        operator = random.choice(['+', '-', '*'])
        if operator == '+':
            correct_ans = first_num + second_num
        elif operator == '-':
            correct_ans = first_num - second_num
        else:
            correct_ans = first_num * second_num
        print(f'Question: {first_num} {operator} {second_num}')
        answer = get_answer()
        comp_response = compare_answer(answer, correct_ans)
        if comp_response:
            pass
        else:
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
