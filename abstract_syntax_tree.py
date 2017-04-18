#/usr/bin/python3

#Imports
from abc import ABC, abstractmethod

class Operator(object):
    "' Declaration of Operators'"
    PLUS = "+"
    MINUS = "-"
    DIV = "/"
    MULT = "*"

class Expression(ABC):
    @abstractmethod
    def analyze(self):
        pass
