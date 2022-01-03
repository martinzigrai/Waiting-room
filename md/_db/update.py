from md.cl.user import *
from md._db.connection import Connection

class Update:

    @staticmethod
    def record_update(new_user: User, id):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        query = 'UPDATE person SET name=%s, surname=%s, username=%s WHERE person_id=%s;'
        val = (new_user.name, new_user.surname, new_user.username, id,)
        my_cursor.execute(query, val)

        connection.commit()
        conn.close_connection()
        return True