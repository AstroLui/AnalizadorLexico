import re
import textwrap

def js_to_py(js_code):
    # Reemplaza let declarations con asignaciones directas
    js_code = re.sub(r'let (\w+);', r'\1 = None', js_code)
    
    js_code = re.sub(r'var (\w+)', r'\1', js_code)

    js_code = re.sub(r'let (\w+)', r'\1', js_code)

    js_code = re.sub(r'let (\w+);', r'\1', js_code)

    # Convert function declarations
    js_code = re.sub(r'(function\s+(\w+)\s*\(\s*\))\s*\{', r'def \2():\n    ', js_code)
    
    # Mantén la indentación original para el cuerpo de la función usando textwrap.dedent
    js_code = re.sub(r'(\n|^)\s+', r'\1', js_code, flags=re.MULTILINE)
    
    # Reemplaza bloques if con la sintaxis de Python y cambia las llaves por dos puntos
    js_code = re.sub(r'if\s+\((.*?)\)\s*\{', r'if \1:\n    ', js_code)
    js_code = re.sub(r'\{\s*', r':\n', js_code)
    
    # Asegura que las asignaciones estén bien formadas y maneja cadenas de texto correctamente
    js_code = re.sub(r'if\s+\((.*?)\)\s*\{\s*(\w+)\s*=\s*"([^"]+)"', r'if \1:\n    \2 = "\3"', js_code)
    
    # Simplified for loop conversion (assuming a simple case)
    js_code = re.sub(r'for\s+(\w+) in (.*?):', 'for \1 in \2:', js_code)
    
    # Asegura que la declaración de retorno esté bien formada
    js_code = re.sub(r'return\s+(.*)\s*;', 'return \1', js_code)
    
    # Elimina la última llave }
    js_code = re.sub(r'{\s*$', '', js_code)
    js_code = re.sub(r'{', '', js_code)
    js_code = re.sub(r'}\s*$', '', js_code)
    js_code = re.sub(r'}', '', js_code)
    
    # Utiliza textwrap.dedent para manejar la indentación dentro de las funciones
    js_code = textwrap.dedent(js_code)
    
    return js_code

# Llamada a la función con el código JavaScript proporcionado
js_code = """
function main(){
    if(x==2){
    x = "HOLA"}}
"""
print(js_to_py(js_code))



