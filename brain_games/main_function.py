import prompt

NUMBER_OF_ROUNDS = 3


def start_game(game):
    print('Welcome to the Brain Games!')
    username = prompt.string('May I have your name? ')
    print(f'Hello, {username}!')
    question_title = game.get_question_title()
    print(question_title)
    for i in range(0, NUMBER_OF_ROUNDS):
        question, correct_answer = game.get_question_and_answer()
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer != str(correct_answer):
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'")
            return print(f"Let's try again, {username}!")

        else:
            print('Correct!')
    print(f'Congratulations, {username}!')
