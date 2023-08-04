#!/usr/bin/env python3
import random
from brain_games.main_func import welcome_user, get_answer, compare_answer


def main():
    name = welcome_user()
    print('What number is missing in the progression?')
    for i in range(0, 3):
        list_len = random.randint(5, 10)
        hidden_num = random.randint(0, list_len - 1)
        ar_list = []
        num = 0
        for i in range(0, list_len):
            ar_list.append(num)
            num += 2
        correct_ans = ar_list[hidden_num]
        ar_list[hidden_num] = ".."
        ar_str = (' '.join(str(x) for x in ar_list))
        print(f'Question: {ar_str}')
        answer = get_answer()
        comp_response = compare_answer(answer, correct_ans, name)
        if comp_response:
            pass
        else:
            return
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
