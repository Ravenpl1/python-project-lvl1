# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from random import SystemRandom

# Константы.
LEN_RANDOM = (0, 100)


def brain_gcd():
    """Функция игры brain-gcd.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    number1, number2 = get_two_numbers()
    correct_answer = get_max_gcd(number1, number2)
    question = '{num1} {num2}'.format(
        num1=number1,
        num2=number2,
    )
    return correct_answer, question


def get_max_gcd(number1, number2):
    """Функция вычисления max делителя 2х чисел.

    Args:
        number1: число 1.
        number2: число 2.

    Returns:
        int: наибольший делитель.
    """
    num1_gcd = devisors(number1)
    num2_gcd = devisors(number2)
    return max(list(set(num1_gcd) & set(num2_gcd)))


def get_two_numbers():
    """Функция случайной генерации двух чисел.

    Returns:
        tupl: 2 числа.
    """
    cryptogen = SystemRandom()
    rand_num1 = cryptogen.randrange(*LEN_RANDOM)
    rand_num2 = cryptogen.randrange(*LEN_RANDOM)
    return rand_num1, rand_num2


def devisors(number):
    """Функция генерации списка делителей.

    Args:
        number: число.

    Returns:
        list: список делителей.
    """
    gcd = []
    for element in range(1, number + 1):
        if number % element == 0:
            gcd.append(element)
    return gcd
