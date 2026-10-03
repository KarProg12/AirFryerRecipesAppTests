import difflib
import textwrap
import inquirer

class Recipe:
    def __init__(self, recipe_name, description, instructions, *ingredients):
        self.description = str(description)
        self.recipe_name = str(recipe_name)
        self.instructions = str(instructions)
        self.ingredients = list(ingredients)

    def __str__(self) -> str:
        formatted_ingredients = "\n".join(f" - {ingredient}" for ingredient in self.ingredients)

        return (f"\nRECIPE_NAME: {self.recipe_name}"
                f"\nDESCRIPTION:\n  {self.description}"
                f"\nINGREDIENTS:\n{formatted_ingredients}"
                f"\nINSTRUCTIONS:\n  {self.instructions}")

    def __repr__(self) -> str:
        return self.__str__()

class RecipeManager:
    def __init__(self):
        self.recipes = []

    def add(self):
        description = "Szybkie śniadanie"
        recipe_name = "Jajecznica"
        ingredients = ('jajka', 'masło', 'sól', 'pieprz')
        instructions = "Rozbij jajka na patelnię i mieszaj"

        new_recipe = Recipe(recipe_name, description, instructions, *ingredients)
        self.recipes.append(new_recipe)
        print(f"\nAdded recipe: {recipe_name}")

    def remove_recipe(self):
        pass

    def search_recipe(self):
        pass

    def run_app(self):
        pass

