# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
from brain_games.cli import (
    ask_question,
    display_correct,
    display_rule,
    end_game,
    get_answer,
)
from brain_games.scripts.brain_games import main as greeting


def games_logic(game, idgame):
    user = greeting()
    display_rule(idgame)
    user_attempt = 0
    while user_attempt != 3:
        generate_data = game()
        items = generate_data['items']
        correct_answer = str(generate_data['correct_answer'])
        ask_question(idgame, items)
        user_answer = get_answer()
        if check_answer(user_answer, correct_answer) is True:
            display_correct()
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
        user: Description of user.

    Returns  # noqa: DAR201
    """
    if user_answer == cor_answer:
        return True
    else:
        return False
