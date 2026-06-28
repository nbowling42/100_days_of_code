from coffee_maker import CoffeeMaker
from menu import Menu
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while True:
    choice = input(f"What would you like? ({menu.get_items()}): ").lower()

    if choice == "off":
        break
    elif choice == "report":
        coffee_machine.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if order:
            if coffee_machine.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                    coffee_machine.make_coffee(order)
