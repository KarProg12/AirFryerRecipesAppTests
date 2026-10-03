import app_funcs


my_recipe = app_funcs.RecipeManager()
my_recipe.add()

for recipe in my_recipe.recipes:
    print(recipe)