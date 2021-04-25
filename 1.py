import py_edamam
import requests

def _init_(ingredient, app_id, app_key):

    def recipe_search(ingredient):
        ingredient.app_id = '7ce35082'
        ingredient.app_key = 'b9556c7fe5a71c999ae5db61af5beb8f'
result = requests.get(
'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id,

app_key)
)
data = result.json()
return data['hits']
def run():
    ingredient = input('Enter an ingredient: ')
    results = recipe_search(ingredient)
for result in results:
    recipe = result['recipe']
print(recipe['label'])
print(recipe['uri'])
print()
run()

