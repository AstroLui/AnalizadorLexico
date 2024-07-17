import re
import textwrap

def js_to_py(js_code):
    # Reemplaza var declarations with let
    js_code = re.sub(r'var (\w+);', r'\1 = ', js_code)
    
    # Convert function declarations
    js_code = re.sub(r'(function\s+(\w+)\s*\(\s*\))\s*\{', r'def \2():\n\t', js_code)
    
    # Mantén la indentación original para el cuerpo de la función usando textwrap.dedent
    js_code = re.sub(r'^\s+', '', js_code, flags=re.MULTILINE).replace('\n', '\n    ')
    
    # Reemplaza console.log with print
    js_code = re.sub(r'console\.log\((.*?)\);', 'print(\1)', js_code)
    
    # Basic if statement conversion
    js_code = re.sub(r'if\s+(\w+)\s*\{\n\s*(.*?)}', 'if \1:\n\t\2', js_code, flags=re.DOTALL)
    
    # Simplified for loop conversion (assuming a simple case)
    js_code = re.sub(r'for\s+(\w+) in (.*?):', 'for \1 in \2:', js_code)
    
    # Asegura que la declaración de retorno esté bien formada
    js_code = re.sub(r'return\s+(.*)\s*;', 'return \1', js_code)
    
    # Elimina la última llave }
    js_code = re.sub(r'}\s*$', '', js_code)
    
    # Utiliza textwrap.dedent para manejar la indentación dentro de las funciones
    js_code = textwrap.dedent(js_code)
    
    return js_code

# Ejemplo de uso
js_code = """
function main(){
  int x = 5;
  x = hola;
}
"""

py_code = js_to_py(js_code)
print(py_code)



