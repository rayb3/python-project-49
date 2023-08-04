#!/usr/bin/env python3
import random
from brain_games.main_func import welcome_user, get_answer, compare_answer


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        rand_num = random.randint(0, 100)
        print(f'Question: {rand_num}')
        if rand_num % 2 == 0:
            correct_ans = 'yes'
        else:
            correct_ans = 'no'
        answer = get_answer()
        comp_response = compare_answer(answer, correct_ans, name)
        if comp_response:
            pass
        else:
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
