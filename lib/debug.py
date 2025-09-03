#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
import ipdb
from models.category import Category
from models.recipe import Recipe

Category.drop_table()
Recipe.drop_table()
Category.create_table()
Recipe.create_table()

desserts = Category.create("Desserts")
breakfast = Category.create("Breakfast")
Recipe.create("Apple Pie", desserts.id)
Recipe.create("Chocolate Cake", desserts.id)
Recipe.create("Quiche", breakfast.id)
Recipe.create("Biscuits and Gravy", breakfast.id)
Recipe.create("Fried Eggs and Bacon", breakfast.id)


ipdb.set_trace()
