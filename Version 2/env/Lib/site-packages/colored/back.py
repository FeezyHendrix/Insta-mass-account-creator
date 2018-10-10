#!/usr/bin/python
# -*- coding: utf-8 -*-


from .colors import names


class back(object):

    ESC = '\x1b[48;5;'
    END = 'm'
    num = 0
    for color in names:
        vars()[color] = '{}{}{}'.format(ESC, num, END)
        num += 1
