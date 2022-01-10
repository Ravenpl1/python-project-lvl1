#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import random


def brain_calc():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    math_operations = ('+', '-', '*')
    rand_math_operation = random.choice(math_operations)
    rand_num1 = random.randrange(0, 10, 1)
    rand_num2 = random.randrange(0, 10, 1)
    if rand_math_operation == '+':
        correct_answer = rand_num1 + rand_num2
    elif rand_math_operation == '-':
        correct_answer = rand_num1 - rand_num2
    elif rand_math_operation == '*':
        correct_answer = rand_num1 * rand_num2
    return {
        'correct_answer': correct_answer,
        'items': 
        {
            'number1': rand_num1,
            'math_operator': rand_math_operation,
            'number2': rand_num2
        }
    }
