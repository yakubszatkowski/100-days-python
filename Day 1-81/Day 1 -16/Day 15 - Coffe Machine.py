from Coffe_Machine_data import menu, ingredients_left


def report():
    """prints the amount of ingredients_left in the coffee machine"""
    print(f'Water: {ingredients_left["water"]}mL\nMilk: {ingredients_left["milk"]}mL\n'
          f'Coffee: {ingredients_left["coffee"]}g\nMoney: ${cash_in_machine} ')


def total_amount():
    """Calculates amount of money being put into money machine."""
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))
    return (quarters * 25 + dimes * 10 + nickels * 5 + pennies) / 100


def change():
    """Returns change to the user"""
    cash_put = total_amount()
    if cash_put >= coffee_price:
        final_change = cash_put - coffee_price
        print(f'Here is ${final_change} change')
        return True
    else:
        print('Sorry not enough money, money refunded.')
        return False


def is_enough_ingredients():
    """Checks if there is enough ingredients_left in the machine to make chosen coffee"""
    enough_ingredient = True
    for ingredient in ingredients_left:
        if ingredient in chosen_coffee_ingredients:
            if chosen_coffee_ingredients[ingredient] > ingredients_left[ingredient]:
                print(f'There is not enough {ingredient}.')
                enough_ingredient = False
    return enough_ingredient


def ingredients_calc():
    for ingredient in ingredients_left:
        if ingredient in chosen_coffee_ingredients:
            ingredients_left[ingredient] -= chosen_coffee_ingredients[ingredient]
    print(f'Here is your {user_choice}. Enjoy!')


cash_in_machine = 0
machine = True
while machine:
    user_choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        machine = False
    else:
        coffee_price = menu[user_choice]['cost']
        chosen_coffee_ingredients = menu[user_choice]['ingredients']
        if is_enough_ingredients() and change():
            cash_in_machine += coffee_price
            ingredients_calc()

