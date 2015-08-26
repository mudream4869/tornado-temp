import hashlib, binascii

class User:
    def __init__(self):
        self.name = ""
        self.is_null = False
        self.id = -1
        self.introduction = ""
        self.address = ""

class UserHandler:
    def __init__(self):
        UserHandler.inst = self

    def getUserByUserId(self, user_id):
        return null_user 

null_user = User()
null_user.name = "null"
null_user.is_null = True
null_user.id = 0
