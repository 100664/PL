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
    r'[2|2][D|d][U|u][P|p]'
    return t

def t_INT(t):
    r'[+|-]?\d+'
    t.value = int(t.value)
    return t

def t_IF (t):
    r'[I|i][F|f]'
    return t

def t_THEN (t):
    r'[T|t][H|h][E|e][N|n]'
    return t

def t_ELSE(t):
    r'[E|e][L|l][S|s][E|e]'
    return t

def t_CHAR (t):
    r'[C|c][H|h][A|a][R|r]'
    return t

def t_EMIT(t):
    r'[E|e][M|m][I|i][T|t]'
    return t

def t_DO(t):
    r'[D|d][O|o]'
    return t

def t_LOOP(t):
    r'[L|l][O|o][O|o][P|p]'
    return t

def t_VARIABLE(t):
    r'[V|v][A|a][R|r][I|i][A|a][B|b][L|l][E|e]'
    return t

def t_CR(t):
    r'[C|c][R|r]'
    return t

def t_SPACE(t):
    r'[S|s][P|p][A|a][C|c][E|e]'
    return t

def t_SPACES(t):
    r'[S|s][P|p][A|a][C|c][E|e][S|s]'
    return t

def t_KEY(t):
    r'[K|k][E|e][Y|y]'
    return t

def t_DUP(t):
    r'[D|d][U|u][P|p]'
    return t

def t_DROP(t):
    r'[D|d][R|r][O|o][P|p]'
    return t

def t_SWAP(t):
    r'[S|s][W|w][A|a][P|p]'
    return t

def t_I(t):
    r'[I|i]'
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