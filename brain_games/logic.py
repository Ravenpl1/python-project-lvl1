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
        return 1

def check_answer(user_answer, correct_answer, user):
    if user_answer == correct_answer:
        return True
    else:
        return False

