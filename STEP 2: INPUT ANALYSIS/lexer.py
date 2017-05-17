class Token(object):
    ILLEGAL_TOKEN = -1
    TOKEN_PLUS = 1
    TOKEN_MULT = 2
    TOKEN_DIV = 3
    TOKEN_SUB = 4
    TOKEN_OPEN_PAREN = 5
    TOKEN_CLOSE_PAREN = 6
    TOKEN_DOUBLE = 7
    TOKEN_NULL = 8

class Lexer(object):
    @classmethod
    def __init__(self, Expression):
        self.IExpression = Expression
        self.length = len(Expression)
        self.index = 0
        self.number = None
    @staticmethod
    def get_token(self):
        token = Token.ILLEGAL_TOKEN
        while self.index < self.length and (self.IExpression[self.index] == '' or self.IExpression[self.index] == '\t'):
            self.index += 1
        if self.index == self.length:
            return Token.TOKEN_NULL
        t = self.IExpression[self.index]
        switchCase = {
            '+' : token = Token.TOKEN_PLUS, self.index += 1,
            '-' : token = Token.TOKEN_SUB, self.index += 1,
            '*' : token = Token.TOKEN_MULT, self.index += 1,
            '/' : token = Token.TOKEN_DIV, self.index += 1,
            '(' : token = Token.TOKEN_OPEN_PAREN, self.index += 1,
            ')' : token = Token.TOKEN_CLOSE_PAREN, self.index += 1
        }
        return switchCase.get(t)