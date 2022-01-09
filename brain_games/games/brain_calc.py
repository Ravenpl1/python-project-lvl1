#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from brain_games.cli import (
    ask_question,
    display_correct,
    display_rule,
    end_game,
    get_answer,
)
from brain_games.logic import check_answer, game_logic
from brain_games.scripts.brain_games import main as greeting


def main():
    pass


def brain_calc_logic():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
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


if __name__ == '__main__':
    main()
