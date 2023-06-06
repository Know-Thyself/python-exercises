counter = 0

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        counter = "FizzBuzz"
    elif number % 3 == 0:
        counter = "Fizz"
    elif number % 5 == 0:
        counter = "Buzz"
    else:
        counter = number
    print(counter)
