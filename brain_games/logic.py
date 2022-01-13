# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import (
    ask_question,
    display_correct,
    display_rule,
    end_game,
    get_answer,
    lost_game,
    welcome_user,
)


def games_logic(game):
    """Содержит общую логику игры.

    Args:
        game: принимает функцию игры.
    """
    user = welcome_user()
    user_attempt = 0
    generate_data = game()
    display_rule(generate_data['rule'])
    while user_attempt != 3:
        correct_answer = str(generate_data['correct_answer'])
        ask_question(generate_data['question'])
        user_answer = get_answer()
        if check_answer(user_answer, correct_answer) is True:
            display_correct()
            generate_data = game()
            user_attempt += 1
        else:
            lost_game(user_answer, correct_answer, user)
            break
    else:
        end_game(user)


def check_answer(user_answer, cor_answer):
    """Функция проверяет ответ пользователя.

    Args:
        user_answer: Description of user_answer.
        cor_answer: Description of correct_answer.

    Returns:
        bool: True если корректный ответ, иначе False.
    """
    return user_answer == cor_answer
