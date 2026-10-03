import difflib
import textwrap
import inquirer

class Recipe:
    def __init__(self, description, recipe_name, instructions, *ingredients):
        self.description = str(description)
        self.recipe_name = str(recipe_name)
        self.instructions = str(instructions)
        self.ingredients = list(ingredients)

    def __str__(self) -> str:
        print(f"Recipe description:\n  {self.description}\n  Recipe name: {self.recipe_name}\n"
              f"  Ingredients:\n\t{self.ingredients}\n  Instructions:\n\t{self.instructions}")

class RecipeManager:
    def __init__(self):
        pass

    def add_recipe(self):
        pass

    def remove_recipe(self):
        pass

    def search_recipe(self):
        pass

class HandleSavingRecipes:
    def __init__(self):
        pass

