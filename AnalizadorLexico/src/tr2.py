import re
import sys

def translate_js_to_py(js_code):
    translations = {
        r'var\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'let\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'const\s+(\w+)\s*=\s*(.*);': r'\1 = \2',
        r'function\s+(\w+)\((.*)\)\s*{': r'def \1(\2):',
        r'console\.log\((.*)\);': r'print(\1)',
        r'if\s*\((.*)\)\s*{': r'if \1:',
        r'else\s*if\s*\((.*)\)\s*{': r'elif \1:',
        r'else\s*{': r'else:',
        r'for\s*\((.*);(.*);(.*)\)\s*{': r'for \1 in range(\2, \3):',
        r'while\s*\((.*)\)\s*{': r'while \1:',
        r'}': r'',
        r'(\w+)\.push\((.*)\);': r'\1.append(\2)',
    }

    py_code = js_code
    for js_pattern, py_replacement in translations.items():
        py_code = re.sub(js_pattern, py_replacement, py_code)
    
    indent_level = 0
    py_lines = []
    for line in py_code.split('\n'):
        stripped_line = line.strip()
        if stripped_line.endswith(':') and not stripped_line.startswith('#'):
            py_lines.append('    ' * indent_level + stripped_line)
            indent_level += 1
        elif stripped_line == '':
            py_lines.append('')
        else:
            if indent_level > 0 and stripped_line == '}':
                indent_level -= 1
            py_lines.append('    ' * indent_level + stripped_line)
    
    return '\n'.join(py_lines)

js = """
let number1 = 10;
let number2 = 20;
let message = "Hello!";

number1 = 15;
number2 = number1 + 5;

console.log("Number 1:", number1);
console.log("Number 2:", number2);
console.log("Message:", message);

let counter = 0;
while (counter < 5) {
  console.log("Counter:", counter);
  counter++;
}

let isAdult = false;
let age = 18;

if (age >= 18) {
  isAdult = true;
  console.log("You are an adult.");
} else {
  console.log("You are not an adult.");
}

let numbers = [1, 2, 3, 4, 5];

console.log("First element:", numbers[0]);
console.log("Last element:", numbers[numbers.length - 1]);

numbers[2] = 10;
console.log("Modified array:", numbers);

for (let i = 0; i < numbers.length; i++) {
  console.log("Element at index", i, ":", numbers[i]);
}

let person = {
  name: "John Doe",
  age: 30,
  occupation: "Software Engineer",
};

console.log("Person's name:", person.name);
console.log("Person's age:", person.age);

person.occupation = "Web Developer";
console.log("Modified occupation:", person.occupation);

person.city = "New York";
console.log("New property:", person.city);
"""

print(translate_js_to_py(js))