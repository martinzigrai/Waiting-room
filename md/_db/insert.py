from md._db.connection import Connection
from md.cl.user import *

class Insert:

    @staticmethod
    def user(new_user: User):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        query = 'INSERT INTO public.user (name, email, username, password) values (%s, %s, %s, %s);'

        val = (new_user.name, new_user.email, new_user.username, new_user.password)
        my_cursor.execute(query, val)

        connection.commit()
        conn.close_connection()
        return True
