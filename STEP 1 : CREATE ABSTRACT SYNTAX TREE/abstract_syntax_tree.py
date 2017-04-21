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
    def process(self):
        pass
class NumericConstant(Expression):
    "'Initialize the numeric property'"
    def __init__(self, value):
        if not isinstance(value, int, float):
            raise TypeError("Error01:Invalid type")
        self.numeric = value
    def process(self):
        return self.numeric
    def __str__(self):
        return self.numeric

