class Recipe:
    def __init__(self, description, recipe_name, instructions, *ingredients):
        self.description = str(description)
        self.recipe_name = str(recipe_name)
        self.instructions = str(instructions)
        self.ingredients = list(ingredients)

class HandleSavingRecipes:
    def __init__(self):
        pass

class RecipeManager:
    def __init__(self):
        pass

    def add_recipe(self):
        pass
