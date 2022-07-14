from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()

end_state = False
while not end_state:
    drink = input(f"what drink do you want? {menu.get_items()} ").lower()

    if drink == "report":
        coffee_machine.report()
        money_machine.report()
    elif drink == "off":
        end_state = True
    else:
        drink_choice = menu.find_drink(drink)
        if coffee_machine.is_resource_sufficient(drink_choice):
            money_machine.make_payment(drink_choice.cost)
            coffee_machine.make_coffee(drink_choice)