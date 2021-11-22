# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import prompt, random
from brain_games.cli import welcome_user

def main():
    """Главный вызов."""
    user = welcome_user()
    print("Hello, %s!" % user)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_answer = ''
    user_attempt = 0
    while user_attempt != 3:
        question_num = random.randrange(0, 100, 1)
        quesion_answer = 'yes' if question_num % 2 == 0 else 'no'
        print('Question: %i' % question_num)
        user_answer = prompt.string('Your answer: ')
        if user_answer == quesion_answer and user_attempt != 3:
            print('Correct!')
            user_attempt += 1
            print('Congratulations, %s!' % user) if user_attempt == 3 else None
        else:
            print("'yes' is wrong answer ;(. Correct answer was 'no'.")
            print("Let's try again, %s!" % user)
            break


if __name__ == '__main__':
    main()
