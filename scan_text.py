from tokens import Token, LexError


def scan_string(src, pos, line, col):
   
    start_pos = pos
    start_col = col
    quote = src[pos]

    pos += 1
    col += 1

    while pos < len(src):
        ch = src[pos]

        if ch == quote:
            pos += 1
            col += 1
            lexeme = src[start_pos:pos]
            return Token("STRING", lexeme, line, start_col), None, pos, line, col

        if ch == "\n":
            break

        if ch == "\\" and pos + 1 < len(src) and src[pos + 1] != "\n":
            pos += 2
            col += 2
            continue

        pos += 1
        col += 1

   
    error = LexError("unclosed string literal starting", line, start_col)
    return None, error, pos, line, col


def skip_comment(src, pos, line, col):
   
    start_line = line
    start_col = col

    
    if src.startswith("//", pos):
        while pos < len(src) and src[pos] != "\n":
            pos += 1
            col += 1
        
        return None, None, pos, line, col

    pos += 2
    col += 2

    while pos < len(src):
        if src.startswith("*/", pos):
            pos += 2
            col += 2
            return None, None, pos, line, col

        if src[pos] == "\n":
            line += 1
            col = 1
        else:
            col += 1
        pos += 1

  
    error = LexError("unclosed comment starting", start_line, start_col)
    return None, error, pos, line, col