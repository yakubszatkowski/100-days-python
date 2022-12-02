# # unlimited argument function
# def add(*args):  # * is a tuple
#     return sum(args)
#
# print(add(3, 5, 6))


# # unlimited keyword arguments function
# def calculate(n, **kwargs):  # ** is a dictionary
#     print(kwargs)
#     for key, value in kwargs.items():
#         print(key, value)
#     print(kwargs['add'])
#     n *= kwargs['multiply']
#     n += kwargs['add']
#     print(n)
#
#
# calculate(2, add=3, multiply=5)

# # kwargs in class and optional categories
# class Car:
#     def __init__(self, **kw):
#         self.make = kw.get('make')  # if this key doesn't receive a value it won't error, returns none
#         self.model = kw['model'] # if this key doesn't receive a value it will error
#
#
# my_car = Car(make='Nissan', model='GTR')
# print(my_car.make, my_car.model)
