# -*- coding: utf-8 -*- #

"""Импортируем prompt."""
import prompt


def welcome_user():
    """Функция возвращает введенное имя.

    Returns  # noqa: DAR201
    """
    return prompt.string('Welcome to the Brain Games \nMay I have your name? ')


def display_rule(idgame):
    """Функция знакомит пользователя с правилами игры.

    Args:
        idgame: Description of idgame.
    """
    if idgame == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')
    elif idgame == 2:
        print('What is the result of the expression?')
    elif idgame == 3:
        print('Find the greatest common divisor of given numbers.')
    elif idgame == 4:
        print('What number is missing in the progression?')
    elif idgame == 5:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')


def ask_question(idgame, items):
    """Функция вопроса.

    Создает и выводит вопрос на экран.

    Args:
        idgame: Description of idgame.
        args: Description of args.
    """
    if idgame == 1:
        print('Question: {0}'.format(items['number']))
    elif idgame == 2:
        print('Question: {num1} {znak} {num2}'
              .format(num1=items['number1'],
                    znak=items['math_operator'],
                    num2=items['number2']
                    )
            )
    elif idgame == 3:
        print('Question: {num1} {num2}'.format(num1=items['number1'],
                                            num2=items['number2']
                                            )
            )


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
