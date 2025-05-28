def print_report(resource_dict):
    print(f"Water: {resource_dict['water']}ml")
    print(f"Milk: {resource_dict['milk']}ml")
    print(f"Coffee: {resource_dict['coffee']}g")
    print(f"Money: ${resource_dict['money']}")

def check_resources_sufficient(resource_dict, choice, menu_dict):
    is_sufficient = True
    for ingredient in menu_dict[choice]["ingredients"]:
        if resource_dict[ingredient] < menu_dict[choice]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            is_sufficient = False
    return is_sufficient

def process_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    user_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return user_money

def check_transaction_successful(choice, money, menu_dict, resources_dict):
    if menu_dict[choice]["cost"] > money:
        print("Sorry that's not enough money.\nMoney refunded.")
    else:
        if money > menu_dict[choice]["cost"]:
            change = money - menu_dict[choice]["cost"]
            print(f"Please take your change: ${round(change, 2)}")
        resources_dict["money"] += menu_dict[choice]["cost"]
        return True

def deduct_ingredients(choice, resources_dict, menu_dict):
    for ingredient in menu_dict[choice]["ingredients"]:
        resources_dict[ingredient] -= menu_dict[choice]["ingredients"][ingredient]

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
    "money": 0,
}

user_choice = ""

while user_choice != "off":
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if user_choice == "report":
        print_report(resources)
    
    if user_choice in MENU:
        is_sufficient = check_resources_sufficient(resources, user_choice, MENU)

        if is_sufficient == False:
            continue
        else:
            user_money = process_coins()
            is_transaction_successful = check_transaction_successful(user_choice, user_money, MENU, resources)

            if is_transaction_successful:
                deduct_ingredients(user_choice, resources, MENU)

                print(f"Here is your {user_choice}. Enjoy!")
