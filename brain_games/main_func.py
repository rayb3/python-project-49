import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def get_answer():
    answer = prompt.string('Your answer: ')
    return answer


def compare_answer(answer, correct_ans, name):
    if answer != str(correct_ans):
        print(f"'{answer}' is wrong answer ;(. "
              f"Correct answer was '{correct_ans}'")
        print(f"Let's try again, {name}!")
        return False
    else:
        print('Correct!')
        return True
