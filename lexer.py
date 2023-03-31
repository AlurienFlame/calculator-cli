from tokens import *

def lex(source: str) -> list[Token]:
    tokens = []

    # Step through characters in the source code
    i = 0
    while i < len(source):
        current_char = source[i]

        # Ignore whitespace
        if current_char in chars[TokenType.WHITESPACE]:
            pass
        elif current_char in chars[TokenType.NUM]:
            # Build up a number token
            num_str = current_char
            i += 1
            while i < len(source) and source[i] in chars[TokenType.NUM]:
                if source[i] == "." and "." in num_str:
                    # TODO: Fancy error handling
                    raise Exception(f"{i}: Tokenizer Error: Unexpected '.' after number '{num_str}'")
                num_str += source[i]
                i += 1

            tokens.append(Token(TokenType.NUM, float(num_str)))
            continue
        # TODO: To this dynamically
        elif current_char in chars[TokenType.PLUS]:
            tokens.append(Token(TokenType.PLUS))
        elif current_char in chars[TokenType.MINUS]:
            tokens.append(Token(TokenType.MINUS))
        elif current_char in chars[TokenType.MUL]:
            tokens.append(Token(TokenType.MUL))
        elif current_char in chars[TokenType.DIV]:
            tokens.append(Token(TokenType.DIV))
        elif current_char in chars[TokenType.LPAREN]:
            tokens.append(Token(TokenType.LPAREN))
        elif current_char in chars[TokenType.RPAREN]:
            tokens.append(Token(TokenType.RPAREN))
        else:
            raise Exception(f"{i}: Tokenizer Error: Unexpected character '{current_char}'")
        i += 1

    print(f"Tokens: {tokens}")
    return tokens
