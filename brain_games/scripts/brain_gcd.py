#!/usr/bin/env python3
import random
from brain_games.main_func import welcome_user, get_answer, compare_answer


def main():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    for i in range(0, 3):
        first_num = random.randint(1, 50)
        second_num = random.randint(1, 50)
        print(f'Question: {first_num} {second_num}')
        if first_num <= second_num:
            lowest_num = first_num
        else:
            lowest_num = second_num
        divider = 1
        while lowest_num + 1 != divider:
            if (first_num % divider == 0) and (second_num % divider == 0):
                divider_ans = divider
                divider += 1
            else:
                divider += 1
        answer = get_answer()
        comp_response = compare_answer(answer, divider_ans, name)
        if comp_response:
            pass
        else:
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
