#!/usr/bin/python3

from abc import ABCMeta, abstractmethod

class Operator(object):
    "' Declaration of Operators'"
    PLUS = "+"
    MINUS = "-"
    DIV = "/"
    MULT = "*"
class Expression(metaclass=ABCMeta):
    @abstractmethod
    def analyze(self):
        pass
class Numerary(Expression):
    "'Initialize the numeric property'"
    def __init__(self, val):
        self.val = val
    