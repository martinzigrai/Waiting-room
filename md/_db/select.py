from md.cl.user import *
from md._db.connection import Connection

class Select:
    @staticmethod
    def users():
        users = List_of_users()
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        my_cursor.execute("SELECT * from public.user")

        my_result = my_cursor.fetchall()

        for i in my_result:
            user = User(i[0], i[1], i[2], i[3], i[4])
            users.addUser(user)

        conn.close_connection()
        return users