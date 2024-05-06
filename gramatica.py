import sys
from ply.lex import lex
from ply.yacc import yacc
from lexer import *
from utils import *


def p_z(t): "z : prog"                                              ; t[0] = f'\n{despejaVars(vars)}\nSTART\n{t[1]}\n\nSTOP\n';

def p_prog1(t): "prog : prog Instrucao "                            ; t[0] = f'{t[1]}\n{t[2]}'
def p_prog2(t): "prog : Instrucao "                                 ; t[0] = t[1]

#def p_Instrucao1(t): "Instrucao : Ciclo"                            ; t[0] = f'{t[1]}'
def p_Instrucao2(t): "Instrucao : Exp"                              ; t[0] = f'{t[1]}'
def p_Instrucao3(t): "Instrucao : Print"                            ; t[0] = f'{t[1]}'
def p_Instrucao4(t): "Instrucao : Cond"                             ; t[0] = t[1]
def p_Instrucao5(t): "Instrucao : ':' Funcao ';'"                   ; t[0] = t[2]
def p_Instrucao6(t): "Instrucao : Variaveis"                        ; t[0] = t[1]

def p_Print1(t): "Print : Exp '.'"                                  ; t[0] = f'{t[1]}\nwritei'
def p_Print2(t): "Print : CHAR ID"                                  ; t[0] = f'pushs "{t[2]}"\nchrcode'
def p_Print3(t): "Print : SPACE"                                    ; t[0] = f' '
def p_Print4(t): "Print : SPACES INT"                               ; t[0] = f' ' * t[2]
def p_Print5(t): "Print : '.' STRING"                               ; t[0] = f'pushs "{t[2]}"'
def p_Print6(t): "Print : STRING '.'"                               ; t[0] = f'writes'
def p_Print7(t): "Print : EMIT"                                     ; t[0] = f'writechr'
def p_Print8(t): "Print : CR"                                       ; t[0] = f'\n'

def p_Exp1(t): "Exp : '(' Exp ')'"                                  ; t[0] = t[2]
def p_Exp2(t): "Exp : Expi"                                         ; t[0] = t[1]
def p_Exp3(t): "Exp : Exp '='"                                      ; t[0] = f'{t[1]}\nequal' #igualdade entre NUMEROS

def p_Expi1(t): "Expi : Lints"                                      ; t[0] = t[1]

def p_Lnums1(t): "Lints : Termoi"                                   ; t[0] = t[1]
def p_Lnums2(t): "Lints : Lints Termoi"                             ; t[0] = f'{t[1]}\n{t[2]}'
def p_Lnums3(t): "Lints : '-' Termoi"                               ; t[0] = f'pushi 0\n{t[2]}\nsub'

def p_Termoi1(t): "Termoi : INT"                                    ; t[0] = f'pushi {t[1]}'
def p_Termoi2(t): "Termoi : INT Lsinais"                              ; t[0] = f'pushi {t[1]}\n{t[2]}'
def p_Termoi3(t): "Termoi : VARIABLE"                               ; t[0] = vars.get(t[1], 0)

def p_cond1(t): "Cond : IF Exp THEN '{' prog '}' ELSE '{' prog '}'" ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[5]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\n{t[9]}\nendif{get_label_cond(t[3])}:'
def p_cond2(t): "Cond : IF Exp THEN '{' prog '}' ELSE Instrucao"    ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[5]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\n{t[8]}\nendif{get_label_cond(t[3])}:'
def p_cond3(t): "Cond : IF Exp THEN '{' prog '}'"                   ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[5]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\nendif{get_label_cond(t[3])}:'
def p_cond4(t): "Cond : IF Exp THEN Instrucao ELSE '{' prog '}'"    ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[4]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\n{t[7]}\nendif{get_label_cond(t[3])}:'
def p_cond5(t): "Cond : IF Exp THEN Instrucao ELSE Instrucao"       ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[4]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\n{t[6]}\nendif{get_label_cond(t[3])}:'
def p_cond6(t): "Cond : IF Exp THEN Instrucao"                      ; t[0] = f'{t[2]}\njz else{get_label_cond(t[1])}\n{t[4]}\njump endif{get_label_cond(t[3])}\nelse{get_label_cond(t[3])}:\nendif{get_label_cond(t[3])}:'

def p_Sinal1(t): "Sinal : '+'"                                      ; t[0] = f'add'
def p_Sinal2(t): "Sinal : '-'"                                      ; t[0] = f'sub'
def p_Sinal3(t): "Sinal : '*'"                                      ; t[0] = f'mul'
def p_Sinal4(t): "Sinal : '/'"                                      ; t[0] = f'div'
def p_Sinal5(t): "Sinal : '%'"                                      ; t[0] = f'mod'
def p_Sinal6(t): "Sinal : '<'"                                      ; t[0] = f'inf'
def p_Sinal7(t): "Sinal : '<' '='"                                  ; t[0] = f'infeq'
def p_Sinal8(t): "Sinal : '>'"                                      ; t[0] = f'sup'
def p_Sinal9(t): "Sinal : '>' '='"                                  ; t[0] = f'supeq'

def p_Funcao1(t): "Funcao : NOME Definicao"                        ; t[0] = f'{define_funcao(t[1], t[2])}'

def p_Definicao1(t): "Definicao : Conteudo"                         ; t[0] = f'{t[1]}'
def p_Definicao2(t): "Definicao : Definicao Conteudo"               ; t[0] = f'{t[1]}\n{t[2]}'

def p_Couteudo1(t): "Conteudo : Exp "                               ; t[0] = f'{t[1]}'
def p_Conteudo2(t): "Conteudo : Lsinais"                            ; t[0] = f'{t[1]}'
def p_Conteudo3(t): "Conteudo : Print"                              ; t[0] = f'{t[1]}'
def p_Conteudo4(t): "Conteudo : Cond"                               ; t[0] = f'{t[1]}'

def p_Lsinais1(t): "Lsinais : Sinal"                                ; t[0] = f'{t[1]}'
def p_Lsinais2(t): "Lsinais : Lsinais Sinal"                        ; t[0] = f'{t[1]}\n{t[2]}'


#ciclos estao mal
def p_Ciclo1(t) : "Ciclo : INT INT DO '{' prog '}' LOOP"             ; t[0] = f'while{get_label_loop(t[3])}:\npushi {t[1]}\npushi {t[2]}\npushn 0\nsup\njz endwhile{get_label_loop(t[4])}\n{t[5]}\n pushg 0\npushi 1\nadd\nstoreg 0\njump while{get_label_loop(t[4])}\nendwhile{get_label_loop(t[4])}:'
def p_Ciclo2(t) : "Ciclo : INT INT DO Instrucao LOOP"                ; t[0] = f'while{get_label_loop(t[3])}:\npushi {t[1]}\npushi {t[2]}\npushn 0\nsup\njz endwhile{get_label_loop(t[4])}\n{t[4]}\n pushg 0\npushi 1\nadd\nstoreg 0\njump while{get_label_loop(t[4])}\nendwhile{get_label_loop(t[4])}:'

def p_Variaveis1(t): "Variaveis : VARIABLE NOME"               ; t[0] = f''; vars[t[1]] = t[2]
def p_Variaveis2(t): "Variaveis : Exp NOME '!'"                ; t[0] = f'{t[1]}\nstoreg {getoffSet(t[2])}'
def p_Variaveis3(t): "Variaveis : NOME '?'"                    ; t[0] = f'pushg {getoffSet(t[1])}\nwritei'

parser = yacc()

program = open(sys.argv[1]).read()

print(parser.parse(program))