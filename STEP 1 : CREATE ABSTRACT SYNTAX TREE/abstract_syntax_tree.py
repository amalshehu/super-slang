#!/usr/bin/python3

from abc import ABCMeta, abstractmethod
import operator

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
        if not isinstance(value, int):
            raise TypeError("Slang Error 01:Invalid type")
        self.numeric = value
    def process(self):
        return self.numeric
    def __str__(self):
        return self.numeric
class BinaryExpression(Expression):
    def __init__(self, a, b, op):
        self.input1 = a
        self.input2 = b
        self.operator = op
    def process(self):
        switcher = {
            Operator.PLUS : operator.add(self.input1.process(), self.input2.process()),
            Operator.MINUS : operator.sub(self.input1.process(), self.input2.process()),
            Operator.MULT : operator.mul(self.input1.process(), self.input2.process()),
            Operator.DIV : operator.truediv(self.input1.process(), self.input2.process())
        }
        return switcher.get(self.operator)
    def __str__(self):
        return "BinaryExp(%s %s %s)" % (self.input1, self.input2, self.operator)

class UnaryExpression(Expression):
    def __init__(self, i, op):
        self.input = i
        self.operator = op
    def process(self):
        if self.operator == Operator.PLUS:
            return self.input.process()
        elif self.operator == Operator.MINUS:
            return -self.input.process()
        else:
            None
if __name__ == "__main__":
    # Abstract Syntax Tree(AST) for 5*4
    exp = BinaryExpression(NumericConstant(5), NumericConstant(5), Operator.MULT)
    print(exp.process())
    exp2 = BinaryExpression(NumericConstant(5), NumericConstant(5), Operator.PLUS)
    print(exp2.process())
