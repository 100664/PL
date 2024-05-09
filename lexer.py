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
          'SPACES')

literals = ['+', '-', '*', '/', '(', ')', '^', '=', ';', '.', '%', ':', '"', '<', '>', '!', '?', '@']

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

def t_NOME(t):
    r'[A-Z]+\b'
    return t

def t_ID (t):
    r'[A-Za-z]'
    return t

def t_STRING (t):
    r'\".*?\"'
    t.value = t.value[1:-1]
    return t

t_ignore = ' \t\n'

def t_error(t):
    print("Caracter inválido: ", t.value[0])
    t.lexer.skip(1)


lexer = lex()

def lexer_debug (exemplo):
    lexer.input(exemplo)
    while token := lexer.token():
        print(token)