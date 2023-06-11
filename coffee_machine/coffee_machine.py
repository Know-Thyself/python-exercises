from menu import MENU, resources

generated_income = 0


def start_machine():
    """
    Starts the coffee machine, asks for user inputs and invokes check_resources() function.
    """
    order = input('What would you like? Type "espresso", "latte" or "cappuccino"): ').lower()
    # 'report' and 'off' options are intended for admins
    if order == 'report':
        for ingredient in resources:
            if ingredient == 'coffee':
                print(f'{ingredient.title()}: {resources[ingredient]}g')
            else:
                print(f'{ingredient.title()}: {resources[ingredient]}ml')
        print(f'Generated income: ${format(generated_income, ".2f")}')
        start_machine()
    elif order == 'off':
        # servicing the machine and refilling
        return
    else:
        check_resources(MENU[order]['ingredients'], order, MENU[order]['cost'])


def check_resources(required_ingredients, coffee_type, price):
    """
    Checks if there are sufficient ingredients and calls the process_payment() function.
    :param required_ingredients:
    :type required_ingredients: dict
    :param coffee_type:
    :type coffee_type: str
    :param price:
    :type price: int
    """
    have_enough_ingredients = True
    for ingredient in required_ingredients:
        if resources[ingredient] < required_ingredients[ingredient]:
            have_enough_ingredients = False
        else:
            resources[ingredient] -= required_ingredients[ingredient]
    if have_enough_ingredients:
        process_payment(price, coffee_type)
    else:
        print("Sorry, we don't have enough ingredients. Restarting...")
        start_machine()


def process_payment(price, coffee_type):
    """
    Checks if the amount of coins inserted can cover the coffee price, returns the change and calls serve_coffee()
    function.
    :param price:
    :type price: int
    :param coffee_type:
    :type coffee_type: str
    """
    print(f'Please pay ${format(price, ".2f")}. We only accept coins')
    quarters = int(input('How many quarters? Type a number: '))
    dimes = int(input('How many dimes? Type a number: '))
    nickles = int(input('How many nickles? Type a number: '))
    pennies = int(input('How many pennies? Type a number: '))
    total_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total_paid < price:
        print(f"Insufficient amount here's your money: {total_paid}")
    else:
        print(f"Here's your change: ${format(total_paid - price, '.2f')}. Your {coffee_type} will be served shortly...")
        serve_coffee(price, coffee_type)


def serve_coffee(paid_amount, coffee_name):
    """
    Serves the coffee, updates generated income and invokes the start_machine() function to repeat the cycle.
    :param paid_amount:
    :type paid_amount: int
    :param coffee_name:
    :type coffee_name: str
    """
    global generated_income
    generated_income += paid_amount
    print(f"Here's your {coffee_name} ☕️. Enjoy!")
    has_more_order = input('Would you like more drinks? Type "y" for yes or "n" for no: ').lower()
    if has_more_order == 'y':
        start_machine()


start_machine()
