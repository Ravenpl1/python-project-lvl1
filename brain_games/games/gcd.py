# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import random


def brain_gcd():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_num1 = random.randrange(1, 100, 1)
    rand_num2 = random.randrange(1, 100, 1)
    num1_gcd = [i for i in range(1, rand_num1 + 1) if rand_num1 % i == 0]
    num2_gcd = [i for i in range(1, rand_num2 + 1) if rand_num2 % i == 0]
    correct_answer = max(list(set(num1_gcd) & set(num2_gcd)))
    rule = 'Find the greatest common divisor of given numbers.'
    question = 'Question: {num1} {num2}'.format(num1=rand_num1,
                                                num2=rand_num2)
    return {'correct_answer': correct_answer,
            'rule': rule,
            'question': question
            }
