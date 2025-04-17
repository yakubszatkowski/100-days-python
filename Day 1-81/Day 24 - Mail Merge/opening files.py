# not related to project

# # reading the file:
# file = open('my_file.txt')
# contents = file.read()
# print(contents)
# file.close()

# # more optimal:
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# # writing in file 'a' for append and 'w' to overwrite
# with open('my_file.txt', mode='a') as file:
#     file.write('\nNew text.')
#
# creating file
with open('my_file2.txt', mode='w') as file:
    file.write('\nNew text.')

# # opening file from directory
# with open('C:/Users/kubas/Desktop/my_file2.txt') as file:
#     print(file.read())

# # opening file with relative path
# with open('../Day 1 - Band name generator.py') as file:
#     print(file.read())
