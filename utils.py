vars = {}
funcs = {}
func_arg = {}
label_cond = 0
label_loop = 0
func_flag = 0

def p_error(t): 
    print(f"Erro de sintaxe: {t.value}, {t}")

def despejaVars (vars):
    return 'pushg 0\n' * (len (vars) - 1)


def define_funcao(nome, exp):
    func_arg[nome] = 0
    funcs[nome] = f'{exp}'
    global func_flag
    func_flag = 1
    for op in ['add', 'sub', 'mul', 'div', 'mod', 'inf', 'sup', 'equal']:
        if op in exp:
            func_arg[nome] += 1
    for op in ['pushi', 'pushsp\nload 0', ]:
        if op in exp:
            func_arg[nome] -= 1

def print_funcoes():
    global func_flag
    result = ''
    if func_flag == 1:
        for nome, exp in funcs.items():
            result += f'{nome}:\n'
            if (func_arg[nome] > 0):
                for i in (range(func_arg[nome]+1)):
                    if (func_arg[nome] - 1 > 0):
                        result += f'   pushfp\n   load {i - (func_arg[nome]+ 1)}\n'
            result += f'   {exp}\n'  
            if (func_arg[nome] -1 > 0): 
                result += f'   storeg {i+1}\n'
            result += f'   return\n'
    return result

def pop(nome):
    return func_arg[nome]+1

def getoffSet (id):
    if (id in vars):
        return vars[id]
    else:
        vars[id] = len(vars) - 1
        return vars[id]
    
def get_label_cond(s):
    global label_cond
    if s == "IF":
        label_cond += 1
    return label_cond

def get_label_loop(s):
    global label_loop
    if s == "DO":
        label_loop += 1
    return label_loop
