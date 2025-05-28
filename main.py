def print_report(resource_dict):
    print(f"Water: {resource_dict["water"]}ml")
    print(f"Milk: {resource_dict["milk"]}ml")
    print(f"Coffee: {resource_dict["coffee"]}g")
    print(f"Money: ${resource_dict["money"]}")

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
