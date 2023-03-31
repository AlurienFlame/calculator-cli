from dataclasses import dataclass
from enum import Enum

OperatorType = Enum("OperatorType", [
    "ADD",
    "SUBTRACT",
    "MULTIPLY",
    "DIVIDE",
    "NEGATE",
    "NULL"
])


@dataclass
class BinaryOperator:
    left: any
    op: any
    right: any

    def __repr__(self) -> str:
        return f"({self.left} {self.op.name} {self.right})"


@dataclass
class UnaryOperator:
    op: any
    right: any

    def __repr__(self) -> str:
        return f"({self.op.name} {self.right})"


@dataclass
class NullaryOperator:
    value: any

    def __repr__(self) -> str:
        return f"{self.value}"
