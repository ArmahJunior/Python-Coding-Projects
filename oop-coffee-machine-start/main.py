from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from prettytable import PrettyTable
table = PrettyTable()
coffee = CoffeeMaker()
money = MoneyMachine()
drink_menu = Menu()
is_on = True
while is_on:
    userInput = input(f"How will you like? {drink_menu.get_items()}:")
    if userInput == "nothing":
        is_on = False
    elif userInput == "report":
        coffee.report()
        money.report()
    elif drink_menu.find_drink(userInput) and coffee.is_resource_sufficient(drink_menu.find_drink(userInput)):
        drink = drink_menu.find_drink(userInput)
        if money.make_payment(drink.cost):
            coffee.make_coffee(drink)
print("Thanks!")
