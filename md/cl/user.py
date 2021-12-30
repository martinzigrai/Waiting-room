class User:
    def __init__(self, user_id, name, email, username, password):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.username = username
        self.password = password

    def getUserInfo(self):
        user = {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "username": self.username,
            "password": self.password
        }
        return user

class List_of_users:
    def __init__(self):
        self.main_list = list()

    def addUser(self, user):
        self.main_list.append(user)

    def getUserNames(self):
        user_names = list()
        for i in range(len(self.main_list)):
            user_names.append(self.main_list[i].username)

        return user_names

    def getUser(self, username):
        for i in range(len(self.main_list)):
            if username == self.main_list[i].username:
                myuser = self.main_list[i]
                break
        return myuser

    def getUsersInfo(self):
        users = list()
        for i in range(len(self.main_list)):
            user = {
                "user_id": self.main_list[i].user_id,
                "name": self.main_list[i].name,
                "email": self.main_list[i].email,
                "username": self.main_list[i].username,
                "password": self.main_list[i].password
            }
            users.append(user)

        return users
