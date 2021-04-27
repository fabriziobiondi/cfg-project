#import library of recipes
import py_edamam
#importing ability to communicate with site
import requests

#setting up search fuction with id and key so we can get data and will produce url
def recipe_search(ingredient):
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id=c457e479&app_key=30acb7fe7dbb730ae70f3b81f1ce1d9f'.format(ingredient)
    )
    #makes the javascript information and data readable
    data = result.json()
    #hits means matching results hits is part of api
    return data['hits']

#what the user experiences
def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)


    for result in results:
        recipe = result['recipe']
        print(recipe['label'])
        print(recipe['shareAs'])
        print()
run()
