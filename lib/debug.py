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

desserts = Category.create("Dessert")
breakfast = Category.create("Breakfast")
seafood = Category.create('Seafood')
Recipe.create("Apple Pie", "Delicious baked treat made from cinnamon and granny smith apples", desserts.id)
Recipe.create("Chocolate Cake", "This baked treat is moist, rich, and bursting with fudgy flavor", desserts.id)
Recipe.create("Quiche", "Easy breakfast casserole made from eggs, bacon, and veggies", breakfast.id)
Recipe.create("Biscuits and Gravy", "Southern staple made from country sausage and homemade biscuits", breakfast.id)
Recipe.create("Fried Eggs and Bacon", "American classic suitable for any day", breakfast.id)
Recipe.create('Coconut Curry Salmon', "Asian-inspired, spicy and sweet seafood dish", seafood.id)
Recipe.create('Gumbo', "Spicy rice dish with sausage and shrimp mix-ins", seafood.id)


ipdb.set_trace()
