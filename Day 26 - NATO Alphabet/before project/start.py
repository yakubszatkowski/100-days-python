import random
import pandas

# numbers = [1, 2, 3]
# new_list = []
# for n in numbers:
#     add_1 = n+1
#     new_list.append(add_1)
# print(new_list)

# # List comprehension
# numbers = [1, 2, 3]
# new_list = [n+1 for n in numbers]
# print(new_list)

# # Works on strings
# name = 'Angela'
# new_list = [letter for letter in name]
# print(new_list)

# # Creating and modifying lists from range
# range_list = [n*2 for n in range(1, 5)]
# print(range_list)

# # Creating list if condition is met
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name)<5]
# print(short_names)

# # Challenge
# up_names = [name.upper() for name in names if len(name)>5]

# # Dictionary comprehension
# # Creating dictionary from list
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
# # Modifying dictionary
# passed_students = {student: score for (student, score) in students_score.items() if score > 45}
# print(passed_students)


# student_dict = {
#     'student': ['Angela', 'James', 'Lily'],
#     'score': [56, 76, 98]
# }
# # looping trough key and values in pho_dict
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

# # similar for looping in dataframe
# student_df = pandas.DataFrame(student_dict)
# basic not so useful loop
# for (key, value) in student_df.items():
#     print(value)

# # better loop
# for (index, row) in student_df.iterrows():
#     print(index)
#     print(row)
#     print(row.student)
#     if row.student == 'Angela':
#         print(row.score)

# # looping trough pandas dataframe
# {new_key:new_value for (index,row) in df.iterrows()}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
nr_letters = random.randint(6, 8)

random_letters = [random.choice(letters) for number in range(0, nr_letters)]
print(random_letters)
