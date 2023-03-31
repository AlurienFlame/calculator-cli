from dataclasses import dataclass
from tokens import TokenType, Token
from operators import *

# TODO: Switch to iterative approach using a stack
# TODO: Switch to functional approach


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = iter(tokens)

    def step_token(self):
        try:
            self.token = next(self.tokens)
        except StopIteration:
            self.token = None

    def parse(self):
        # Consume the iterator, replacing each token with nodes based on order of operations (the grammar)
        self.step_token()
        ast = self.add_or_sub()  # Outermost level
        return ast

    def add_or_sub(self):
        result = self.mul_or_div()  # Assume token is start of mult statement, move token past mult statement

        while self.token and self.token.type in (TokenType.PLUS, TokenType.MINUS):
            operator = self.token
            self.step_token()  # Step over operator
            if operator.type == TokenType.MINUS:
                result = BinaryOperator(result, OperatorType.SUBTRACT, self.mul_or_div())
            elif operator.type == TokenType.PLUS:
                result = BinaryOperator(result, OperatorType.ADD, self.mul_or_div())

        return result

    def mul_or_div(self):
        result = self.paren()

        while self.token and self.token.type in (TokenType. MUL, TokenType.DIV):
            operator = self.token
            self.step_token()
            if operator.type == TokenType.MUL:
                result = BinaryOperator(result, OperatorType.MULTIPLY, self.paren())
            elif operator.type == TokenType.DIV:
                result = BinaryOperator(result, OperatorType.DIVIDE, self.paren())

        return result

    def paren(self):
        if self.token.type == TokenType.LPAREN:
            self.step_token()
            result = self.add_or_sub()  # Treat inside of parens as top level
            if self.token.type != TokenType.RPAREN:
                raise Exception(f"Expected RPAREN, got {self.token}")
            self.step_token()
            return result
        return self.negative()

    def negative(self):
        if self.token.type == TokenType.MINUS:
            operator = self.token
            self.step_token()
            return UnaryOperator(OperatorType.NEGATE, self.add_or_sub())
        return self.constant()

    def constant(self):

        if self.token.type != TokenType.NUM:
            raise Exception(f"Expected NUM, got {self.token}")

        result = NullaryOperator(self.token.value)
        self.step_token()

        return result


def parse(tokens: list[Token]) -> any:
    return Parser(tokens).parse()
