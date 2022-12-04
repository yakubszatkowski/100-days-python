# # FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()
# # KeyError
# a_dictionary = {'some key':'some value'}
# value = a_dictionary['non-existent key']
# # IndexError
# fruit_list = ['apple', 'banana', 'pear']
# fruit = fruit_list[3]
# # TypeError
# text = 'abc'
# print(text + 5)

# # # Catching exceptions
#
# try:  # something that might cause an exception
#     file = open("a_file.txt")
#     a_dictionary = {'some key': 'some value'}
#     print(a_dictionary['some key'])
# except FileNotFoundError:  # do this if there was an exception (in case FileNotFoundError)
#     file = open("a_file.txt", 'w')
#     file.write('something')
# except KeyError as error_message:
#     print(f'the key {error_message} doesn\'t exist')
# else:  # do this if there were no exceptions
#     content = file.read()
#     print(content)
# finally:  # do this no matter what happens
#     # file.close()
#     # print('File was closed')
#     raise TypeError("This is a error I\'ve made up")  # raise our own exceptions

# # another raise stuff:
# height = float(input('Height: '))
# weight = float(input('Weight: '))
#
# if height >= 3:
#     raise ValueError('No one is over three meters')
#
# bmi = weight/height ** 2
# print(bmi)

# # exercise 1
# fruits = ["Apple", "Pear", "Orange"]
#
#
# # TODO: Catch the exception and make sure the code runs without crashing.
# def make_pie(index):
#     try:
#         fruit = fruits[index]
#     except IndexError:
#         print('Fruit pie')
#     else:
#         print(fruit + " pie")
#
#
# make_pie(4)

# # exercise 2
# facebook_posts = [
#     {'Likes': 21, 'Comments': 2},
#     {'Likes': 13, 'Comments': 2, 'Shares': 1},
#     {'Likes': 33, 'Comments': 8, 'Shares': 3},
#     {'Comments': 4, 'Shares': 2},
#     {'Comments': 1, 'Shares': 1},
#     {'Likes': 19, 'Comments': 3}
# ]
#
# total_likes = 0
#
# for post in facebook_posts:
#     try:
#         total_likes += post['Likes']
#     except KeyError:
#         post['Likes'] = 0  # or just >pass, or total_likes += 0
#
# print(total_likes)
