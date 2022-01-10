#!/usr/bin/env python3
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
    return {
        'correct_answer': correct_answer,
        'items':
        {
            'number1': rand_num1,
            'number2': rand_num2
        }
    }
