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

# Константы.
ROUNDS = 3


def games_logic(game):
    """Функция общей логики игр.

    Args:
        game: игра.
    """
    user = welcome_user()
    generate_data = game()
    display_rule(generate_data['rule'])
    for _ in range(ROUNDS):
        correct_answer = str(generate_data['correct_answer'])
        ask_question(generate_data['question'])
        user_answer = get_answer()
        if user_answer == correct_answer:
            display_correct()
            generate_data = game()
        else:
            lost_game(user_answer, correct_answer, user)
            break
    else:
        end_game(user)
