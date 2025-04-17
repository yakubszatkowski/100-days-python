# # ********Day 54 Start**********
# # Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
#
# def subtract(n1, n2):
#     return n1 - n2
#
#
# def multiply(n1, n2):
#     return n1 * n2
#
#
# def divide(n1, n2):
#     return n1 / n2


# # Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.

# def calculate(calc_function, n1, n2):
#     return calc_function(n1, n2)
#
#
# result = calculate(add, 2, 3)
# print(result)


# # Nested function

# def outer_function():
#     print('I\'m outer')
#
#     def nested_function():
#         print('I\'m inner')
#
#     return nested_function
#
#
# inner_function = outer_function()
# print('')
# inner_function()


# # Python decorators function
import time


def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)  # do something before
        function()
        say_bye()  # or after

    return wrapper_function


@delay_decorator
def say_hello():
    # time.sleep(2)
    print('Hello')


def say_bye():
    print('Bye')


def say_greeting():
    print('How are you?')


# or
decorated_function = delay_decorator(say_greeting)
decorated_function()
