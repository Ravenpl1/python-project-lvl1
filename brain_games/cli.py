# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция возвращает введенное имя.

    Returns  # noqa: DAR201
    """
    user = prompt.string('Welcome to the Brain Games! \nMay I have your name? ')
    print('Hello, {0}!'.format(user))
    return user


def display_rule(rule):
    """Функция знакомит пользователя с правилами игры.

    Args:
        idgame: Description of idgame.
    """
    print(rule)


def ask_question(question):
    """Функция вопроса.

    Создает и выводит вопрос на экран.

    Args:
        idgame: Description of idgame.
        items: Description of args.
    """
    print(question)


def get_answer():
    """Функция получает ответ пользователя.

    Returns  # noqa: DAR201
    """
    return prompt.string('Your answer: ')


def display_correct():
    """Функция отображает Correct."""
    print('Correct!')


def end_game(correct, user_answer, correct_answer, user):
    """Функция отображает конец игры.

    Args:
        correct: Description of correct.
        user_answer: Description of user_answer.
        correct_answer: Description of correct_answer.
        user: Description of user.
    """
    if correct is True:
        print('Congratulations, {0}!'.format(user))
    elif correct is False:
        print("'{uanswer}' is wrong answer ;(. Correct answer was '{canswer}'."
              .format(uanswer=user_answer, canswer=correct_answer))
        print("Let's try again, {0}!".format(user))
