#
# TODO 2:

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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
    "money": 0
}
a = 1
while a > 0:
    use_input = input('“What would you like"? (espresso/latte/cappuccino):')
    rep_key = 0
    if use_input == "report":
        rep_key=1
        for i in resources:
            print(i, ":", resources[i])
    # TODO Turn off the Coffee Machine by entering “off” to the prompt
    if use_input == "off":
        a = -1
    # TODO Check resources sufficient?
    z = "resources are not  sufficient"
    while(rep_key!=1):
        if MENU[use_input]["ingredients"]["water"] < resources["water"]:
            if MENU[use_input]["ingredients"]["milk"] < resources["milk"]:
                if MENU[use_input]["ingredients"]["coffee"] < resources["coffee"]:
                    print("Please insert coins.")
                    # note 100 pennies, 20 nickels, 10 dimes, or 4 quarters; each = 1 dollar
                    quarters = int(input("how many quarters?:"))
                    quarters_d = quarters / 4
                    dimes = int(input("how many dimes?:"))
                    dimes_d = dimes / 10
                    nickels = int(input("how many nickels?:"))
                    nickels_d = nickels / 20
                    pennies = int(input("how many pennies:"))
                    pennies_d = pennies / 100
                    total_money_d = quarters_d + dimes_d + nickels_d + pennies_d
                    if (total_money_d < MENU[use_input]["cost"]):
                        print(" Please inserted enough money to purchase the drink selected.")
                        continue
                    else:
                        change = round(total_money_d - MENU[use_input]["cost"])
                        resources["cost"] = resources["cost"] + MENU[use_input]["cost"]
                    print(f"here is ${change} in change.")
                    print(f"here is your {use_input} ☕ .Enjoy! ")
                    resources["water"] = resources["water"] - MENU[use_input]["ingredients"]["water"]
                    resources["milk"] = resources["milk"] - MENU[use_input]["ingredients"]["milk"]
                    resources["coffee"] = resources["coffee"] - MENU[use_input]["ingredients"]["coffee"]
                    # TODO money

                    rep_key=1
                else:
                    print(z)
                    rep_key = 1
            else:
                print(z)
                rep_key = 1
        else:
            print(z)
            rep_key=1

print("of maintainers of the coffee machine")