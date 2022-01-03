class View:
    def __init__(self, person_id, name, surname, phone_num, mail, birth_id_num):
        self.person_id = person_id
        self.name = name
        self.surname = surname
        self.phone_num = phone_num
        self.mail = mail
        self.birth_id_num = birth_id_num

    def getViewInfo(self):
        view = {
            "person_id": self.person_id,
            "name": self.name,
            "surname": self.surname,
            "phone_num": self.phone_num,
            "mail": self.mail,
            "birth_id_num": self.birth_id_num

        }
        return view

class List_of_views:
    def __init__(self):
        self.main_list = list()

    def addView(self, view):
        self.main_list.append(view)

    def getView(self, username):
        for i in range(len(self.main_list)):
            if username == self.main_list[i].username:
                myview = self.main_list[i]
                break
        return myview

    def getViewsInfo(self):
        views = list()
        for i in range(len(self.main_list)):
            view = {
                "person_id": self.main_list[i].person_id,
                "name": self.main_list[i].name,
                "surname": self.main_list[i].surname,
                "phone_num": self.main_list[i].phone_num,
                "mail": self.main_list[i].mail,
                "birth_id_num": self.main_list[i].birth_id_num
            }
            views.append(view)

        return views

