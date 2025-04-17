# # My take:
# with open('file1.txt') as file:
#     contents1 = file.readlines()
#     stripped_contents1 = [int(n.strip()) for n in contents1]
# with open('file2.txt') as file_2:
#     contents2 = file_2.readlines()
#     stripped_contents2 = [int(n.strip()) for n in contents2]
#
# result = [num for num in stripped_contents1 if num in stripped_contents2]
#
# print(result)

# # Angela's take (better)
# with open('file1.txt') as file1:
#     file_1_data = file1.readlines()
#
# with open('file2.txt') as file2:
#     file_2_data = file2.readlines()
#
# result = [int(num) for num in file_1_data if num in file_2_data]  # num.strip() could also be there
# print(result)



#I also forgot about readlines()
# .split() would be also fine