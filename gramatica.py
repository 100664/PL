import sys
from ply.lex import lex
from ply.yacc import yacc
from lexer import *
from utils import *

def p_z(t): "z : prog"                                          ; t[0] = f'{despejaVars(vars)}\nSTART\n{t[1]}\nSTOP'

def p_prog1(t): "prog : prog Instrucao "                        ; t[0] = f'{t[1]}\n{t[2]}'
def p_prog2(t): "prog : Instrucao "                             ; t[0] = t[1]

def p_Instrucao1(t): "Instrucao : Exp"                          ; t[0] = f'{t[1]}'
def p_Instrucao2(t): "Instrucao : '.'"                          ; t[0] = f'writei'
def p_Instrucao3(t): "Instrucao : '.' '\"' STRING '\"'"         ; t[0] = f'pushs {t[3]}\nwrites'
def p_Instrucao4(t): "Instrucao : CHAR ID"                      ; t[0] = f'pushs "{t[2]}"\nchrcode'
def p_Instrucao5(t): "Instrucao : EMIT"                         ; t[0] = f'writechr'
def p_Instrucao6(t): "Instrucao : Cond"                         ; t[0] = t[1]
def p_Instrucao7(t): "Instrucao : ':' Funcao ';'"               ; t[0] = t[2]

def p_Exp1(t): "Exp : '(' Exp ')'"                              ; t[0] = t[2]
def p_Exp2(t): "Exp : Expi"                                     ; t[0] = t[1]
def p_Exp3(t): "Exp : Exp '='"                                  ; t[0] = f'{t[1]}\nequal' #igualdade entre NUMEROS

def p_Expi1(t): "Expi : Lints"                                  ; t[0] = t[1]

def p_Lnums1(t): "Lints : Termoi"                               ; t[0] = t[1]
def p_Lnums2(t): "Lints : Lints Termoi"                         ; t[0] = f'{t[1]}\n{t[2]}'
def p_Lnums3(t): "Lints : '-' Termoi"                           ; t[0] = f'pushi 0\n{t[2]}\nsub'

def p_Termoi1(t): "Termoi : INT"                                ; t[0] = f'pushi {t[1]}'
def p_Termoi2(t): "Termoi : INT Sinal"                          ; t[0] = f'pushi {t[1]}\n{t[2]}'

def p_cond1(t): "Cond : IF Exp THEN '{' prog '}' Elseop"        ; t[0] = f'{t[2]}\n ftoi \n jz else \n {t[5]}\n\n{t[7]}\nend:'
def p_cond2(t): "Cond : IF Exp THEN prog Elseop"                ; t[0] = f'{t[2]}\n ftoi \n jz end \n {t[4]}\n\n{t[5]}\nend:'

def p_elseop1(t): "Elseop : ELSE '{' prog '}'"                  ; t[0] = f'else: \n{t[3]}'
def p_elseop2(t): "Elseop : ELSE prog"                          ; t[0] = f'else: \n{t[2]}'
def p_elseop3(t): "Elseop : "                                   ; t[0] = f'else: \n'

def p_Sinal1(t): "Sinal : '+'"                                  ; t[0] = f'add'
def p_Sinal2(t): "Sinal : '-'"                                  ; t[0] = f'sub'
def p_Sinal3(t): "Sinal : '*'"                                  ; t[0] = f'mul'
def p_Sinal4(t): "Sinal : '/'"                                  ; t[0] = f'div'
def p_Sinal5(t): "Sinal : '%'"                                  ; t[0] = f'mod'
def p_Sinal6(t): "Sinal : '<'"                                  ; t[0] = f'inf'
def p_Sinal7(t): "Sinal : '<' '='"                              ; t[0] = f'infeq'
def p_Sinal8(t): "Sinal : '>'"                                  ; t[0] = f'sup'
def p_Sinal9(t): "Sinal : '>' '='"                              ; t[0] = f'supeq'

def p_Funcao1(t): "Funcao : NFUNC Definicao"                    ; t[0] = f'{define_funcao(t[1], t[2])}'

def p_Definicao1(t): "Definicao : Conteudo"                     ; t[0] = f'{t[1]}'
def p_Definicao2(t): "Definicao : Definicao Conteudo"           ; t[0] = f'{t[1]}\n{t[2]}'

def p_Couteudo1(t): "Conteudo : Exp "                           ; t[0] = f'{t[1]}'
def p_Conteudo2(t): "Conteudo : Lsinais"                        ; t[0] = f'{t[1]}'

def p_Lsinais1(t): "Lsinais : Sinal"                            ; t[0] = f'{t[1]}'
def p_Lsinais2(t): "Lsinais : Lsinais Sinal"                    ; t[0] = f'{t[1]}\n{t[2]}'

parser = yacc()

program = open(sys.argv[1]).read()

print(parser.parse(program))