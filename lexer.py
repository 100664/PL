import math
import re
from ply.lex import lex

tokens = ('INT', 
          'ID', 
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
    r'2DUP\b'
    return t

def t_INT(t):
    r'[+|-]?\d+'
    t.value = int(t.value)
    return t

def t_IF (t):
    r'IF\b'
    return t

def t_THEN (t):
    r'THEN\b'
    return t

def t_ELSE (t):
    r'ELSE\b'
    return t

def t_CHAR (t):
    r'CHAR\b'
    return t

def t_EMIT(t):
    r'EMIT\b'
    return t

def t_DO(t):
    r'DO\b'
    return t

def t_LOOP(t):
    r'LOOP\b'
    return t

def t_VARIABLE(t):
    r'VARIABLE\b'
    return t

def t_CR(t):
    r'CR\b'
    return t

def t_SPACE(t):
    r'SPACE\b'
    return t

def t_SPACES(t):
    r'SPACES\b'
    return t

def t_KEY(t):
    r'KEY\b'
    return t

def t_DUP(t):
    r'DUP\b'
    return t

def t_DROP(t):
    r'DROP\b'
    return t

def t_SWAP(t):
    r'SWAP\b'
    return t

def t_I(t):
    r'I\b'
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
    r'[A-Za-z0-9?]+\b'
    return t

def t_ID (t):
    r'[A-Za-z]'
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