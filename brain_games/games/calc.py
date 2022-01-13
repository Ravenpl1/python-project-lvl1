# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from random import SystemRandom


def brain_calc():
    """Функция игры brain-calc.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    math_operator = get_math_operator()
    two_numbers = get_two_numbers()
    if math_operator == '+':
        correct_answer = two_numbers[0] + two_numbers[1]
    elif math_operator == '-':
        correct_answer = two_numbers[0] - two_numbers[1]
    elif math_operator == '*':
        correct_answer = two_numbers[0] * two_numbers[1]
    rule = 'What is the result of the expression?'
    question = 'Question: {n1} {op} {n2}'.format(
        n1=two_numbers[0],
        op=math_operator,
        n2=two_numbers[1],
    )
    return {
        'correct_answer': correct_answer,
        'rule': rule,
        'question': question,
    }


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
    rand_num1 = cryptogen.randrange(start=0, stop=10)
    rand_num2 = cryptogen.randrange(start=0, stop=10)
    return (rand_num1, rand_num2)
