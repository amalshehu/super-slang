#/usr/bin/python3

from abc import ABC, abstractmethod

class OPERATOR:
    PLUS = "+"
    MINUS = "-"
    DIV = "/"
    MUL = "*"

class Expression(ABC):
    @abstractmethod
    def analyze(self):
        pass
