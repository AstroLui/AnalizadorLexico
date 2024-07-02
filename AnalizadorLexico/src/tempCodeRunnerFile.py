import ply.yacc as yacc
from lexema import tokens

precedence = (
    ('right', 'ASIGNAR'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('left', 'MAYOR', 'MENOR', 'MAYOR_IGUAL', 'MENOR_IGUAL'),
    ('left', 'AND', 'OR'),
)

def p_expression_binop(p):
    '''expression : expression SUMA expression
                   | expression RESTA expression
                   | expression MULT expression
                   | expression DIV expression'''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]

def p_expression_number(p):
    'expression : NUMERO'
    p[0] = p[1]

def p_expression_parentheses(p):
    'expression : PARENT_IZQ expression PARENT_DER'
    p[0] = p[2]

def p_error(p):
    print("Error de sintaxis en la entrada:", p)

def p_expression_assign(p):
    '''expression : ID ASIGNAR expression'''
    print("Asignación:", p[1], p[3])

def p_expression_and(p):
    '''expression : expression AND expression'''
    p[0] = p[1] and p[3]

def p_expression_or(p):
    '''expression : expression OR expression'''
    p[0] = p[1] or p[3]


yacc.yacc()

data = "1 AND 3"
result = yacc.parse(data)
print(result)