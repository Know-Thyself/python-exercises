def add(*args):
    result = 0
    for n in args:
        result += n
    return result


def calculate(**kwargs):
    result = 0
    for key, value in kwargs.items():
        if key == "num" or key == "add":
            result += value
        else:
            result *= value
    print(result)


# unlimited positional arguments can be passed
total = add(1, 2, 3, 4)
print(total)
calculate(num=3, add=4, multiply=4)
