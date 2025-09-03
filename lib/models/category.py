# lib/models/category.py
from models.__init__ import CURSOR, CONN

class Category:

    all = {}

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name) in range(1, 25, 1):
            self._name = name
        else:
            print('Category name must be a string between 1-25 characters in length')

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY,
            name TEXT)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS categories"""
        CURSOR.execute(sql)
        CONN.commit()
