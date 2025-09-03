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

ipdb.set_trace()
