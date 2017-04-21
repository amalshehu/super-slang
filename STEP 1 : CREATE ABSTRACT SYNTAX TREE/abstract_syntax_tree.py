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
class BinaryExpression(Expression):
    def __init__(self, num1, num2, op):
        super (BinaryExpression, self).__init__(input1, input2, operator))
    def process(self):
        switcher = {
            self.operator = Operator.PLUS : input1.process() + input2.process(),
            self.operator = Operator.MINUS : input1.process() + input2.process(),
            self.operator = Operator.MULT : input1.process() + input2.process(),
            self.operator = Operator.DIV : input1.process() + input2.process()
        }
        return switcher.get(self, "None")
        
