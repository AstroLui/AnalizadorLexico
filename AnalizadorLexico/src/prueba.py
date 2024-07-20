import esprima

# Define your code string
code = """
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

def sintactico(texto):
  parsed_code = esprima.parseScript(texto)
  strCode = str(parsed_code)
  print(strCode)
  return strCode

sintactico(code)