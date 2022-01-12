#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем random."""
import random


def brain_even():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_num1 = random.randrange(0, 100, 1)
    correct_answer = 'yes' if rand_num1 % 2 == 0 else 'no'
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = 'Question: {0}'.format(rand_num1)
    return {'correct_answer': correct_answer,
            'rule': rule,
            'question': question
            }
