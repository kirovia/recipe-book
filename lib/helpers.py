# lib/helpers.py
from models.category import Category
from models.recipe import Recipe

def is_integer(input):
    try:
        return int(input)
    except:
        return False

def view_all_categories():
    print('\nCHAPTERS:\n')
    categories = Category.get_all()
    print("*~*~*~*~*~*~*~*~*~*\n")
    for i, category in enumerate(categories, start=1):
        print(f'{i} - {category.name}\n')
    print("*~*~*~*~*~*~*~*~*~*\n")
    print('Type A to add new chapter')
    print('Type D to delete a chapter')
    print('Type E to exit the cookbook')
    print('Type chapter number to open that chapter')
    user_input = input('\nType your selection: \n')
    if user_input.upper() == 'A':
        create_category()
    elif user_input.upper() == 'D':
        delete_category()
    elif user_input.upper() == 'E':
        exit_program()
    elif is_integer(user_input) and is_integer(user_input) in range(len(categories) + 1):
        view_all_recipes(int(user_input) - 1)
    else:
        print('\nInput not recognized, please try again\n')
        view_all_categories()


def create_category():
    name = input('Please enter the name of the new chapter: ')
    try:
        Category.create(name)
        print(f'\n\nSuccessfully created new chapter: {name}!\n\n')
    except Exception as exc:
        print(f'\n\n{exc}\n\n')
    view_all_categories()

def delete_category():
    categories = Category.get_all()
    user_input = input('Please enter the chapter number to delete: ')
    if int(user_input) in range(len(categories) + 1):
        category = Category.find_by_name(categories[int(user_input) - 1].name)
        recipes = category.recipes()
        for recipe in recipes:
            recipe.delete()
        category.delete()
        print(f'\n\n{category.name} category and its recipes successfully deleted\n\n')
        view_all_categories()
    else:
        print('\nInput not recognized, please try again\n')
        view_all_categories()

def view_all_recipes(category_id):
    categories = Category.get_all()
    category = categories[category_id]
    print(f'\n{category.name.upper()} RECIPES:')
    print("\n*~*~*~*~*~*~*~*~*~*\n")
    for i, recipe in enumerate(category.recipes(), start=1):
        print(f'{i} - {recipe.name}\n')
    print("*~*~*~*~*~*~*~*~*~*\n")
    select_recipe(category_id)
        

def select_recipe(category_id):
    categories = Category.get_all()
    category = categories[category_id]
    recipes = category.recipes()
    print('Type A to add a new recipe')
    print('Type D to delete a recipe')
    print('Type B to go back to chapters')
    print('Type recipe number to view that recipe')
    user_input = input('\nType your selection: ')
    if user_input.upper() == 'A':
        create_recipe(category_id)
    elif user_input.upper() == 'D':
        delete_recipe(category_id)
    elif user_input.upper() == 'B':
        view_all_categories()
    elif is_integer(user_input) and is_integer(user_input) in range(len(recipes) + 1):
        recipe_description(category_id, user_input)
        view_all_recipes(category_id)
    else:
        print('\nInput not recognized, please try again\n')
        view_all_recipes(category_id)


def create_recipe(category_id):
    name = input('Please enter the name of the recipe: ')
    description = input('Please enter a brief description of the dish: ')
    try:
        recipe = Recipe.create(name, description, int(category_id + 1))
        print(f'\n\nSuccessfully added {recipe.name} to the {Category.find_by_id(category_id + 1).name} chapter!\n\n')
    except Exception as exc:
        print(f'\n\n{exc}\n\n')
    view_all_recipes(category_id)


def delete_recipe(category_id):
    category = Category.find_by_id(category_id + 1)
    recipes = category.recipes()
    user_input = input('Type the recipe number to be deleted: ')
    if int(user_input) in range(len(recipes) + 1):
        recipes[int(user_input) - 1].delete()
        print(f'{recipes[int(user_input) - 1].name} successfully deleted!')
        view_all_recipes(category_id)
    else:
        print('\nInput not recognized, please try again\n')
        view_all_recipes(category_id)


def recipe_description(category_id, user_input):
    categories = Category.get_all()
    category = categories[category_id]
    recipes = category.recipes()
    recipe = recipes[int(user_input) - 1]
    print(f'\n{recipe.description}\n')
    view_all_recipes(category_id)

def exit_program():
    print("Goodbye!")
    exit()
