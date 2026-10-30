from tokens import Token

OPERATORS = {
    "==": "LOGOP", "!=": "LOGOP", "<=": "LOGOP", ">=": "LOGOP",
    "<": "LOGOP", ">": "LOGOP",
    "=": "ASSIGN",
    "+": "MATHOP", "-": "MATHOP", "*": "MATHOP", "/": "MATHOP", "%": "MATHOP",
}

PARS = {
    "(": "LPAR", ")": "RPAR",
    "{": "LCUR", "}": "RCUR",
    "[": "LSQU", "]": "RSQU",
    ";": "SEMICOLON", ",": "COMMA", ".": "DOT",
}


def scan_number(src, pos, line, col):
    start = pos

    while pos < len(src) and src[pos].isdigit():
        pos += 1

    if pos + 1 < len(src) and src[pos] == "." and src[pos + 1].isdigit():
        pos += 1
        while pos < len(src) and src[pos].isdigit():
            pos += 1

    # 1name is an invalid identifier, not a number
    if pos < len(src) and (src[pos].isalpha() or src[pos] == "_"):
        return None, None, start, line, col

    lexeme = src[start:pos]
    return Token("NUMBER", lexeme, line, col), None, pos, line, col + len(lexeme)


def scan_operator(src, pos, line, col):
    two = src[pos:pos + 2]
    if two in OPERATORS:
        return Token(OPERATORS[two], two, line, col), None, pos + 2, line, col + 2

    one = src[pos]
    if one in OPERATORS:
        return Token(OPERATORS[one], one, line, col), None, pos + 1, line, col + 1

    return None, None, pos, line, col


def scan_delimiter(src, pos, line, col):
    ch = src[pos]
    if ch in PARS:
        return Token(PARS[ch], ch, line, col), None, pos + 1, line, col + 1

    return None, None, pos, line, col
