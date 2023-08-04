#!/usr/bin/env python3
import random
from brain_games.main_func import welcome_user, get_answer, compare_answer


def main():
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    for i in range(0, 3):
        rand_num = random.randint(0, 50)
        count = 0
        for i in range(1, rand_num + 1):
            if rand_num % i == 0:
                count += 1
        if count == 2:
            correct_ans = 'yes'
        else:
            correct_ans = 'no'
        print(f'Question: {rand_num}')
        answer = get_answer()
        comp_response = compare_answer(answer, correct_ans, name)
        if comp_response:
            pass
        else:
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
