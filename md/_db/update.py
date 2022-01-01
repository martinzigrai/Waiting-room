from md.cl.user import *
from md._db.connection import Connection

class Update:

    @staticmethod
    def record_update(new_user: User, id):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        query = 'UPDATE public.user SET name=%s, email=%s, username=%s WHERE user_id=%s;'
        val = (new_user.name, new_user.email, new_user.username, id,)
        my_cursor.execute(query, val)

        connection.commit()
        conn.close_connection()
        return True