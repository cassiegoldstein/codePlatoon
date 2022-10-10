# your User class goes here

class User:
    def __init__(self, name, email_address, dl_num):
        self.name = name
        self.email_address = email_address
        self.dl_num = dl_num

    def __str__(self):
        return 'name: ' + self.name + '\nemail: ' + self.email_address + "\ndriver's license: " + self.dl_num



user1 = User('Cassie', 'cassieg@gmail.com', '12345')
user2 = User('Dave', 'penguin@gmail.com', '23456')
user3 = User('Bob', 'bob@bob.com', '5647746')

users = [user1, user2, user3]

i = 1
for user in users:
    print("user " + str(i)+":")
    print(user)
    i = i + 1