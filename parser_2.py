import math
import sys
from ply.lex import lex
from ply.yacc import yacc

tokens = ('NUM','ID', 'LER', 'STRING', 'IF', 'THEN', 'ELSE')

literals = ['+', '-', '*', '/', '%', '(', ')', '^', '=', ';', '.']

fs = {'log': math.log, 'exp': math.exp, 'sin': math.sin, 'inc': lambda x: x+1}

def t_NUM(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

def t_IF(t):
    r'if\b'
    return t

def t_THEN(t):
    r'then\b'
    return t

def t_ELSE(t):
    r'else\b'
    return t

def t_LER(t):
    r'ler\b'
    return t

def t_ID(t):
    r'[A-Za-z]\w*'
    if t.value in fs:
        t.type = 'FUNC1'
        t.value = fs[t.value]
    return t

def t_STRING(t):
    r'".*?"' #aceita tudo
    t.value = t.value[1:-1] # remover as aspas duplas
    return t

def t_COMMENT(t):
    r'\#.*'

t_ignore = ' \t\n'

def t_error(t):
    print(f"Caracter inválido: {t.value[0]}")
    t.lexer.skip(1)
    
lexer = lex()

def lexer_debug (exemplo):
    lexer.input(exemplo)
    while token := lexer.token():
        print(token)
        
#lexer_debug(exemplo)

#Gramática

vars = {}

def p_z(t): "z : prog"                             ; t[0] = f'{despejaVars(vars)}\nSTART\n{t[1]}\nSTOP'

def p_prog1(t): "prog : Instrucao prog"             ; t[0] = f'{t[1]}\n{t[2]}'
def p_prog2(t): "prog : Instrucao '.' prog"         ; t[0] = f''

def p_Eq1(t) : "Instrucao : ID '=' Exp"             ; t[0] = f'{t[3]}\n storeg {getOffSet(t[1])}' #vars[t[1]]  = t[3]
def p_Eq2(t) : "Instrucao : Exp"                    ; t[0] = f'{t[1]}\n writef' #t[1]
def p_Eq3(t) : "Instrucao : cond"

def p_cond1(t): "cond : IF Exp THEN '{' prog '}' elseop" ; t[0] = f'{t[2]}\n ftoi \n jz else \n {t[5]}\n\n{t[7]}\nend:'
def p_cond2(t): "cond : IF Exp THEN prog elseop"      ; t[0] = f'{t[2]}\n ftoi \n jz else \n {t[4]}\n\n{t[5]}end:'

def p_elseop1(t): "elseop : ELSE '{' prog '}'"      ; t[0] = f'else: \n{t[3]}'
def p_elseop2(t): "elseop : ELSE prog"              ; t[0] = 'else: \n{t[2]}'
def p_elseop3(t): "elseop : "                       ; t[0] = 'else: \n'

def p_Exp1(t) : "Exp : parcela"                     ; t[0] = t[1]
def p_Exp2(t) : "Exp : Exp parcela '+'"             ; t[0] = f'{t[1]}\n{t[2]}\nfadd'  #t[1] + t[3]
def p_Exp3(t) : "Exp : Exp parcela '-' "             ; t[0] = f'{t[1]}\n{t[2]}\nfsub'  #t[1] - t[3]

def p_parcela1(t) : "parcela : fator"               ; t[0] = t[1]
def p_parcela2(t) : "parcela : parcela fator '*'"   ; t[0] = f'{t[1]}\n{t[2]}\nfmul'  #t[1] * t[3]
def p_parcela3(t) : "parcela : parcela  fator '/'"   ; t[0] = f'{t[1]}\n{t[2]}\nfdiv'  #t[1] / t[3]

def p_fator1(t) : "fator : termo"                   ; t[0] = t[1]
def p_fator2(t) : "fator : termo fator '^'"         ; t[0] = t[1] ** t[2]
def p_fator3(t) : "fator : termo fator '%'"         ; t[0] = f'{t[1]}\n{t[2]}\nfmod'

def p_termo1(t) : "termo : '(' Exp ')'"             ; t[0] = t[2]
def p_termo2(t) : "termo : NUM"                     ; t[0] = f'pushf {t[1]}' #t[1]
def p_termo3(t) : "termo : NUM '-'"                 ; t[0] = f'pushf 0 \n {t[1]} \n fsub' #-t[2]
def p_termo4(t) : "termo : NUM '+'"                 ; t[0] = t[1]
def p_termo5(t) : "termo : ID"                      ; t[0] = f'pushg {getOffSet(t[1])}' #vars.get(t[1], 0) #t[1] caso esta definida em vars, 0 caso contrário
def p_termo7(t) : "termo : LER '(' STRING ')'"      ; t[0] = f'pushs "{t[3]}"\n writes \n read \n atof'

def p_error(t):
    print(f"Erro de sintaxe: {t.value}, {t}")

def despejaVars (vars):
    return 'pushf 0\n' * len(vars)

def getOffSet(id):
    if(id in vars):
        return vars[id]
    else:
        vars[id] = len(vars)
        return vars[id]

parser = yacc()
 
programa = open(sys.argv[1]).read()
    
    
print(parser.parse(programa))