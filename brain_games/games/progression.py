#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

"""Импортируем random."""
import random


def brain_progression():
    """Функция описывает матлогику игры
    и возвращает аргументы вопроса и правильного ответа
    id games"""
    rand_len_progression = random.randrange(5, 15, 1)
    rand_step = random.randrange(1, 10, 1)
    progression = [i for i in range(rand_step,
                                    rand_len_progression * rand_step + 1,
                                    rand_step)]
    rand_question_element = random.randrange(1, rand_len_progression, 1)
    correct_answer = progression[rand_question_element - 1]
    progression[rand_question_element - 1] = 0
    return {'correct_answer': correct_answer,
            'items': {'number': progression}
            }
