class User:
    id = 0
    def __init__(self,id,last_name):
        self.id = id
        self.last_name = last_name
        self.followers = 0
        self.following = 0
    def follow(self,user):
        self.followers += 1
        self.following += 1
user1 = User(5)