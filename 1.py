#import library of recipes
import py_edamam
#importing ability to communicate with site
import requests

#setting up search fuction with id and key so we can get data and will produce url
def flower(paperclip):
    bench = requests.get(
        'https://api.edamam.com/search?q={}&app_id=c457e479&app_key=30acb7fe7dbb730ae70f3b81f1ce1d9f'.format(paperclip)
    )
    #makes the javascript information and data readable
    data = bench.json()
    #hits means matching results hits is part of api
    return data['hits']

#what the user experiences
def run():
    paperclip = input('Enter an ingredient: ')
    butterfly = flower(paperclip)


    for bench in butterfly:
        recipe = bench['recipe']
        print(recipe['label'])
        print(recipe['shareAs'])
        print()
run()
