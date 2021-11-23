#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем welcome_user."""
import random
from brain_games.cli import get_correct

def game_logic(idgame):
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

def check_answer(user_answer, correct_answer, user):
    if user_answer == correct_answer:
        return True
    else:
        return False

