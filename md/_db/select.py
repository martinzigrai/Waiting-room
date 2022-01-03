from md.cl.user import *
from md.cl.view import *
from md._db.connection import Connection

class Select:
    @staticmethod
    def users():
        users = List_of_users()
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        my_cursor.execute("SELECT * from person")

        my_result = my_cursor.fetchall()

        for i in my_result:
            user = User(i[0], i[1], i[2], i[3], i[4])
            users.addUser(user)

        conn.close_connection()
        return users

    @staticmethod
    def record_by_id(person_id):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        query = 'SELECT * from person WHERE person_id=%s'
        val = (person_id,)

        my_cursor.execute(query, val)

        myresult = my_cursor.fetchall()

        for i in myresult:
            user = User(i[0], i[1], i[2], i[3], i[4])

        conn.close_connection()
        return user

    @staticmethod
    def views():
        views = List_of_views()
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        my_cursor.execute("SELECT * from person_contact")

        my_result = my_cursor.fetchall()

        for i in my_result:
            view = View(i[0], i[1], i[2], i[3], i[4], i[5])
            views.addView(view)

        conn.close_connection()
        return views

    @staticmethod
    def viewsSortBy(sort_by: str):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        if sort_by == "name":
            query = 'SELECT * FROM person_contact ORDER BY name;'
        elif sort_by == "surname":
            query = 'SELECT * FROM person_contact ORDER BY surname;'
        else:
            query = 'SELECT * FROM person_contact;'
        my_cursor.execute(query)
        rows = my_cursor.fetchall()
        list_of_views = List_of_views()
        for i in rows:
            view =  View(i[0], i[1], i[2], i[3], i[4], i[5])
            list_of_views.addView(view)

        conn.close_connection()
        return list_of_views

    @staticmethod
    def inj():
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()
        my_cursor.execute('SELECT injection FROM injection')
        rows = my_cursor.fetchall()
        injections = list()
        for row in rows:
            injection = {"injection": row[0]}
            injections.append(injection)
        conn.close_connection()
        return injections

