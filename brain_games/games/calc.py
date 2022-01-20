# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from random import SystemRandom

# Константы.
RULE = 'What is the result of the expression?'
LEN_RANDOM = (0, 10)


def get_round_data():
    """Функция игры brain-calc.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    math_operator = get_math_operator()
    number1, number2 = get_two_numbers()
    if math_operator == '+':
        correct_answer = number1 + number2
    elif math_operator == '-':
        correct_answer = number1 - number2
    elif math_operator == '*':
        correct_answer = number1 * number2
    question = '{n1} {op} {n2}'.format(
        n1=number1,
        op=math_operator,
        n2=number2,
    )
    return correct_answer, question


def get_math_operator():
    """Функция случайной генерации математического оператора.

    Returns:
        math_operations[rand_operator]: оператор.
    """
    cryptogen = SystemRandom()
    math_operations = ('+', '-', '*')
    rand_operator = cryptogen.randrange(len(math_operations))
    return math_operations[rand_operator]


def get_two_numbers():
    """Функция случайной генерации двух чисел.

    Returns:
        tupl: 2 числа.
    """
    cryptogen = SystemRandom()
    rand_num1 = cryptogen.randrange(*LEN_RANDOM)
    rand_num2 = cryptogen.randrange(*LEN_RANDOM)
    return rand_num1, rand_num2
