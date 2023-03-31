from operators import OperatorType, BinaryOperator, UnaryOperator, NullaryOperator
resolve = {
    OperatorType.ADD: lambda left, right: left + right,
    OperatorType.SUBTRACT: lambda left, right: left - right,
    OperatorType.MULTIPLY: lambda left, right: left * right,
    OperatorType.DIVIDE: lambda left, right: left / right,
    OperatorType.NEGATE: lambda right: -right
}


def evaluate(ast):
    # Recursively evaluate the AST
    if isinstance(ast, BinaryOperator):
        return resolve[ast.op](evaluate(ast.left), evaluate(ast.right))
    elif isinstance(ast, UnaryOperator):
        return resolve[ast.op](evaluate(ast.right))
    elif isinstance(ast, NullaryOperator):
        return ast.value
    else:
        raise Exception(f"Unknown AST node type: {type(ast)}:{ast}")
    pass
