# lib/models/recipe.py
from models.__init__ import CURSOR, CONN
from models.category import Category

class Recipe:

    def __init__(self, category, name):
        self.category = category
        self.name = name

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        if isinstance(category, Category):
            self._category = category
        else:
            print('Recipe category must be an instance of the Category class')

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name) in range(1, 50, 1):
            self._name = name
        else:
            print('Recipe name must be a string between 1-50 characters in length')

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """DROP TABLE IF EXISTS recipes"""
        CURSOR.execute(sql)
        CONN.commit()