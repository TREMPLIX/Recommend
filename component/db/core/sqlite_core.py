import sqlite3
import pandas as pd
from component.db.core.base import Base
from component.logs_comp import logging


class SqliteCore(Base):

    def __init__(self, database):
        self.lg = logging()
        self.db = database

    def create_connection(self):
        self.cnx = sqlite3.connect(self.db)
        self.lg.write_logs('Создание коннекта с бд')

    def close_connection(self):
        self.cnx.close()
        self.lg.write_logs('Закрытие коннекта с бд')

    def get_data(self, query):
        self.create_connection()
        cursor = self.cnx.cursor()
        result = cursor.execute(query)
        data = result.fetchall()
        names = [i[0] for i in cursor.description]
        df = pd.DataFrame(data, columns=names)
        self.close_connection()

        return df

    def update_table(self, query):
        self.create_connection()
        cursor = self.cnx.cursor()
        cursor.execute(query)
        self.cnx.commit()
        self.close_connection()
