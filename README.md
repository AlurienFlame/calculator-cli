This project is a basic command line math interpreter written in Python. It supports addition, subtraction, multiplication, division, and parentheses for arithmetic expressions. The purpose of this project is to serve as a learning exercise for understanding the fundamentals of compilers. If the project were to be expanded, a library like Lark would be employed instead.

## Features

- Lexer: Tokenizes input strings into a list of tokens
- Parser: Parses the list of tokens into an abstract syntax tree (AST)
- Evaluator: Evaluates the AST to produce a numerical result

## Installation

To install the math interpreter, simply clone the repository:

```bash
git clone https://github.com/AlurienFlame/calculator-cli.git
cd calculator-cli
```
Note: This project was written using Python 3.10.10, and may not work with other versions.

## Usage

Run the math interpreter from the command line:

```bash
python3 main.py
```

Enter an arithmetic expression with supported operators (+, -, *, /, and parentheses):

```
> 2 + 3 * (4 - 1)
```

The interpreter will display the result, after some information about the internal process:

```
Tokens: [NUM, PLUS, NUM, MUL, LPAREN, NUM, MINUS, NUM, RPAREN]
Syntax Tree: (2.0 ADD (3.0 MULTIPLY (4.0 SUBTRACT 1.0)))
Result: 11.0
```

To exit the math interpreter, press `ctrl+C` or `ctrl+D` (keyboard interrupt or end of file).

## Limitations

This basic math interpreter only supports the following operators: addition (+), subtraction (-), multiplication (*), division (/), and parentheses. It does not handle complex expressions or other mathematical operations.