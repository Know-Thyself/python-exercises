from menu import MENU, resources

generated_income = 0


def machine_setup():
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'report':
        for ingredient in resources:
            if ingredient == 'coffee':
                print(f'{ingredient.title()}: {resources[ingredient]}g')
            else:
                print(f'{ingredient.title()}: {resources[ingredient]}ml')
        print(f'Generated income: ${format(generated_income, ".2f")}')
        machine_setup()
    elif order == 'off':
        return
    else:
        check_resources(MENU[order]['ingredients'], order, MENU[order]['cost'])


def check_resources(required_ingredients, coffee_type, price):
    have_enough_ingredients = True
    for ingredient in required_ingredients:
        if resources[ingredient] < required_ingredients[ingredient]:
            have_enough_ingredients = False
        else:
            resources[ingredient] -= required_ingredients[ingredient]
    if have_enough_ingredients:
        print(f'Your {coffee_type} is getting prepared.')
        process_payment(price, coffee_type)
    else:
        print("Sorry, we don't have enough ingredients! Please come back later.")


def process_payment(price, coffee_type):
    print(f'Please pay ${format(price, ".2f")}. We only accept coins')
    quarters = int(input('How many quarters? Type a number: '))
    dimes = int(input('How many dimes? Type a number: '))
    nickles = int(input('How many nickles? Type a number: '))
    pennies = int(input('How many pennies? Type a number: '))
    total_paid = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total_paid < price:
        print(f"Insufficient amount here's your money: {total_paid}")
    else:
        print(f"Here's your change: ${round(total_paid - price, 2)}. Your {coffee_type} will be served shortly...")
        serve_coffee(price, coffee_type)


def serve_coffee(paid_amount, coffee_name):
    global generated_income
    generated_income += paid_amount
    print(f"Here's your {coffee_name} ☕️. Enjoy!")
    has_more_order = input('Would you like more drinks? Type "y" for yes or "n" for no: ')
    if has_more_order == 'y':
        machine_setup()


machine_setup()
