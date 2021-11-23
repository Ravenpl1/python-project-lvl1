#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from brain_games.scripts.brain_games import main as greeting
from brain_games.cli import get_rule, ask_question, get_answer, get_correct, end_game
from brain_games.logic import game_logic, check_answer

def main():
    """Главный вызов."""
    user = greeting()
    get_rule(1)
    user_attempt = 0
    while user_attempt != 3:
        question_num, correct_answer = game_logic(1)
        ask_question(1, question_num)
        user_answer = get_answer()
        if check_answer(user_answer, correct_answer, user) == True:
            get_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, correct_answer, user)
            break
    else:
        end_game(True, user_answer, correct_answer, user)


if __name__ == '__main__':
    main()
