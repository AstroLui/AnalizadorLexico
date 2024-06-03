import ply.lex as lex

reservadas = {'IF': 'if', 'ELSE': 'else', 'GET': 'get', 'INT': 'int', 'FLOAT': 'float'}
tokens = list(reservadas.keys()) + ['ID', 'NUMERO', 'STRING', 'ASIGNAR', 'SUMA', 'RESTA', 'DIV', 'MULT', 'COMA', 'PUNTO', 'MENOR', 'MAYOR', 'MODULO', 'MASMAS', 'MENOSMENOS', 'IGUAL', 
                                    'MAYOR_IGUAL', 'MENOR_IGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT']

t_SUMA = r'\+'
t_RESTA = r'\-'
t_ASIGNAR = r'='
t_MASMAS = r'\++'
t_MENOSMENOS = r'\--'
t_MENOR = r'\<'
t_MAYOR = r'\>'
t_DIV = r'/'
t_MULT = r'\*'
t_COMA = r'\,'
t_MODULO = r'\%'
t_IGUAL = r'\=='
t_MAYOR_IGUAL = r'\>='
t_MENOR_IGUAL = r'\<='
t_DIFERENTE = r'\!='
t_AND = r'\&&'
t_OR = r'\|\|'
t_NOT = r'\!'
t_ignore = r' \n'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_STRING(t):
    r'\"(.*?)\"'
    t.value = t.value[1:-1]
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t



def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()


data = "if else jota123 = 3, + 4 * 2 && ||"
lexer.input(data)

while True:
    token = lexer.token()
    if not token:
        break
    print(f"Tipo: {token.type}, Lexema: ({token.value}), Posición: {token.lexpos}")

