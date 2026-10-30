def print_tokens(tokens):
    for t in tokens:
        print_token(t)

def print_errors(errors):
    for e in errors:
        print_error(e.message, e.line, e.col)

def print_table(table):
    table.print_table()

def print_token(token):
    """Prints a valid token matching the required format."""
    print(f"Lexeme: {token.lexeme}, Token: {token.type}")

def print_error(message, line, col):
    """Prints an error matching the required format."""
    print(f"Error: {message} at line {line}, column {col}.")

