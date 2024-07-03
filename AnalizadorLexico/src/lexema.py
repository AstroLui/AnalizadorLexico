import ply.lex as lex

reservadas = {
 'IF': 'if', 'ELSE': 'else','INT': 'int','FLOAT': 'float','TRUE': 'true','FALSE': 'false','FOR': 'for','WHILE': 'while','LET': 'let','VAR': 'var', 'IMPORT': 'import','CLASS': 'class',
 'FUNCTION': 'function','DO': 'do','RETURN': 'return','BREAK': 'break','CONTINUE': 'continue','ABSTRACT': 'abstract','ARGUMENTS': 'arguments','BOOLEAN': 'boolean','BYTE': 'byte', 
 'CASE': 'case','CATCH': 'catch','CHAR': 'char','CONST': 'const','DEBUGGER': 'debugger','DEFAULT': 'default','DELETE': 'delete','ENUM': 'enum','EXPORT': 'export','EXTENDS': 'extends',
 'FINAL': 'final','FINALLY': 'finally','IN': 'in','INSTANCEOF': 'instanceof','LONG': 'long','NEW': 'new','NULL': 'null','OF': 'of','PACKAGE': 'package','PRIVATE': 'private',
 'PROTECTED': 'protected','PUBLIC': 'public','READONLY': 'readonly','SHORT': 'short','STATIC': 'static','SUPER': 'super','SWITCH': 'switch','SYNCHRONIZED': 'synchronized','THIS': 'this',
 'THROW': 'throw','THROWS': 'throws','TRANSIENT': 'transient','TRY': 'try','TYPEOF': 'typeof','UNDEFINED': 'undefined','VOID': 'void','VOLATILE': 'volatile','WITH': 'with',
 'YIELD': 'yield'}

tokens = ['ID', 'NUMERO', 'DECIMAL', 'STRING', 'ASIGNAR', 'SUMA', 'RESTA', 'DIV', 'MULT', 'COMA', 'PUNTO', 'MENOR', 'MAYOR', 'MODULO', 'IGUAL', 
         'MAYOR_IGUAL', 'MENOR_IGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT', 'PARENT_DER', 'PARENT_IZQ', 'CORCHETE_DER', 'CORCHETE_IZQ', 'LLAVE_DER', 'LLAVE_IZQ',
         'PUNTOCOMA', 'DOSPUNTOS', 'INTERROGACION', 'PALABRA_RESERVADA']

t_SUMA = r'\+'
t_RESTA = r'\-'
t_ASIGNAR = r'='
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
t_PARENT_DER = r'\)'
t_PARENT_IZQ = r'\('
t_CORCHETE_DER = r'\]'
t_CORCHETE_IZQ = r'\['
t_LLAVE_DER = r'\}'
t_LLAVE_IZQ = r'\{'
t_PUNTO = r'\.'
t_PUNTOCOMA = r'\;'
t_DOSPUNTOS = r'\:'
t_INTERROGACION = r'\?'
t_ignore = r' \n'

def t_NUMERO(t):
  r'\d+'
  t.value = int(t.value)
  return t

def t_STRING(t):
  r'\"(.*?)\"'
  t.value = t.value[1:-1]
  return t

def t_ID(t):
  r'[a-zA-Z_][a-zA-Z_0-9]*'
  if t.value.upper() in reservadas:
    t.type = 'PALABRA_RESERVADA'
  return t

def t_error(t):
  print("Carácter no válido: '%s'" % t.value[0])
  t.lexer.skip(1)


lexer = lex.lex()


def Data(datos):
    data = datos
    lexer.input(data)
    stringData = ""
    datas = []
    while True:
        token = lexer.token()
        if not token:
            break
        stringData += (f"Tipo: {token.type}, Lexema: ( {token.value} )\n")
        datas.append((token.type, token.value))
    diccionarioData = dict(zip(range(len(datas)), datas))
    return diccionarioData

