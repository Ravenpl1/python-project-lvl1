#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем prompt, random."""
import random


def brain_even():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_num1 = random.randrange(0, 100, 1)
    correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
    return {'correct_answer': correct_answer,
            'items': {'number': rand_num1}
            }
