import sys
from ply.lex import lex
from ply.yacc import yacc
from lexer import *
from utils import *


def p_z(t):
    """z : prog EOF"""
    t[0] = f'\n{despejaVars(vars)}\nSTART\n{t[1]}\nSTOP\n\n{print_funcoes()}'

def p_prog1(t):
    """prog : prog Instrucao """
    t[0] = f'{t[1]}\n{t[2]}'

def p_prog2(t):
    """prog : Instrucao """
    t[0] = t[1]

#def p_Instrucao1(t): "Instrucao : Ciclo"
#                            ; t[0] = f'{t[1]}'

def p_Instrucao2(t):
    """Instrucao : Print """
    t[0] = f'{t[1]}'
    

def p_Instrucao3(t):
    """Instrucao : Cond """
    t[0] = f'{t[1]}'
    
def p_Instrucao4(t):
    """Instrucao : Exp """
    t[0] = f'{t[1]}'

def p_Instrucao5(t):
    """Instrucao : Funcoes """
    t[0] = f'{t[1]}'

def p_Instrucao6(t):
    """Instrucao : Variaveis """
    t[0] = f'{t[1]}'

def p_Print1(t):
    """Print : '.' """
    t[0] = f'writei'

def p_Print2(t):
    """Print : CHAR ID """
    t[0] = f'pushs "{t[2]}"\nchrcode'

def p_Print3(t):
    """Print : KEY Exp """
    t[0] = f'read'

def p_Print4(t):
    """Print : SPACE """
    t[0] = f'pushs " "\nwrites'

def p_Print5(t):
    """Print : INT SPACES """
    t[0] = f' ' * t[1]

def p_Print6(t):
    """Print : STRING """
    t[0] = f'pushs "{t[1][3:]}\nwrites'

def p_Print7(t):
    """Print : EMIT """
    t[0] = f'writechr'

def p_Print8(t):
    """Print : CR """
    t[0] = f'writeln'

def p_Exp1(t):
    """Exp : '(' Exp ')' """
    t[0] = t[2]

def p_Exp2(t):
    """Exp : Expi """
    t[0] = t[1]

def p_Exp3(t):
    """Exp : Exp '=' """
    t[0] = f'{t[1]}\nequal' #igualdade entre NUMEROS

def p_Expi1(t):
    """Expi : Lints """
    t[0] = t[1]

def p_Lnums1(t):
    """Lints : Termoi """
    t[0] = t[1]

def p_Lnums2(t):
    """Lints : Lints Termoi """
    t[0] = f'{t[1]}\n{t[2]}'

def p_Lnums3(t):
    """Lints : '-' Termoi """
    t[0] = f'pushi 0\n{t[2]}\nsub'

def p_Termoi1(t):
    """Termoi : INT """
    t[0] = f'pushi {t[1]}'

def p_Termoi2(t):
    """Termoi : INT Lsinais """
    t[0] = f'pushi {t[1]}\n{t[2]}'

def p_Termoi3(t):
    """Termoi : DUP """
    t[0] = f'dup 1'

def p_Termoi4(t):
    """Termoi : DUP Lsinais """
    t[0] = f'dup 1\n{t[3]}'

def p_Termoi5(t):
    """Termoi : 2DUP """
    t[0] = f'pushsp\nload-1\npushsp\nload-1'

def p_Termoi6(t):
    """Termoi : DROP """
    t[0] = f'pop 1'

def p_cond1(t):
    """Cond : Exp IF prog ELSE prog THEN """
    t[0] = f'{t[1]}\njz else{get_label_cond(t[2])}\n{t[3]}\njump endif{get_label_cond(t[6])}\nelse{get_label_cond(t[6])}:\n{t[5]}\nendif{get_label_cond(t[6])}:'

def p_cond3(t):
    """Cond : Exp IF prog THEN """
    t[0] = f'{t[1]}\njz else{get_label_cond(t[2])}\n{t[3]}\njump endif{get_label_cond(t[4])}\nelse{get_label_cond(t[4])}:\nendif{get_label_cond(t[4])}:'

