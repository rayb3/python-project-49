#!/usr/bin/env python3
import random
import prompt


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        rand_num = random.randint(0, 100)
        print(f'Question: {rand_num}')
        if rand_num % 2 == 0:
            correct_ans = 'yes'
        else:
            correct_ans = 'no'
        answer = prompt.string('Your answer: ')
        if answer not in ('yes', 'no'):
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_ans}'")
        elif answer == 'yes' and correct_ans == 'no':
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_ans}'")
        elif answer == 'no' and correct_ans == 'yes':
            return (f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_ans}'")
        else:
            print('Correct!')
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
