"""

z : prog '$'

prog : Instrucao ';' prog
    | Instrucao ';'" 
    | Intrucao '.' prog

Instrucao : parcela
    | parcela '+' Exp
    | parcela '-' Exp
    
parcela : fator
    | fator '*' parcela
    | fator '/' parcela
    
fator: termo
    | termo '^' fator
    
termo: '(' Exp ')'
    | NUM
    


"""