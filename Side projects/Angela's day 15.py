from Coffe_Machine_data import menu, ingredients_left


def report():
    print(f'Water: {ingredients_left["water"]}ml')
    print(f'Milk: {ingredients_left["milk"]}ml')
    print(f'Coffee: {ingredients_left["coffee"]}g')
    print(f'Money: ${money_in_machine}')


def is_resource_sufficient(drink_ingredients):
    is_enough_ingredient = True
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] > ingredients_left[ingredient]:
            is_enough_ingredient = False
            if not is_enough_ingredient:
                print(f'There is not enough {ingredient}')
    return is_enough_ingredient

def money_processing():
    total = int(input('How many quarters?: ')) * 0.25
    total += int(input('How many dimes?: ')) * 0.10
    total += int(input('How many nickles?: ')) * 0.05
    total += int(input('How many pennies?: ')) * 0.01
    return round(total, 2)

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print('Sorry that\'s not enough money')
        return False
    else:
        global money_in_machine
        money_in_machine += drink_cost
        change = round(money_received - drink_cost, 2)
        print(f'Your change is: {change}')
        return True


def making_coffee(drink_name, drink_ingredients):
    for ingredient in drink_ingredients:
        ingredients_left[ingredient] -= drink_ingredients[ingredient]
    print(f'Here is your {drink_name}. Enjoy!')


money_in_machine = 0
machine_is_on = True
while machine_is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ')
    if choice == 'off':
        machine_is_on = False
    elif choice == 'report':
        report()
    else:
        drink = menu[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = money_processing()
            if is_transaction_successful(payment, drink['cost']):
                making_coffee(choice, drink['ingredients'])


