import sys
from lexer import tokenize
from output import print_tokens, print_errors, print_table


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "test_input.txt"

    with open(filename, "r") as f:
        src = f.read()

    tokens, errors, table = tokenize(src)

    print_tokens(tokens)
    print_errors(errors)
    print_table(table)


main()