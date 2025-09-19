# lib/models/recipe.py
from models.__init__ import CURSOR, CONN
from models.category import Category

class Recipe:

    all = {}

    def __init__(self, name, description, category_id, id = None):
        self.id = id
        self.name = name
        self.description = description
        self.category_id = category_id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) is str and len(name) in range(1, 50, 1):
            self._name = name
        else:
            print('Recipe name must be a string between 1-50 characters in length')

    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if type(description) is str and len(description):
            self._description = description
        else:
            raise ValueError('Recipe description cannot be empty!')

    @property
    def category_id(self):
        return self._category_id
    
    @category_id.setter
    def category_id(self, category_id):
        if type(category_id) is int and Category.find_by_id(category_id):
            self._category_id = category_id
        else:
            print('Recipe category must be an instance of the Category class')

    @classmethod
    def create_table(cls):
        sql = """CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
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

    def save(self):
        sql = """INSERT INTO recipes (name, description, category_id) VALUES (?, ?, ?)"""
        CURSOR.execute(sql, (self.name, self.description, self.category_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description, category_id):
        recipe = cls(name, description, category_id)
        recipe.save()
        return recipe
    
    def delete(self):
        sql = """DELETE FROM recipes WHERE id = ?"""
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]

    @classmethod
    def get_all(cls):
        sql = """SELECT * FROM recipes"""
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """SELECT * FROM recipes WHERE id = ?"""
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """SELECT * FROM recipes WHERE name = ?"""
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def instance_from_db(cls, row):
        recipe = cls.all.get(row[0])
        if recipe:
            recipe.name = row[1]
            recipe.description = row[2]
            recipe.category_id = row[3]
        else:
            recipe = cls(row[1], row[2], row[3])
            recipe.id = row[0]
            cls.all[recipe.id] = recipe
        return recipe