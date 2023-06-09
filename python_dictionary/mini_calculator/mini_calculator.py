from art import logo

print("Welcome to python mini calculator!")


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculate(n1, n2, symbol):
    return operations[symbol](n1, n2)


def calculator():
    print(logo)
    number1 = float(input("Enter a number\n"))
    is_continuous = True
    while is_continuous:
        for op in operations:
            print(op)
        operation = input("Enter one of the above operation symbols\n")
        number2 = float(input("Enter a second number\n"))
        answer = calculate(number1, number2, operation)
        print(f"{number1} {operation} {number2} = {answer}")
        more_calculations = input(
            'Type "y" to continue calculating, "r" to '
            'restart or "n" to exit\n'
        )
        if more_calculations == "y":
            number1 = answer
        elif more_calculations == "r":
            calculator()
        else:
            is_continuous = False


calculator()
