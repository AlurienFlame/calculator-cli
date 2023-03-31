from dataclasses import dataclass
from enum import Enum

OperatorType = Enum("OperatorType", [
    "ADD",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
    "NEGATE"
])


@dataclass
class BinaryOperator:
    left: any
    op: any
    right: any

    def __repr__(self) -> str:
        return f"({self.left} {self.op} {self.right})"


@dataclass
class UnaryOperator:
    op: any
    right: any

    def __repr__(self) -> str:
        return f"({self.op} {self.right})"
