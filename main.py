from lexer import lex
from parser_ import parse
from evaluator import evaluate

while True:
    try:
        source = input("> ")
        tokens = lex(source)
        print(f"Tokens: {tokens}")
        ast = parse(tokens)
        print(f"Syntax Tree: {ast}")
        result = evaluate(ast)
        print(f"Result: {result}")
    except EOFError:
        print("quit")
        break
    except KeyboardInterrupt:
        print("quit")
        break
    except Exception as e:
        print(e)
