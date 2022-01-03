from md._db.connection import Connection

class Delete:
    @staticmethod
    def record_from_table(id):
        conn = Connection()
        connection = conn.get_connection()
        my_cursor = connection.cursor()

        query = 'DELETE FROM person WHERE person_id = %s;'
        val = (id,)
        my_cursor.execute(query, val)

        connection.commit()
        conn.close_connection()
        return True