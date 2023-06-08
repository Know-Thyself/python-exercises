# Write your code below this line 👇
def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
    elif number > 1:
        # Using for...else
        for i in range(2, number):
            if number % i == 0:
                print("It's not a prime number.")
                break
        else:
            print("It's a prime number.")


# Alternatively:
def prime_number_checker(number):
    is_Prime = True
    for i in range(2, number):
        if number % i == 0:
            is_Prime = False
            break
    if is_Prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
