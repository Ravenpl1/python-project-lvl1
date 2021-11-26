# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
import random

from brain_games.cli import display_correct


def game_logic(idgame):
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильный ответ"""
    if idgame == 1:
        rand = random.randrange(0, 100, 1)
        return (rand, 'yes' if rand % 2 == 0 else 'no')
    elif idgame == 2:
        math_operations = ('+', '-', '*')
        rand_math_operation = random.choice(math_operations)
        rand_num1 = random.randrange(0, 10, 1)
        rand_num2 = random.randrange(0, 10, 1)
        if rand_math_operation == '+':
            result = rand_num1 + rand_num2
        elif rand_math_operation == '-':
            result = rand_num1 - rand_num2
        elif rand_math_operation == '*':
            result = rand_num1 * rand_num2
        return rand_num1, rand_math_operation, rand_num2, result
    elif idgame == 3:
        rand_num1 = random.randrange(0, 100, 1)
        rand_num2 = random.randrange(0, 100, 1)
        num1_gcd = gcd(rand_num1)
        num2_gcd = gcd(rand_num2)
        result = max(list(set(num1_gcd) & set(num2_gcd)))
        return rand_num1, rand_num2, result
    elif idgame == 4:
        rand_len_progression = random.randrange(5, 15, 1)
        rand_step = random.randrange(1, 10, 1)
        progression = [i for i in range(rand_step, rand_len_progression*rand_step+1, rand_step)]
        rand_question_element = random.randrange(1, rand_len_progression, 1)
        print(rand_len_progression, rand_step, progression, rand_question_element)
        result = progression[rand_question_element-1]
        progression[rand_question_element-1] = 0
        return progression, result


def check_answer(user_answer, correct_answer, user):
    """Функция проверяет ответ пользователя
    
    Args:
        user_answer: Description of user_answer.
        correct_answer: Description of correct_answer.
        user: Description of user.
    
    Returns  # noqa: DAR201
    """
    if user_answer == correct_answer:
        return True
    else:
        return False


def gcd(var):
    result = []
    for i in range(1, var + 1):
        if var % i == 0:
            result.append(i)
    return result
