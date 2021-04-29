"""
Project: CFG Python Project - Search
Description: Recipe search using Edamame API
Created by: Raina Greifer and Yui Yan Wong
"""

# Importing libraries
## Edamame API
import py_edamam
## Requests - ability to interact with HTTP URL
import requests


# Main function to search for recipes from Edamam API
def recipe_search(ingredient):
    ## Setting up the URL at the backend with app id and key - Able to put 'ingredients' (input from user) back to this for searches
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id=c457e479&app_key=30acb7fe7dbb730ae70f3b81f1ce1d9f'.format(ingredient)
    )

    ## Transform results to JavaScript Object Notation format - more readable and easier to process
    data = result.json()

    ## Hits extracted from the Edamam API - extracting matching objects
    return data['hits']


# The key function that to be run
def run():
    ## Asking user for input for ingredients that would like to cook with
    ingredient = input('Enter an ingredient: ')

    ## Substitute the user input back to the recipe_serach function
    results = recipe_search(ingredient)

    ## Getting recipes that match the user-search criteria
    for result in results:
        
        ### Extracting the selected information from the data of JSON (dictionary):
        #### Looking for matching recipes - through the URL that we have previously set up
        recipe = result['recipe']

        #### Recipe title in recipe
        print(recipe['label'])

        #### Links to recipe available on the Edamam site
        print(recipe['shareAs'])


# Executing the function        
run()
