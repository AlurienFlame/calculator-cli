from lexer import lex
from parser_ import parse
from evaluator import evaluate

while True:
    try:
        source = input("> ")
        tokens = lex(source)
        ast = parse(tokens)
        result = evaluate(ast)
        print(f"= {result}")
    except EOFError:
        print("quit")
        break
    except KeyboardInterrupt:
        print("quit")
        break
    except Exception as e:
        print(e)