def p_Lsinais1(t):
    """Lsinais : Sinal """
    t[0] = f'{t[1]}'

def p_Lsinais2(t):
    """Lsinais : Lsinais Sinal """
    t[0] = f'{t[1]}\n{t[2]}'

def p_Sinal1(t):
    """Sinal : '+' """
    t[0] = f'add'

def p_Sinal2(t):
    """Sinal : '-' """
    t[0] = f'sub'

def p_Sinal3(t):
    """Sinal : '*' """
    t[0] = f'mul'

def p_Sinal4(t):
    """Sinal : '/' """
    t[0] = f'div'

def p_Sinal5(t):
    """Sinal : '%' """
    t[0] = f'mod'

def p_Sinal6(t):
    """Sinal : '<' """
    t[0] = f'inf'

def p_Sinal7(t):
    """Sinal : '<' '=' """
    t[0] = f'infeq'

def p_Sinal8(t):
    """Sinal : '>' """
    t[0] = f'sup'

def p_Sinal9(t):
    """Sinal : '>' '=' """
    t[0] = f'supeq'

def p_Sinal10(t):
    """Sinal : '<' '>' """
    t[0] = f'not\nequal'

def p_Funcoes1(t):
    """Funcoes : ':' NOME Definicao ';' """
    t[0] = f''; define_funcao(t[2], t[3])

def p_Funcoes2(t):
    """Funcoes : NOME """
    t[0] = f'pusha {t[1]}\ncall'; funcs.get(t[1], 0)

def p_Funcoes3(t):
    """Funcoes : Exp NOME """
    t[0] = f'{t[1]}\npusha {t[2]}\ncall'; funcs.get(t[2], 0)

def p_Definicao1(t):
    """Definicao : Conteudo """
    t[0] = f'{t[1]}'

def p_Definicao2(t):
    """Definicao : Definicao Conteudo """
    t[0] = f'{t[1]}\n{t[2]}'

def p_Conteudo1(t):
    """Conteudo : Lsinais """
    t[0] = f'{t[1]}'

def p_Couteudo2(t):
    """Conteudo : Exp """
    t[0] = f'{t[1]}'

def p_Conteudo3(t):
    """Conteudo : Print """
    t[0] = f'{t[1]}'

def p_Conteudo4(t):
    """Conteudo : Cond """
    t[0] = f'{t[1]}'

def p_Conteudo5(t):
    """Conteudo : NOME """
    t[0] = funcs.get(t[1], 0)

#ciclos estao mal
def p_Ciclo1(t):
    """Ciclo : Lints DO '{' prog '}' LOOP """
    t[0] = f'while{get_label_loop(t[3])}:\npushi {t[1]}\npushi {t[2]}\npushn 0\nsup\njz endwhile{get_label_loop(t[4])}\n{t[5]}\n pushg 0\npushi 1\nadd\nstoreg 0\njump while{get_label_loop(t[4])}\nendwhile{get_label_loop(t[4])}:'

def p_Ciclo2(t):
    """Ciclo : Lints DO Instrucao LOOP """
    t[0] = f'while{get_label_loop(t[3])}:\npushi {t[1]}\npushi {t[2]}\npushn 0\nsup\njz endwhile{get_label_loop(t[4])}\n{t[4]}\n pushg 0\npushi 1\nadd\nstoreg 0\njump while{get_label_loop(t[4])}\nendwhile{get_label_loop(t[4])}:'

def p_Variaveis1(t):
    """Variaveis : VARIABLE NOME """
    t[0] = f''; vars[t[1]] = t[2]

def p_Variaveis2(t):
    """Variaveis : Exp NOME '!' """
    t[0] = f'{t[1]}\nstoreg {getoffSet(t[2])}'

def p_Variaveis3(t):
    """Variaveis : NOME '?' """
    t[0] = f'pushg {getoffSet(t[1])}\nwritei'

def p_Variaveis4(t):
    """Variaveis : NOME '@' """
    t[0] = f'pushg {getoffSet(t[1])}'

parser = yacc()

program = open(sys.argv[1]).read()

print(parser.parse(program))
