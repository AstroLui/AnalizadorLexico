import esprima

def analizar_asignaciones(nodo):
    if nodo['type'] == 'VariableDeclaration':
        for declaracion in nodo['declarations']:
            nombre_variable = declaracion['id']['name']
            if declaracion.get('init'):
                valor = analizar_expresion(declaracion['init'])
                print(f"Asignación: {nombre_variable} = {valor}")

def analizar_expresion(nodo):
    if nodo['type'] == 'Literal':
        return nodo['value']
    elif nodo['type'] == 'BinaryExpression':
        valor_izquierdo = analizar_expresion(nodo['left'])
        operador = nodo['operator']
        valor_derecho = analizar_expresion(nodo['right'])
        return f"({valor_izquierdo} {operador} {valor_derecho})"

codigo_js = """
var x = 10;
var y = 20;
var z = x + y;
"""

arbol_sintaxis = esprima.parse(codigo_js)

analizar_asignaciones(arbol_sintaxis)