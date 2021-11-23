#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from brain_games.scripts.brain_games import main as greeting
from brain_games.cli import get_rule, ask_question, get_answer, get_correct, end_game
from brain_games.logic import game_logic, check_answer

def main():
    """Главный вызов."""
    user = greeting()
    get_rule(2)
    user_attempt = 0
    while user_attempt != 3:
        question_num1, question_operation, question_num2, correct_answer = game_logic(2)
        ask_question(2, question_num1, question_operation, question_num2)
        user_answer = get_answer()
        if check_answer(user_answer, str(correct_answer), user) == True:
            get_correct()
            user_attempt += 1
        else:
            end_game(False, user_answer, str(correct_answer), user)
            break
    else:
        end_game(True, user_answer, str(correct_answer), user)


if __name__ == '__main__':
    main()
