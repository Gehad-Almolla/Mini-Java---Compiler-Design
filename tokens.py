# Shared by everyone. Don't change the names without telling the team!
from dataclasses import dataclass

@dataclass
class Token:
    type: str      # CLASS, IDENTIFIER, NUMBER ...
    lexeme: str    # the actual text
    line: int
    col: int

@dataclass
class LexError:
    message: str   # example: "invalid character '@'"  (no line/col inside)
    line: int
    col: int



''' Token names to use:
  Keywords: CLASS PUBLIC STATIC VOID INT FLOAT BOOLEAN_TYPE CHAR STRING_TYPE IF ELSE WHILE FOR RETURN
  Others: IDENTIFIER NUMBER STRING BOOLEAN ASSIGN MATHOP LOGOP
  Delimiters: LPAR RPAR LCUR RCUR LSQU RSQU SEMICOLON COMMA DOT


  Every scanner function must look like this:
    def scan_xxx(src, pos, line, col):
        return token, error, new_pos, new_line, new_col

  token / error = None if there is nothing to return.
  new_pos MUST be bigger than pos (positions always move forward). '''