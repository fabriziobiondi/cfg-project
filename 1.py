"""
Project: CFG Python Project - Search
Description: Recipe search using Edamame API
Created by: Raina Greifer and Yui Yan Wongo
"""

# Importing libraries
# Edamame API - main database of getting recipes
import py_edamam
# Requests - ability to interact with HTTP URL
import requests
# Random - generate a random recipe
import random

# Setting up Edamam API ID and key
app_id = 'c457e479'
app_key = '30acb7fe7dbb730ae70f3b81f1ce1d9f'


# Backbone function - asking user for the criteria of the search
def run():
    # Ask for dietary requirement - to be used as an input for Health labels
    input_diet = int(input('Do you have any other dietary requirements? '
                           '\r\n 1=None , 2=Vegan, 3=Vegetarian, 4=Pescatarian, 5=Wheat-free, 6=Kosher:'))

    # If statements for obtaining the right parts of URL
    if input_diet == 1:
        allergy = ''
    elif input_diet == 2:
        allergy = '&health=vegan'
    elif input_diet == 3:
        allergy = '&health=vegetarian'
    elif input_diet == 4:
        allergy = '&health=pescatarian'
    elif input_diet == 5:
        allergy = '&health=wheat-free'
    elif input_diet == 6:
        allergy = '&health=kosher'

    # In case of an unidentified input, dietary requirement set to 1 - None
    else:
        allergy = ''
        print('Input not recognised. No special dietary requirements have been specified.\n')

    # Asking user for the basis of the search - searching by ingredient or by calories
    input_choice = input('Do you want to choose by ingredient (enter: I) or by calories (enter: C)? ').lower()

    # If searching by ingredient
    if input_choice == 'i':

        # Ask user for choice of ingredient
        ingredient = input('Please enter an ingredient: ')

        # Check if user want a random recipe
        input_random = input(
            "\nDo you want generate a random recipe (enter: R) "
            "or do you want to check our catalogue (enter: C)? ").lower()

        # Call the random recipe function that decides if the user wants all the recipes or a random recipe
        random_ask(ingredient, input_random, allergy)

    # If searching by calories
    elif input_choice == 'c':

        # Ask user to specify the calories for the meal
        calories = int(input("What is the maximum calories you can have for the meal? "))
        calories_search(calories, allergy)

    # In case of an unexpected input - will recall the main function again
    else:
        print(error_msg)
        run()


#  Check if user want a random recipe
def random_ask(ingredient, input_random, allergy):
    # If the user choose to have a random recipe, call the random search function
    if input_random == "r":
        random_recipe_search(ingredient, allergy)

    # Otherwise, will show a catalogue of 10 recipes (set by the API URL by default)
    elif input_random == "c":
        recipe_search(ingredient, allergy)

    # In case of unexpected input, will ask the user again to confirm their preference.
    else:
        print(error_msg)
        random_ask(ingredient, allergy)


# Obtaining data from the API for the recipe search
def get_data(ingredient, allergy):
    # Setting up the URL at the backend - Able to insert user's inputs back for the search
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}{}'.
            format(ingredient, app_id, app_key, allergy))

    # Transform results to JavaScript Object Notation format - more readable and easier to process
    data = result.json()

    # Hits extracted from the Edamam API - extracting matching objects
    return data["hits"]


# Presenting results for recipe search
def recipe_search(ingredient, allergy):
    # Substitute the user inputs back to the recipe_serach function
    results = get_data(ingredient, allergy)

    # formatting for printing in console
    print(dbl_lines)

    # Getting recipes that match the user's search criteria
    for result in results:

        # Extracting the selected information from the data of JSON (dictionary):
        # Looking for matching recipes - through the URL that we have previously set up
        recipe = result['recipe']
        # Recipe title in recipe
        print(recipe['label'])
        # Valid URL link to recipe
        print(recipe['shareAs'], '\n')
        # Listing out the ingredients in a more readable format
        print("\nIngredients:", '\n', dashes)
        for ingredient in recipe["ingredientLines"]:
            print(f"-{ingredient}")
        print(dbl_lines)

        # Ask if the user would like to save the recipes
    save_file = input('Do you want to save the recipe(s) to a file? (Y/N) ').lower()
    if save_file == 'y':
        # If so, open up a text file and write in it - call it recipe.txt
        with open("recipe.txt", "w+") as Recipes:

            # Writing in the recipe name, ingredients required and URL
            Recipes.write("\n")
            Recipes.write(f"{recipe['label']}\n\n")
            Recipes.write(dbl_lines)
            for ingredient in recipe["ingredientLines"]:
                Recipes.write(f"-{ingredient}\n")
            Recipes.write(dbl_lines)
            Recipes.write(f"Link:{recipe['shareAs']}\n\n")

            # Close the text file when complete
            Recipes.close()
        # Let the user know it is done and exit the function
        print(yes_save)
        exit()
    else:
        # Confirm their preference and exit the function.
        print(no_save)
        exit()


