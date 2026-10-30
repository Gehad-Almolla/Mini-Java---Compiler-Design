
from tokens import Token, LexError


# Case-sensitive keywords
KEYWORDS = {
    "class": "CLASS",
    "public": "PUBLIC",
    "static": "STATIC",
    "void": "VOID",
    "int": "INT",
    "float": "FLOAT",
    "boolean": "BOOLEAN_TYPE",
    "char": "CHAR",
    "String": "STRING_TYPE",
    "if": "IF",
    "else": "ELSE",
    "while": "WHILE",
    "for": "FOR",
    "return": "RETURN",
}


def is_identifier_start(ch):
    """
    An identifier must start with a letter or underscore.
    """
    return ch.isalpha() or ch == "_"


def is_identifier_part(ch):
    """
    After the first character, an identifier can contain
    letters, digits, or underscores.
    """
    return ch.isalnum() or ch == "_"


def scan_identifier(src, pos, line, col):
    """
    Scan an identifier, keyword, boolean, or invalid identifier.

    Returns:
        token, error, new_pos, new_line, new_col
    """

    start_pos = pos
    start_col = col

    # 1. Read the complete word
    while pos < len(src) and is_identifier_part(src[pos]):
        pos += 1
        col += 1

    word = src[start_pos:pos]

    # 2. Invalid identifier: starts with a digit
    if word[0].isdigit():
        error = LexError(
            f"invalid identifier '{word}'",
            line,
            start_col
        )

        return None, error, pos, line, col

    # 3. Boolean values
    if word == "true" or word == "false":
        token = Token(
            "BOOLEAN",
            word,
            line,
            start_col
        )

        return token, None, pos, line, col

    # 4. Keywords
    if word in KEYWORDS:
        token = Token(
            KEYWORDS[word],
            word,
            line,
            start_col
        )

        return token, None, pos, line, col

    # 5. Regular identifier
    token = Token(
        "IDENTIFIER",
        word,
        line,
        start_col
    )

    return token, None, pos, line, col
