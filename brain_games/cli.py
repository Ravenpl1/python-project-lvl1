# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция приветствует и возвращает введенное имя.

    Returns:
        user: return user name.
    """
    user = prompt.string('Welcome to the Brain Games! \nMay I have your name? ')
    print('Hello, {0}!'.format(user))
    return user


def display_rule(rule):
    """Функция отображает правила игры.

    Args:
        rule: Description of rule.
    """
    print(rule)


def ask_question(question):
    """Функция отображает вопрос игры.

    Args:
        question: Description of question.
    """
    print(question)


def get_answer():
    """Функция получает ответ пользователя.

    Returns:
        prompt: return user responce.
    """
    return prompt.string('Your answer: ')


def display_correct():
    """Функция отображает Correct."""
    print('Correct!')


def lost_game(user_answer, correct_answer, user):
    """Функция отображает проигрыш.

    Args:
        user_answer: Description of user_answer.
        correct_answer: Description of correct_answer.
        user: Description of user.
    """
    text1 = "'{0}' is wrong answer ;(. ".format(user_answer)
    text2 = "Correct answer was '{0}'.".format(correct_answer)
    print(text1 + text2)
    print("Let's try again, {0}!".format(user))


def end_game(user):
    """Функция отображает конец игры.

    Args:
        user: Description of user.
    """
    print('Congratulations, {0}!'.format(user))
