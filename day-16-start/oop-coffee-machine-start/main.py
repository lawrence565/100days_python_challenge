from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True
menus = []
for i in menu.menu:
    menus.append(i.name)

while is_on:
    command = ""
    while command not in menus:
        command = input(f"What's would you like to drink? ({menu.get_items()}): ")
        if command == "off":
            print("Thanks for using.")
            is_on = False
        elif command == "report":
            coffee_machine.report()
            money_machine.report()
    item = menu.find_drink(command)
    if coffee_machine.is_resource_sufficient(item):
        if money_machine.make_payment(item.cost):
            coffee_machine.make_coffee(item)