# Function for generating a single random recipe
def random_recipe_search(ingredient, allergy):
    # Substitute inputs back to the URL
    all_recipes = get_data(ingredient, allergy)

    # Generate a random number
    random_number = random.randint(0, len(all_recipes) - 1)

    # Select the random recipe
    random_recipe = all_recipes[random_number]
    recipe = random_recipe["recipe"]

    # Printing out results in console
    print('\n')
    print(recipe["label"])
    print("Ingredients:")
    for ingredient in recipe["ingredientLines"]:
        print(f"-{ingredient}")

        # Ask if user would like to save the recipe
    save_file = input('Do you want to save the recipe to a file? (Y/N) ').lower()
    if save_file == 'y':
        with open("recipe.txt", "w+") as Random_recipe:
            Random_recipe.write("\n")
            Random_recipe.write(f"{recipe['label']}\n\n")
            Random_recipe.write(dbl_lines)
            for ingredient in recipe["ingredientLines"]:
                Random_recipe.write(f"-{ingredient}\n")
            Random_recipe.write(dbl_lines)
            Random_recipe.write(f"Link:{recipe['shareAs']}\n\n")
            Random_recipe.close()
        print(yes_save)
        exit()
    else:
        print(no_save)
        exit()


# Obtaining data from the API for the recipe search - specially for the inclusion of calories
def get_calorie_data(calories, allergy):
    # Setting up the URL at the backend - Able to append calories input by user for the search
    result = requests.get(
        'https://api.edamam.com/search?q=calories={}{}&app_id={}&app_key={}&to=10'.format(
            calories, allergy, app_id, app_key))

    # Transform results to JavaScript Object Notation format
    data = result.json()

    # Hits extracted from the Edamam API - extracting matching objects
    return data["hits"]


# Presenting relevant recipes that meets the calories submitted by the user
def calories_search(calories, allergy):
    results_meal = get_calorie_data(calories, allergy)

    # Printing out results in the console
    for result in results_meal:
        recipe = result['recipe']
        # Recipe title in recipe
        print(recipe['label'])
        # Valid URL link to recipe
        print(recipe['shareAs'], '\n')
        # Listing out the ingredients in a more readable format
        print("\nIngredients:", '\n', dashes)
        for ingredient in recipe["ingredientLines"]:
            print(f"-{ingredient}")
        print(dbl_lines)

    # saves the recipes in a file
    save_file = input('Do you want to save the recipe(s) to a file? (Y/N) ').lower()
    if save_file == 'y':
        with open("recipe.txt", "w+") as calories_recipe:
            calories_recipe.write("\n")
            calories_recipe.write(f"{recipe['label']}\n\n")
            calories_recipe.write(dbl_lines)
            for ingredient in recipe["ingredientLines"]:
                calories_recipe.write(f"-{ingredient}\n")
            calories_recipe.write(dbl_lines)
            calories_recipe.write(f"{recipe['shareAs']}\n\n")
            calories_recipe.close()
        print(yes_save)
        exit()
    else:
        print(no_save)
        exit()


# Texts used for printing
welcome_msg = 'Hi there! Before we start searching:  '
error_msg = 'Sorry, input not recognised. Please try again.'
yes_save = '\nSaved successfully. Enjoy your meal!'
no_save = '\nNo problem. Enjoy your meal!'
dbl_lines = "\n=============================\n"
dashes = "------------------------------"

# Executing the programme
print(welcome_msg)
run()
