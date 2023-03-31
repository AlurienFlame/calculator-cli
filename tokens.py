from dataclasses import dataclass
from enum import Enum

TokenType = Enum("TokenType", [
    "WHITESPACE",
    "NUM",
    "PLUS",
    "MINUS",
    "MUL",
    "DIV",
    "LPAREN",
    "RPAREN"
])

chars = {
    TokenType.WHITESPACE: " \t",
    TokenType.NUM: "0123456789.",
    TokenType.PLUS: "+",
    TokenType.MINUS: "-",
    TokenType.MUL: "*",
    TokenType.DIV: "/",
    TokenType.LPAREN: "(",
    TokenType.RPAREN: ")",
}


@dataclass
class Token:
    type: str
    value: str

    def __init__(self, type, value=None) -> None:
        self.type = type
        self.value = value

    def __repr__(self) -> str:
        return self.type.name
