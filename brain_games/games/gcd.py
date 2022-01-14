# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
from random import SystemRandom


def brain_gcd():
    """Функция игры brain-gcd.

    Returns:
        Dict: правильный ответ, правила, вопрос.
    """
    two_numbers = get_two_numbers()
    correct_answer = get_max_gcd(two_numbers)
    rule = 'Find the greatest common divisor of given numbers.'
    question = 'Question: {num1} {num2}'.format(
        num1=two_numbers[0],
        num2=two_numbers[1],
    )
    return {
        'correct_answer': correct_answer,
        'rule': rule,
        'question': question,
    }


def get_max_gcd(two_numbers):
    """Функция вычисления max делителя 2х чисел.

    Args:
        two_numbers: два числа в кортеже.

    Returns:
        int: наибольший делитель.
    """
    rand_num1 = two_numbers[0]
    rand_num2 = two_numbers[1]
    num1_gcd = devisors(rand_num1)
    num2_gcd = devisors(rand_num2)
    return max(list(set(num1_gcd) & set(num2_gcd)))


def get_two_numbers():
    """Функция случайной генерации двух чисел(1-100).

    Returns:
        tupl: 2 числа.
    """
    cryptogen = SystemRandom()
    rand_num1 = cryptogen.randrange(start=1, stop=100)
    rand_num2 = cryptogen.randrange(start=1, stop=100)
    return (rand_num1, rand_num2)


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
