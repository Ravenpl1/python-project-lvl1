# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
import prompt
from brain_games.cli import welcome_user

# Константы.
NUMBER_OF_ROUNDS = 3


def games_logic(game):
    """Функция общей логики игр.

    Args:
        game: модуль игры.
    """
    user = welcome_user()
    correct_answer, question = game.get_round_data()
    print(game.RULE)
    for _ in range(NUMBER_OF_ROUNDS):
        print('Question: {0}'.format(question))
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            correct_answer, question = game.get_round_data()
        else:
            print("'{0}' is wrong answer ;(. ".format(user_answer), end='')
            print("Correct answer was '{0}'.".format(correct_answer))
            print("Let's try again, {0}!".format(user))
            break
    else:
        print('Congratulations, {0}!'.format(user))
