import ply.lex as lex

reservadas = {
  'IF': 'if', 'ELSE': 'else','INT': 'int','FLOAT': 'float','TRUE': 'true','FALSE': 'false','FOR': 'for','WHILE': 'while','LET': 'let','VAR': 'var', 'IMPORT': 'import','CLASS': 'class',
  'FUNCTION': 'function','DO': 'do','RETURN': 'return','BREAK': 'break','CONTINUE': 'continue','ABSTRACT': 'abstract','ARGUMENTS': 'arguments','BOOLEAN': 'boolean','BYTE': 'byte', 
  'CASE': 'case','CATCH': 'catch','CHAR': 'char','CONST': 'const','DEBUGGER': 'debugger','DEFAULT': 'default','DELETE': 'delete','ENUM': 'enum','EXPORT': 'export','EXTENDS': 'extends',
  'FINAL': 'final','FINALLY': 'finally','IN': 'in','INSTANCEOF': 'instanceof','LONG': 'long','NEW': 'new','NULL': 'null','OF': 'of','PACKAGE': 'package','PRIVATE': 'private',
  'PROTECTED': 'protected','PUBLIC': 'public','READONLY': 'readonly','SHORT': 'short','STATIC': 'static','SUPER': 'super','SWITCH': 'switch','SYNCHRONIZED': 'synchronized','THIS': 'this',
  'THROW': 'throw','THROWS': 'throws','TRANSIENT': 'transient','TRY': 'try','TYPEOF': 'typeof','UNDEFINED': 'undefined','VOID': 'void','VOLATILE': 'volatile','WITH': 'with',
  'YIELD': 'yield'}
tokens = list(reservadas.keys()) + ['ID', 'NUMERO', 'DECIMAL' 'STRING', 'ASIGNAR', 'SUMA', 'RESTA', 'DIV', 'MULT', 'COMA', 'PUNTO', 'MENOR', 'MAYOR', 'MODULO', 'MASMAS', 'MENOSMENOS', 'IGUAL', 
                                    'MAYOR_IGUAL', 'MENOR_IGUAL', 'DIFERENTE', 'AND', 'OR', 'NOT', 'PARENT_DER', 'PARENT_IZQ', 'CORCHETE_DER', 'CORCHETE_IZQ', 'LLAVE_DER', 'LLAVE_IZQ',
                                    'PUNTOCOMA', 'DOSPUNTOS', 'INTERROGACION']

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

def t_TRUE(t):
    r'true'
    return t

def t_FALSE(t):
    r'false'
    return t

def t_FOR(t):
    r'for'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_LET(t):
    r'let'
    return t

def t_VAR(t):
    r'var'
    return t

def t_IMPORT(t):
    r'import'
    return t

def t_CLASS(t):
    r'class'
    return t

def t_FUNCTION(t):
    r'function'
    return t

def t_DO(t):
    r'do'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_BREAK(t):
    r'break'
    return t

def t_CONTINUE(t):
    r'continue'
    return t

def t_ABSTRACT(t):
    r'abstract'
    return t

def t_INT(t):
    r'int'
    return t

def t_FLOAT(t):
    r'float'
    return t

def t_ARGUMENTS(t):
    r'arguments'
    return t

def t_BOOLEAN(t):
    r'boolean'
    return t

def t_BYTE(t):
    r'byte'
    return t

def t_CASE(t):
    r'case'
    return t

def t_CATCH(t):
    r'catch'
    return t

def t_CHAR(t):
    r'char'
    return t

def t_CONST(t):
    r'const'
    return t

def t_DEBUGGER(t):
    r'debugger'
    return t

def t_DELETE(t):
    r'delete'
    return t

def t_ENUM(t):
    r'enum'
    return t

def t_EXPORT(t):
    r'export'
    return t

def t_EXTENDS(t):
    r'extends'
    return t

def t_FINAL(t):
    r'final'
    return t

def t_FINALLY(t):
    r'finally'
    return t

def t_IN(t):
    r'in'
    return t

def t_INSTANCEOF(t):
    r'instanceof'
    return t

def t_LONG(t):
    r'long'
    return t

def t_NEW(t):
    r'new'
    return t

def t_NULL(t):
    r'null'
    return t

def t_OF(t):
    r'of'
    return t

def t_PACKAGE(t):
    r'package'
    return t

def t_PRIVATE(t):
    r'private'
    return t

def t_PROTECTED(t):
    r'protected'
    return t

def t_PUBLIC(t):
    r'public'
    return t

def t_READONLY(t):
    r'readonly'
    return t

def t_SHORT(t):
    r'short'
    return t

def t_SUPER(t):
    r'super'
    return t

def t_SWITCH(t):
    r'switch'
    return t

def t_SYNCHRONIZED(t):
    r'synchronized'
    return t

def t_THIS(t):
    r'this'
    return t

def t_THROW(t):
    r'throw'
    return t

def t_THROWS(t):
    r'throws'
    return t

def t_TRANSIENT(t):
    r'transient'
    return t

def t_TRY(t):
    r'try'
    return t

def t_TYPEOF(t):
    r'typeof'
    return t

def t_UNDEFINED(t):
    r'undefined'
    return t

def t_VOID(t):
    r'void'
    return t

def t_VOLATILE(t):
    r'volatile'
    return t

def t_WITH(t):
    r'with'
    return t

def t_YIELD(t):
    r'yield'
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t



def t_error(t):
    print("Carácter no válido: '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()

def Data(datos):
    data = datos
    lexer.input(data)
    stringData = ""
    while True:
        token = lexer.token()
        if not token:
            break
        stringData += (f"Tipo: {token.type}, Lexema: ( {token.value} )\n")
    return stringData

