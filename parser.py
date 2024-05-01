import re
from ply.lex import lex
from ply.yacc import yacc
import math
import sys

tokens = ('INT', 'FLOAT', 'ID', 'STRING', 'IF', 'THEN', 'ELSE')

literals = ['+', '-', '*', '/', '(', ')', '^', '=', ';', '.', '%', ':', '"', '<', '>']

fs = {'sin' : math.sin, 'cos' : math.cos, 'inc' : lambda x: x + 1, 'dec' : lambda x: x - 1}

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_FLOAT (t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_IF (t):
    r'if\b'
    return t

def t_THEN (t):
    r'then\b'
    return t

def t_ELSE (t):
    r'else\b'
    return t

def t_ID (t):
    r'[A-Za-z]\w*'
    if (t.value in fs):
        t.type = 'TRIGNO'
        t.value = fs[t.value]
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


### GRAMÁTICA ### 
        
vars = {}

def p_z(t): "z : prog"                                          ; t[0] = f'{despejaVars(vars)}\nSTART\n{t[1]}\nSTOP'

def p_prog1(t): "prog : prog Instrucao "                        ; t[0] = f'{t[1]}\n{t[2]}'
def p_prog2(t): "prog : Instrucao "                             ; t[0] = t[1]

def p_Instrucao1(t): "Instrucao : Exp"                          ; t[0] = f'{t[1]}'
def p_Instrucao2(t): "Instrucao : '.'"                          ; t[0] = f'pop'
def p_Instrucao3(t): "Instrucao : '.' '\"' STRING '\"'"         ; t[0] = f'pushs {t[3]}\nwrites'
def p_Instrucao4(t): "Instrucao : Cond"                         ; t[0] = t[1]

def p_cond1(t): "Cond : IF Exp THEN '{' prog '}' Elseop"        ; t[0] = f'{t[2]}\n ftoi \n jz else \n {t[5]}\n\n{t[7]}\nend:'
def p_cond2(t): "Cond : IF Exp THEN prog Elseop"                ; t[0] = f'{t[2]}\n ftoi \n jz end \n {t[4]}\n\n{t[5]}\nend:'

def p_elseop1(t): "Elseop : ELSE '{' prog '}'"                  ; t[0] = f'else: \n{t[3]}'
def p_elseop2(t): "Elseop : ELSE prog"                          ; t[0] = f'else: \n{t[2]}'
def p_elseop3(t): "Elseop : "                                   ; t[0] = f'else: \n'

def p_Exp1(t): "Exp : '(' Exp ')'"                              ; t[0] = t[2]
def p_Exp2(t): "Exp : Expi"                                     ; t[0] = t[1]
def p_Exp3(t): "Exp : Expf"                                     ; t[0] = t[1]
def p_Exp4(t): "Exp : Exp '='"                                  ; t[0] = f'{t[1]}\nequal' #igualdade entre NUMEROS

def p_Expi1(t): "Expi : Lints"                                  ; t[0] = t[1]
def p_Expi2(t): "Expi : Expi '+'"                               ; t[0] = f'{t[1]}\nadd'
def p_Expi3(t): "Expi : Expi '-'"                               ; t[0] = f'{t[1]}\nsub'
def p_Expi4(t): "Expi : Expi '*'"                               ; t[0] = f'{t[1]}\nmul'
def p_Expi5(t): "Expi : Expi '/'"                               ; t[0] = f'{t[1]}\ndiv'
def p_Expi6(t): "Expi : Expi '%'"                               ; t[0] = f'{t[1]}\nmod'
def p_Expi7(t): "Expi : Expi '<'"                               ; t[0] = f'{t[1]}\ninf'
def p_Expi8(t): "Expi : Expi '<' '='"                               ; t[0] = f'{t[1]}\ninfeq'
def p_Expi9(t): "Expi : Expi '>'"                               ; t[0] = f'{t[1]}\nsup'
def p_Expi10(t): "Expi : Expi '>' '='"                          ; t[0] = f'{t[1]}\nsupeq'

def p_Expf1(t): "Expf : Lfloats"                                 ; t[0] = t[1]
def p_Expf2(t): "Expf : Expf '+'"                                ; t[0] = f'{t[1]}\nfadd'
def p_Expf3(t): "Expf : Expf '-'"                                ; t[0] = f'{t[1]}\nfsub'
def p_Expf4(t): "Expf : Expf '*'"                                ; t[0] = f'{t[1]}\nfmul'
def p_Expf5(t): "Expf : Expf '/'"                                ; t[0] = f'{t[1]}\nfdiv'
def p_Expf6(t): "Expf : Expf '%'"                                ; t[0] = f'{t[1]}\nfmod'
def p_Expf7(t): "Expf : Expf '<'"                                ; t[0] = f'{t[1]}\nfinf'
def p_Expf8(t): "Expf : Expf '<' '='"                           ; t[0] = f'{t[1]}\nfinfeq'
def p_Expf9(t): "Expf : Expf '>'"                               ; t[0] = f'{t[1]}\nfsup'
def p_Expf10(t): "Expf : Expf '>' '='"                          ; t[0] = f'{t[1]}\nfsupeq'

def p_Lnums1(t): "Lints : Termoi"                               ; t[0] = t[1]
def p_Lnums2(t): "Lints : Lints Termoi"                         ; t[0] = f'{t[1]}\n{t[2]}'
def p_Lnums3(t): "Lints : '-' Termoi"                           ; t[0] = f'pushi 0\n{t[2]}\nsub'

def p_Termoi1(t): "Termoi : INT"                                ; t[0] = f'pushi {t[1]}'
def p_Termoi2(t): "Termoi : INT '+'"                            ; t[0] = f'pushi {t[1]}\nadd'
def p_Termoi3(t): "Termoi : INT '-'"                            ; t[0] = f'pushi {t[1]}\nsub'
def p_Termoi4(t): "Termoi : INT '*'"                            ; t[0] = f'pushi {t[1]}\nmul'
def p_Termoi5(t): "Termoi : INT '/'"                            ; t[0] = f'pushi {t[1]}\ndiv'

def p_Lfloats1(t): "Lfloats : Termof"                           ; t[0] = t[1]
def p_Lfloats2(t): "Lfloats : Lfloats Termof"                   ; t[0] = f'{t[1]}\n{t[2]}'
def p_Lfloats3(t): "Lfloats : '-' Termof"                       ; t[0] = f'pushf 0\n{t[2]}\nfsub'

def p_Termof1(t): "Termof : FLOAT"                              ; t[0] = f'pushf {t[1]}'
def p_Termof2(t): "Termof : FLOAT '+'"                          ; t[0] = f'pushf {t[1]}\nfadd'
def p_Termof3(t): "Termof : FLOAT '-'"                          ; t[0] = f'pushf {t[1]}\nfsub'
def p_Termof4(t): "Termof : FLOAT '*'"                          ; t[0] = f'pushf {t[1]}\nfmul'
def p_Termof5(t): "Termof : FLOAT '/'"                          ; t[0] = f'pushf {t[1]}\nfdiv'

def p_error(t): 
    print(f"Erro de sintaxe: {t.value}, {t}")

def despejaVars (vars):
    return 'pushn 0\n' * len (vars)

def getoffSet (id):
    if (id in vars):
        return vars[id]
    else:
        vars[id] = len(vars)
        return vars[id]

parser = yacc()

program = open(sys.argv[1]).read()

print(parser.parse(program))
