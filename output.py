def print_token(token):
    """Prints a valid token matching the required format."""
    print(f"Lexeme: {token.lexeme}, Token: {token.type}")

def print_error(message, line, col):
    """Prints an error matching the required format."""
    print(f"Error: {message} at line {line}, column {col}.")