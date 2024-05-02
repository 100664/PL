vars = {}
funcs = {}
label = 0

def p_error(t): 
    print(f"Erro de sintaxe: {t.value}, {t}")

def despejaVars (vars):
    return 'pushg 0\n' * len (vars)

def define_funcao(nome, exp):
    funcs[nome] = f'{exp}\nstoreg {len(funcs) - 1}'
    return f'{exp}\nstoreg {len(funcs) - 1}'

def getoffSet (id):
    if (id in vars):
        return vars[id]
    else:
        vars[id] = len(vars)
        return vars[id]
    
def get_label(s):
    global label
    if s == "IF":
        label += 1
    return label
