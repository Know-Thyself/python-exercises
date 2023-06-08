def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

number1 = int(input('Enter a number\n'))
number2 = int(input('Enter a second number\n'))
for op in operations:
    print(op)
operation = input('Enter one of the above operation symbols to add, subtract, multiply or divide respectively\n')

def calculate(n1, n2, symbol):
    return operations[symbol](n1, n2)

answer = calculate(number1, number2, operation)
print(f'{number1} {operation} {number2} = {answer}')