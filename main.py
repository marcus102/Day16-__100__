from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_report = CoffeeMaker()
profit = MoneyMachine()
my_menu = Menu()

coffe_machine_is_on = True
while coffe_machine_is_on:
    option = my_menu.get_items()
    customer_choice = input(f"What would you like? {option}: ").lower()
    if customer_choice == 'off':
        coffe_machine_is_on = False
    elif customer_choice == 'report':
        final_report = my_report.report()
        final_profit = profit.report()
    elif customer_choice == 'espresso' or customer_choice == 'latte' or customer_choice == 'cappuccino':
        my_drink = my_menu.find_drink(customer_choice)
        if my_report.is_resource_sufficient(drink= my_drink):
            if profit.make_payment(cost= my_drink.cost):
                my_report.make_coffee(order= my_drink)
        
    else:
        print("Not such flavor!\nHere our available flavors:\n epresso\n latte\n cappuccino")