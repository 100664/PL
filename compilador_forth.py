import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'NUMBER',
    'DOT',
    'DUP',
    'SWAP',
    'OVER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE'
)

# Regras de expressão regular para tokens simples
t_DOT = r'\.'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

# Definição de token para números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco
t_ignore = ' \t'

# Manipulador de erro para caracteres inválidos
def t_error(t):
    print("Caráter inválido '%s'" % t.value[0])
    t.lexer.skip(1)

# Construindo o analisador léxico
lexer = lex.lex()

# Definição da gramática
def p_expression_stack(p):
    '''
    expression : expression NUMBER
               | expression DUP
               | expression SWAP
               | expression OVER
               | operation
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if p[2] == 'DUP':
            p[0] = p[1] + [p[1][-1]]
        elif p[2] == 'SWAP':
            p[0] = p[1][:-2] + [p[1][-1], p[1][-2]]
        elif p[2] == 'OVER':
            p[0] = p[1] + [p[1][-2]]
        else:
            p[0] = p[1] + [p[2]]

def p_expression_dot(p):
    'expression : expression DOT'
    print(p[1][-1])

def p_expression_number(p):
    'expression : NUMBER'
    p[0] = [p[1]]
    print(p[1])

def p_operation(p):
    '''
    operation : expression PLUS
              | expression MINUS
              | expression TIMES
              | expression DIVIDE
    '''
    if p[2] == '+':
        p[0] = p[1][:-2] + [p[1][-2] + p[1][-1]]
    elif p[2] == '-':
        p[0] = p[1][:-2] + [p[1][-2] - p[1][-1]]
    elif p[2] == '*':
        p[0] = p[1][:-2] + [p[1][-2] * p[1][-1]]
    elif p[2] == '/':
        p[0] = p[1][:-2] + [p[1][-2] / p[1][-1]]

# Manipulador de erro para a sintaxe incorreta
def p_error(p):
    print("Erro de sintaxe!")

# Construindo o analisador sintático
parser = yacc.yacc()

# Testando o interpretador
while True:
    try:
        s = input('Forth> ')
    except EOFError:
        break
    parser.parse(s)
