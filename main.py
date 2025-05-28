def print_report(resource_dict):
    print(f"Water: {resource_dict["water"]}ml")
    print(f"Milk: {resource_dict["milk"]}ml")
    print(f"Coffee: {resource_dict["coffee"]}g")
    print(f"Money: ${resource_dict["money"]}")

def check_resources_sufficient(resource_dict, choice, menu_dict):
    is_sufficient = True
    for ingredient in menu_dict[choice]["ingredients"]:
        if resource_dict[ingredient] <= menu_dict[choice]["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            is_sufficient = False
    return is_sufficient

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
    
    if user_choice not in ["report", "off"]:
        is_sufficient = check_resources_sufficient(resources, user_choice, MENU)

        if is_sufficient == False:
            break
        else:
            print("The resources are sufficient")
