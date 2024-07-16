import re

def js_to_py(js_code):
    # Reemplaza var declarations with let
    js_code = re.sub(r'var (\w+);', r'\1 = ', js_code)
    
    # Convert function declarations
    js_code = re.sub(r'(function\s+(\w+)\s*\(\s*\))\s*\{', r'def \2(', js_code)
    
    # Mantén la indentación original para el cuerpo de la función
    js_code = re.sub(r'^\s+', '', js_code, flags=re.MULTILINE)
    
    # Reemplaza console.log with print
    js_code = re.sub(r'console\.log\((.*?)\);', 'print(\1)', js_code)
    
    # Basic if statement conversion
    js_code = re.sub(r'if\s+(\w+)\s*\{\n\s*(.*?)}', 'if \1:\n\t\2', js_code, flags=re.DOTALL)
    
    # Basic for loop conversion
    js_code = re.sub(r'for\s+(\w+)\s+=\s+0;\s+\w+\s+<\s+\d+;\s+\w+\s++\s*\{', 'for i in range(5):\n\ti += 1\n\t\2', js_code)
    
    # Asegura que la declaración de retorno esté bien formada
    js_code = re.sub(r'return\s+(.*)\s*;', 'return \1', js_code)
    
    return js_code

# Ejemplo de uso
js_code = """
function main(){
  int x = 5;
  x = "hola";
}
"""

py_code = js_to_py(js_code)
print(py_code)