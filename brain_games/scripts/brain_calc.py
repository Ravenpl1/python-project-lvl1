#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import prompt, random
from brain_games.scripts.brain_games import main
from brain_games.cli import rule, ask_question, get_answer

def main():
    """Главный вызов."""
    user = greeting()
    rule(2)


if __name__ == '__main__':
    main()
