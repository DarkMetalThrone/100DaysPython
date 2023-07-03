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

import art
end = False

def display_resource():
    """Displays the Resourses remaining in the Coffee Machine."""
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {resources['money']}")
    
def evaluate(drink):
    """Asks for the coins you inserted and returns the change and adds the funds to coffee machine"""
    print("Please Insert Coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if inserted > MENU[command]["cost"]:
        change = round(inserted - MENU[command]["cost"], 2)
        resources["money"] += MENU[command]["cost"]
        print(f"Here {change} in change.")
        print(f"Here is your {drink}, Enjoy!")
        return True
    else:
        print("Sorry, Insuffecient Funds Inserted.")
        return False

def deduction(drink):
    """Checks if Deduction from the resourses is possible"""
    for i in MENU[drink]["ingredients"]:
        if resources[i] < MENU[drink]["ingredients"][i]:
            return False
    return True
        
def reduce(drink):
    """"Reduces the resourses when a drink is made"""
    for i in MENU[drink]["ingredients"]:
        if i in resources:
            resources[i] -= MENU[drink]["ingredients"][i]

while not end:
    #ask the user input until he exits
    command = input("What would you like? (espresso/ latte/ cappuccino): ")
    if command == "report":
        #display report if asked
        display_resource()
    elif command == "espresso" or command == "latte" or command == "cappuccino":
        #if a drink is selected, check if deuction is possible and usesr has insesrted enough funds
        if deduction(drink = command) and evaluate(drink = command):
            #reduce the resources
            reduce(drink = command)
        elif not deduction(drink = command):
            print(f"Sorry, Insufficient Ingredients.")
    #if the user decides to exit
    elif command == "exit":
        print("The Machine will now stop.")
        end = True
    #Catch all invalid inputs
    else:
        print("Invalid Input! Try Again.")
