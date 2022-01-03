class User:
    def __init__(self, person_id, name, surname, username, password):
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.username = username
        self.password = password

    def getUserInfo(self):
        user = {
            "person_id": self.person_id,
            "name": self.name,
            "surname": self.surname,
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
                "person_id": self.main_list[i].person_id,
                "name": self.main_list[i].name,
                "surname": self.main_list[i].surname,
                "username": self.main_list[i].username,
                "password": self.main_list[i].password
            }
            users.append(user)

        return users
