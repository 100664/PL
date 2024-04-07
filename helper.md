# GIC

```
S -> Exp '$'

Exp -> Termo Exp2

Exp2 ->  '+' Exp
    | '-' Exp
    | ε

Termo -> Fator Termo2

Termo2 -> '*' Termo2
    | '/' Termo2
    | ε

Fator -> num | id |  '(' Exp ')'

```