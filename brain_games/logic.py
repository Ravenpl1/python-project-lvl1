# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
import random


def game_logic(idgame):
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа"""
    if idgame == 1:
        rand_num1 = random.randrange(0, 100, 1)
        correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
        return (rand_num1, correct_answer)
    elif idgame == 2:
        math_operations = ('+', '-', '*')
        rand_math_operation = random.choice(math_operations)
        rand_num1 = random.randrange(0, 10, 1)
        rand_num2 = random.randrange(0, 10, 1)
        if rand_math_operation == '+':
            correct_answer = rand_num1 + rand_num2
        elif rand_math_operation == '-':
            correct_answer = rand_num1 - rand_num2
        elif rand_math_operation == '*':
            correct_answer = rand_num1 * rand_num2
        return rand_num1, rand_math_operation, rand_num2, correct_answer
    elif idgame == 3:
        rand_num1 = random.randrange(1, 100, 1)
        rand_num2 = random.randrange(1, 100, 1)
        num1_gcd = gcd(rand_num1)
        num2_gcd = gcd(rand_num2)
        correct_answer = max(list(set(num1_gcd) & set(num2_gcd)))
        return rand_num1, rand_num2, correct_answer
    elif idgame == 4:
        rand_len_progression = random.randrange(5, 15, 1)
        rand_step = random.randrange(1, 10, 1)
        progression = [i for i in range(rand_step,
                                        rand_len_progression * rand_step + 1,
                                        rand_step)]
        rand_question_element = random.randrange(1, rand_len_progression, 1)
        correct_answer = progression[rand_question_element - 1]
        progression[rand_question_element - 1] = 0
        return progression, correct_answer
    elif idgame == 5:
        rand_num1 = random.randrange(0, 101, 1)
        num1_gcd = gcd(rand_num1)
        correct_answer = 'yes' if len(num1_gcd) == 2 else 'no'
        return (rand_num1, correct_answer)


def check_answer(user_answer, cor_answer, user):
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
