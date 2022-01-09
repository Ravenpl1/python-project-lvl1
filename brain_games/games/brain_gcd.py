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


def brain_gcd_logic():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_num1 = random.randrange(1, 100, 1)
    rand_num2 = random.randrange(1, 100, 1)
    num1_gcd = gcd(rand_num1)
    num2_gcd = gcd(rand_num2)
    correct_answer = max(list(set(num1_gcd) & set(num2_gcd)))
    return rand_num1, rand_num2, correct_answer


if __name__ == '__main__':
    main()
