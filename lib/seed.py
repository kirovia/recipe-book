#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.category import Category
from models.recipe import Recipe

def seed_database():
    Category.drop_table()
    Recipe.drop_table()
    Category.create_table()
    Recipe.create_table()

    # Create seed data
    desserts = Category.create("Desserts")
    breakfast = Category.create("Breakfast")
    Recipe.create("Apple Pie", desserts.id)
    Recipe.create("Chocolate Cake", desserts.id)
    Recipe.create("Quiche", breakfast.id)
    Recipe.create("Biscuits and Gravy", breakfast.id)
    Recipe.create("Fried Eggs and Bacon", breakfast.id)


seed_database()
print("Seeded database")
