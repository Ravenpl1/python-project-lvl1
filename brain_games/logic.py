# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import (
    ask_question,
    display_correct,
    display_rule,
    end_game,
    get_answer,
    welcome_user,
)


def games_logic(game):
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
            end_game(False, user_answer, correct_answer, user)
            break
    else:
        end_game(True, user_answer, correct_answer, user)


def check_answer(user_answer, cor_answer):
    """Функция проверяет ответ пользователя

    Args:
        user_answer: Description of user_answer.
        cor_answer: Description of correct_answer.

    Returns  # noqa: DAR201
    """
    if user_answer == cor_answer:
        return True
    else:
        return False
