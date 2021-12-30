from md._db.connection import Connection

class Insert:

    @staticmethod
    def user(name, email, username, password):

        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()
        query = 'INSERT INTO public.user (name, email, username, password) values (%s, %s, %s, %s);'
        val = (name, email, username, password)
        my_cursor.execute(query, val)
        connection.commit()
        conn.close_connection()
        return True
