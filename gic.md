"""

z -> prog EOF

prog -> prog Instrucao
      | Instrucao

Instrucao -> Print
           | Cond
           | Exp
           | Funcoes
           | Variaveis
           | Ciclo

Print -> '.'
       | CHAR NOME
       | KEY
       | SPACE
       | INT SPACES
       | STRING
       | EMIT
       | CR

Exp -> '(' Exp ')'
     | Expi

Expi -> Lints
      | Lints Lcomps

Lcomps -> Comp
        | Lcomps Comp

Comp -> '='
      | '<'
      | '<' '='
      | '>'
      | '>' '='
      | '<' '>'

Lints -> Lints Termoi
       | Termoi

Termoi -> INT
        | INT Lsinais
        | DUP
        | DUP Lsinais
        | 2DUP
        | DROP
        | SWAP
        | I
        | I Lsinais

Lsinais -> Sinal
         | Lsinais Sinal

Sinal -> '+'
       | '-'
       | '*'
       | '/'
       | '%'

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
          | Ciclo

Cond -> Exp IF prog ELSE prog THEN
      | Exp IF prog THEN

Ciclo -> DO prog LOOP

Variaveis -> VARIABLE NOME
           | Exp NOME '!'
           | NOME '?'
           | NOME '@'


"""