import math
import re
from ply.lex import lex

tokens = ('INT', 
          'STRING', 
          'IF', 
          'THEN', 
          'ELSE', 
          'CHAR', 
          'EMIT', 
          'NOME', 
          'DO', 
          'LOOP', 
          'VARIABLE', 
          'CR', 
          'SPACE', 
          'SPACES',
          'KEY',
          'DUP',
          '2DUP',
          'DROP',
          'EOF',
          'SWAP',
          'I'
        )

literals = ['+', '-', '*', '/', '(', ')', '^', '=', ';', '.', '%', ':', '"', '<', '>', '!', '?', '@']

def t_2DUP(t):
    r'2[Dd][Uu][Pp]'
    return t

def t_INT(t):
    r'[+-]?\d+'
    t.value = int(t.value)
    return t

def t_IF (t):
    r'[Ii][Ff]'
    return t

def t_THEN (t):
    r'[Tt][Hh][Ee][Nn]'
    return t

def t_ELSE(t):
    r'[Ee][Ll][Ss][Ee]'
    return t

def t_CHAR (t):
    r'[Cc][Hh][Aa][Rr]'
    return t

def t_EMIT(t):
    r'[Ee][Mm][Ii][Tt]'
    return t

def t_DO(t):
    r'[Dd][Oo]'
    return t

def t_LOOP(t):
    r'[Ll][Oo][Oo][Pp]'
    return t

def t_VARIABLE(t):
    r'[Vv][Aa][Rr][Ii][Aa][Bb][Ll][Ee]'
    return t

def t_CR(t):
    r'[Cc][Rr]'
    return t

def t_SPACE(t):
    r'[Ss][Pp][Aa][Cc][Ee]'
    return t

def t_SPACES(t):
    r'[Ss][Pp][Aa][Cc][Ee][Ss]'
    return t

def t_KEY(t):
    r'[Kk][Ee][Yy]'
    return t

def t_DUP(t):
    r'[Dd][Uu][Pp]'
    return t

def t_DROP(t):
    r'[Dd][Rr][Oo][Pp]'
    return t

def t_SWAP(t):
    r'[Ss][Ww][Aa][Pp]'
    return t

def t_I(t):
    r'[Ii]'
    return t

def t_EOF(t):
    r'\$'
    if hasattr(t.lexer, 'eof_returned'):
        res = None
    else:
        t.lexer.lineno += len(t.value)
        t.value = '$'
        t.type = 'EOF'  
        t.lexer.eof_returned = True
        res = t
    return res

def t_NOME(t):
    r'[A-Za-z0-9?!]+\b'
    return t

def t_STRING(t):
    r'\."\s*([^"]+)"'
    return t

t_ignore = ' \t\n'

def t_error(t):
    if t.value != '$':  # Evita processar o token de final de arquivo como caracter inválido
        print("Caracter inválido: ", t.value[0])
    t.lexer.skip(1)


lexer = lex()

def lexer_debug(exemplo):
    lexer.input(exemplo)
    while token := lexer.token():
        if token.type == 'EOF':  # Verificando se é o token de final de arquivo
            break
        print(token)