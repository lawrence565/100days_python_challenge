from math import expm1

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def choose_coffee():
    chosen = ""
    while chosen not in ["espresso", "latte", "cappuccino", "off"]:
        chosen = input("WHat would you like? (Espresso/Latte/Cappuccino): ").lower()
        if chosen == "report":
            print("Water:", resources["water"])
            print("Milk:", resources["milk"])
            print("Coffee:", resources["coffee"])
            print("Money: $" + str(money))
    return chosen

def check_sufficient(order_ingredient):
    """Receive ingredients of coffe and return if resources are sufficient."""
    for item in order_ingredient:
        if order_ingredient[item] > resources[item]:
            print(f"Sorry that's not enough {item}.")
            return False
    return True

def get_coin():
    """Receive coins and return the value of them"""
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return coins

def main():
    global money
    running = True
    while running:
        chosen_coffee = choose_coffee()
        if chosen_coffee == 'off':
            running = False
            print("Thanks for using.")
            continue

        water = MENU[chosen_coffee]["ingredients"]["water"]
        milk = 0
        try:
            milk = MENU[chosen_coffee]["ingredients"]["milk"]
        except KeyError:
            pass
        coffee = MENU[chosen_coffee]["ingredients"]["coffee"]
        price = MENU[chosen_coffee]["cost"]

        if check_sufficient(MENU[chosen_coffee]["ingredients"]):
            print("Please insert coin.")
        else:
            continue

        coins = get_coin()
        if coins > price:
            change = round(coins - price, 2)
            print(f"Here is {change} in change.")
            print(f"Here is your {chosen_coffee} ☕ Enjoy!")
            resources["water"] -= water
            resources["milk"] -= milk
            resources["coffee"] -= coffee
            money += price
        else:
            print("Sorry that's not enough money. Money refunded.")

main()