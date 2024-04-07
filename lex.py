import ply.lex as lex

tokens = ('+', '-', '*', '/', ')', '(', '$', 'num')

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    
t_ignore = " \t"

def t_error(t):
    print("Caráter inválido '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

prox_simb = ('Erro', '', 0, 0)

class Node:
    def __init__(self, type):
        self.type = type

class Exp(Node):
    pass
    
class Exp2(Node):
    pass
    
class Termo(Node):
    pass
    
class Termo2(Node):
    def rec_Termo2():
        global prox_simb
        if prox_simb.type == '*':
            rec_Term('*')
            rec_Termo()
        elif prox_simb.type == '/':
            rec_Term('/')
            rec_Termo()
        elif prox_simb.type in ['+', '-', ')', '$']:
            pass
        else:
            # CAPTURA DE ERRO (erro sintático)
            pass
    
class Fator(Node):
    pass
    
def rec_parser (data): 
    global prox_simb
    lexer.input(data)
    prox_simb = lexer.token() #primeiro token
    Exp()   