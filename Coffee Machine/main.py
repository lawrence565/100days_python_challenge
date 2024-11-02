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
    while chosen not in ["espresso", "latte", "cappuccino"]:
        chosen = input("WHat would you like? (Espresso/Latte/Cappuccino): ").lower()
        if chosen == "report":
            print("Water:", resources["water"])
            print("Milk:", resources["milk"])
            print("Coffee:", resources["coffee"])
            print("Money: $" + str(money))
    return chosen

def check_sufficient(water, milk, coffee):
    if water < resources["water"] and coffee < resources["coffee"] and milk < resources["milk"]:
        return True
    else:
        if water > resources["water"]:
            print("Sorry that's not enough water.")
        if coffee > resources["coffee"]:
            print("Sorry that's not enough coffee.")
        if milk > resources["milk"]:
            print("Sorry that's not enough milk.")
        return False

def get_coin():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))

    coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return coins

def main():
    running = True
    global money
    while running:
        chosen_coffee = choose_coffee()

        water = MENU[chosen_coffee]["ingredients"]["water"]
        milk = 0
        try:
            milk = MENU[chosen_coffee]["ingredients"]["milk"]
        except KeyError:
            pass
        coffee = MENU[chosen_coffee]["ingredients"]["coffee"]
        price = MENU[chosen_coffee]["cost"]

        if check_sufficient(water, milk, coffee):
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