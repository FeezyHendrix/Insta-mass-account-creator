#!/usr/bin/python
# -*- coding: utf-8 -*-


class style(object):

    ESC = "\x1b["
    END = "m"

    names = {
        'BOLD': 1,
        'DIM': 2,
        'UNDERLINED': 4,
        'BLINK': 5,
        'REVERSE': 7,
        'HIDDEN': 8,
        'RESET': 0,
        'RES_BOLD': 21,
        'RES_DIM': 22,
        'RES_UNDERLINED': 24,
        'RES_BLINK': 25,
        'RES_REVERSE': 27,
        'RES_HIDDEN': 28
    }

    for color, num in names.items():
        vars()[color] = '{}{}{}'.format(ESC, num, END)
