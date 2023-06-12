from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


def run_coffee_machine():
    options = menu.get_items()
    order = input(f"What would you like? Type {options} ")
    if order == "report":
        ingredients_report = coffee_maker.report()
        cash_report = money_machine.report()
        print(ingredients_report)
        print(cash_report)
        run_coffee_machine()
    elif order == "off":
        return
    else:
        drink = menu.find_drink(order)
        is_available = coffee_maker.is_resource_sufficient(drink)
        if is_available:
            has_paid = money_machine.make_payment(drink.cost)
            if has_paid:
                coffee_maker.make_coffee(drink)
                wants_more = input("Would you like more drinks? Type 'y' for yes or 'n' to exit: ")
                if wants_more == 'y':
                    run_coffee_machine()


run_coffee_machine()
