from Calculator_art import logo

def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    return n1 / n2

operations = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
}

def calculation_recursion():
    print(logo)
    num1 = float(input('What is the first number? '))
    for symbol in operations:
        print(symbol)
    calc=True
    while calc:
        op = input('Which operation would you like to do? ')
        num2 = float(input('What is the second number? '))
        answer = operations[op](num1, num2)                     # operations[op] - picks value of operations(mathematical
        # operation) based on op(symbol) and then attaches (num1, num2) which creates functions calculating the answer
        print(f'{num1} {op} {num2} = {answer}')
        keepgoing=input(f'Do you want to keep on calculating using {answer}? Y/N ').lower()
        if keepgoing == 'n':
            calculation_recursion()
        elif keepgoing == 'y':
            num1 = answer

calculation_recursion()