class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user_1 = User(1, 'Angela')
user_2 = User(2, 'Jack')

# print(user_1.id); print(user_1.username)
# print(user_2.id); print(user_2.username)

user_2.follow(user_1)

print(user_1.followers)  #
print(user_1.following)  #
print(user_2.followers)  #
print(user_2.following)  #
