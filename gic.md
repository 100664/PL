"""

z -> prog '$'

prog -> prog Instrucao
      | Instrucao

Instrucao -> Print
           | Cond
           | Exp
           | Funcoes
           | Variaveis

Print -> '.'
       | CHAR ID
       | KEY Exp
       | SPACE
       | INT SPACES
       | STRING
       | EMIT
       | CR

Exp -> '(' Exp ')'
      | Expi
      | Exp '='

Expi -> Lints

Lints -> Termoi
       | Lints Termoi
       | '-' Termoi

Termoi -> INT
        | INT Lsinais
        | DUP
        | DUP Lsinais
        | 2DUP

Lsinais -> Sinal
         | Lsinais Sinal

Sinal -> '+'
       | '-'
       | '*'
       | '/'
       | '%'
       | '<'
       | '<' '='
       | '>'
       | '>' '='
       | '<' '>'

Cond -> Exp IF prog ELSE prog THEN
      | Exp IF prog THEN

Funcoes -> ':' NOME Definicao ';'
         | NOME
         | Exp NOME

Definicao -> Conteudo
           | Definicao Conteudo

Conteudo -> Lsinais
          | Exp
          | Print
          | Cond
          | NOME

Ciclo -> Lints DO '{' prog '}' LOOP
       | Lints DO Instrucao LOOP

Variaveis -> VARIABLE NOME
           | Exp NOME '!'
           | NOME '?'
           | NOME '@'



"""