# lib/cli.py

from helpers import (
    exit_program,
    view_all_categories,
    get_category,
    create_category,
    delete_category,
    get_category_recipes,
    view_all_recipes,
    get_recipe,
    create_recipe,
    delete_recipe,
    view_recipe_category
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            view_all_categories()
        elif choice == "2":
            get_category()
        elif choice == "3":
            create_category()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            get_category_recipes()
        elif choice == "6":
            view_all_recipes()
        elif choice == "7":
            get_recipe()
        elif choice == "8":
            create_recipe()
        elif choice == "9":
            delete_recipe()
        elif choice == "10":
            view_recipe_category()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("*~*~*~*~*~*~*~*~*~*")
    print("0. Exit the program")
    print("1. View all categories")
    print("2. Find category by id or name")
    print("3. Create new category")
    print("4. Delete category")
    print("5. View all recipes from single category")
    print("6. View all recipes")
    print("7. Find recipe by id or name")
    print("8. Add new recipe")
    print("9. Delete recipe")
    print("10. View a recipe's category")
    print("*~*~*~*~*~*~*~*~*~*")


if __name__ == "__main__":
    main()