import re

def js_to_py(js_code):
    # Reemplaza var declarations with let
    js_code = re.sub(r'var (\w+);', r'let \1;', js_code)
    
    # Convert function declarations
    js_code = re.sub(r'(function\s+\w+\s*\(\s*\))\s*\{', r'def  ', js_code)
    js_code = re.sub(r'\}\s*(\w+)\s*;', r'\1)', js_code)
    
    # Replace console.log with print
    js_code = re.sub(r'console\.log\((.*?)\);', r'print(\1)', js_code)
    
    # Basic if statement conversion
    js_code = re.sub(r'if\s+(\w+)\s*\{\n\s*(.*?)}', r'if \1:\n\t\2', js_code, flags=re.DOTALL)
    
    # Basic for loop conversion
    js_code = re.sub(r'for\s+(\w+)\s+=\s+0;\s+\w+\s+<\s+\d+;\s+\w+\s++\s*\{', 'for i in range(5):\n\ti += 1\n\t\2', js_code)
    
    return js_code

# Ejemplo de uso
js_example = """
var name = "John";
function greet() {
    console.log("Hello " + name);
}
if (name == "John") {
    console.log(name);
}
for (var i = 0; i < 5; i++) {
    console.log(i);
}
"""

py_example = js_to_py(js_example)
print(py_example)


