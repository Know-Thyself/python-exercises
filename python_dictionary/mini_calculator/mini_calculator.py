from art import logo

print(logo)
print('Welcome to python mini calculator!')


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


def calculate(n1, n2, symbol):
	return operations[symbol](n1, n2)


is_continuous = True
while is_continuous:
	for op in operations:
		print(op)
	operation = input('Enter one of the above operation symbols to add, subtract, multiply or divide respectively\n')
	answer = calculate(number1, number2, operation)
	print(f'{number1} {operation} {number2} = {answer}')
	more_calculations = input('Would you like to do more calculation? Type "yes" to continue or "no" to exit\n')
	if more_calculations == 'no':
		is_continuous = False
	else:
		number1 = answer
		number2 = int(input('Enter a number\n'))
