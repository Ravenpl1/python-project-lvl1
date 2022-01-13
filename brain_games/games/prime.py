# -*- coding: utf-8 -*- #

"""Импортируем random."""
import random


def brain_prime():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_num1 = random.randrange(0, 101, 1)
    num1_gcd = [i for i in range(1, rand_num1 + 1) if rand_num1 % i == 0]
    correct_answer = 'yes' if len(num1_gcd) == 2 else 'no'
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = 'Question: {0}'.format(rand_num1)
    return {'correct_answer': correct_answer,
            'rule': rule,
            'question': question
            }
