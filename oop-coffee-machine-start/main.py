from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_off = False

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu_object = Menu()

while not is_off:
    preference = input(f"What would you like? ({menu_object.get_items()}):").lower()


    if preference == "report":
        coffee_maker.report()
        money_machine.report()

    elif preference == "off":
        is_off = True

    else:
        drink = menu_object.find_drink(preference)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)




