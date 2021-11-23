#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция возвращает введенное имя."""
    print('Welcome to the Brain Games')
    return prompt.string('May I have your name? ')


def get_rule(idgame):
    if idgame == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif idgame == 2:
        print('What is the result of the expression?')


def ask_question(idgame, num):
    if idgame == 1:
        print('Question: %i' % num)
    elif idgame == 2:
        print('What is the result of the expression?')


def get_answer():
    return prompt.string('Your answer: ')


def get_correct():
    print('Correct!')


def end_game(correct, user_answer, correct_answer, user):
    if correct == True:
        print('Congratulations, %s!' % user)
    elif correct == False:
        print("'%s' is wrong answer ;(. Correct answer was '%s'." % (user_answer, correct_answer))
        print("Let's try again, %s!" % user)
