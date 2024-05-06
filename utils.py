vars = {}
funcs = {}
label_cond = 0
label_loop = 0
func_flag = 0

def p_error(t): 
    print(f"Erro de sintaxe: {t.value}, {t}")

def despejaVars (vars):
    return 'pushg 0\n' * (len (vars) - 1)

def define_funcao(nome, exp):
    funcs[nome] = f'{exp}\nstoreg {len(funcs) - 1}'

def print_funcoes():
    result = f''
    if (func_flag == 1) :
        result = f'{funcs}pushfp\n'
        for key, value in funcs.items():
            result += f'{define_funcao(key, value)}\n'
        result += 'return'
        for key, value in funcs.items():
            result += f'\n{key}:\n {value}'
    return result

def getoffSet (id):
    if (id in vars):
        return vars[id]
    else:
        vars[id] = len(vars) - 1
        return vars[id]
    
def get_label_cond(s):
    global label
    if s == "IF":
        label_cond += 1
    return label_cond

def get_label_loop(s):
    global label_loop
    if s == "DO":
        label_loop += 1
    return label_loop
