# lib/cli.py

from helpers import (
    exit_program,
    view_all_categories,
    # get_category_by_name,
    # create_category,
    # delete_category,
    # view_all_recipes,
    # get_recipe_description,
    # create_recipe,
    # delete_recipe,
    # view_recipe_category
)

def menu():
    print("\nWELCOME TO YOUR COOKBOOK!\n")
    view_all_categories()

if __name__ == "__main__":
    menu()