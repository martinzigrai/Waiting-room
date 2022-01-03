import psycopg2
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

class Connection:
    def __init__(self):
        self.dbConnection = None

    def get_connection(self):
        self.dbConnection = psycopg2.connect(
            database="final_project", #treba nahradit vlastnymi parametrami
            user="spravca",
            password="root",
            host="localhost",
            port="5432"
        )
        return self.dbConnection

    def close_connection(self):
        self.dbConnection.close()
