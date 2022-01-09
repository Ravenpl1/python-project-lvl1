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
        ask_question(idgame, generate_data['items'])
        user_answer = get_answer()
        if check_answer(user_answer, generate_data['correct_answer']) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, generate_data['correct_answer'])
            break
    else:
        end_game(True, user_answer, generate_data['correct_answer'])


'''
def brain_even_logic():
    """Главный вызов."""
    user = greeting()
    display_rule(1)
    user_attempt = 0
    while user_attempt != 3:
        question_num, correct_answer = game_logic(1)
        ask_question(1, question_num)
        user_answer = get_answer()
        if check_answer(user_answer, correct_answer, user) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, correct_answer, user)
            break
    else:
        end_game(True, user_answer, correct_answer, user)


def brain_calc_logic():
    """Главный вызов."""
    user = greeting()
    display_rule(2)
    user_attempt = 0
    while user_attempt != 3:
        (question_num1, question_operation,
            question_num2, correct_answer) = game_logic(2)
        ask_question(2, question_num1, question_operation, question_num2)
        user_answer = get_answer()
        if check_answer(user_answer, str(correct_answer), user) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, str(correct_answer), user)
            break
    else:
        end_game(True, user_answer, str(correct_answer), user)


def brain_gcd_logic():
    """Главный вызов."""
    user = greeting()
    display_rule(3)
    user_attempt = 0
    while user_attempt != 3:
        question_num1, question_num2, correct_answer = game_logic(3)
        ask_question(3, question_num1, question_num2)
        user_answer = get_answer()
        if check_answer(user_answer, str(correct_answer), user) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, str(correct_answer), user)
            break
    else:
        end_game(True, user_answer, str(correct_answer), user)


def brain_progression_logic():
    """Главный вызов."""
    user = greeting()
    display_rule(4)
    user_attempt = 0
    while user_attempt != 3:
        question_num1, correct_answer = game_logic(4)
        ask_question(4, question_num1)
        user_answer = get_answer()
        if check_answer(user_answer, str(correct_answer), user) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, str(correct_answer), user)
            break
    else:
        end_game(True, user_answer, str(correct_answer), user)


def brain_prime_logic():
    """Главный вызов."""
    user = greeting()
    display_rule(5)
    user_attempt = 0
    while user_attempt != 3:
        question_num1, correct_answer = game_logic(5)
        ask_question(5, question_num1)
        user_answer = get_answer()
        if check_answer(user_answer, str(correct_answer), user) is True:
            display_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, str(correct_answer), user)
            break
    else:
        end_game(True, user_answer, str(correct_answer), user)
'''

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


def gcd(var):
    result = []
    for i in range(1, var + 1):
        if var % i == 0:
            result.append(i)
    return result