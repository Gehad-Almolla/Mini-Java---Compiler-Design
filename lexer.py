from tokens import Token, LexError
from scan_ident import scan_identifier
from scan_symbols import scan_number, scan_operator, scan_delimiter
from scan_text import scan_string, skip_comment
from symbol_table import SymbolTable

DELIMITERS = "(){}[];,."
OPERATOR_CHARS = "+-*/%=<>!&|"


def digit_start_is_identifier(src, pos):
    # look at the whole word that starts with a digit
    # "25" -> number,  "1name" -> bad identifier
    i = pos
    while i < len(src) and (src[i].isalnum() or src[i] == "_"):
        i += 1
    word = src[pos:i]
    return not word.isdigit()


def tokenize(src):
    tokens = []
    errors = []
    table = SymbolTable()

    pos = 0
    line = 1
    col = 1

    while pos < len(src):
        ch = src[pos]

        # 1) whitespace
        if ch == "\n":
            pos += 1
            line += 1
            col = 1
            continue
        if ch in " \t\r":
            pos += 1
            col += 1
            continue

        token = None
        error = None

        # 2) comments (must be checked before operators because of "/")
        if src.startswith("//", pos) or src.startswith("/*", pos):
            token, error, new_pos, new_line, new_col = skip_comment(src, pos, line, col)

        # 3) words: identifiers, keywords, true/false
        elif ch.isalpha() or ch == "_":
            token, error, new_pos, new_line, new_col = scan_identifier(src, pos, line, col)

        # 4) things that start with a digit
        elif ch.isdigit():
            if digit_start_is_identifier(src, pos):
                token, error, new_pos, new_line, new_col = scan_identifier(src, pos, line, col)
            else:
                token, error, new_pos, new_line, new_col = scan_number(src, pos, line, col)

        # 5) strings
        elif ch == '"' or ch == "'":
            token, error, new_pos, new_line, new_col = scan_string(src, pos, line, col)

        # 6) delimiters
        elif ch in DELIMITERS:
            token, error, new_pos, new_line, new_col = scan_delimiter(src, pos, line, col)

        # 7) operators
        elif ch in OPERATOR_CHARS:
            token, error, new_pos, new_line, new_col = scan_operator(src, pos, line, col)

        # 8) anything else is an illegal character
        else:
            error = LexError("invalid character '" + ch + "'", line, col)
            new_pos = pos + 1
            new_line = line
            new_col = col + 1

        if token is None and error is None and new_pos <= pos:
            error = LexError("invalid character '" + ch + "'", line, col)

        # safety: never get stuck in an infinite loop
        if new_pos <= pos:
            new_pos = pos + 1
            new_col = col + 1

        if token is not None:
            tokens.append(token)
            if token.type == "IDENTIFIER":
                table.insert(token.lexeme, token.line, token.col)
        if error is not None:
            errors.append(error)

        pos, line, col = new_pos, new_line, new_col

    return tokens, errors, table