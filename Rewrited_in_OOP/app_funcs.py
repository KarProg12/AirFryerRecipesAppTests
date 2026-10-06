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

class Commands:
    def __init__(self):
        self.commands_map = {}

    def show_in_table(self):
        pass

    def search(self):
        pass

    def remove(self):
        pass

    def help(self):
        help_menu = """
        > Type ['/end'] or ['/exit'] to escape the program.
        > Type ['/intable'] to display all recipes in table.
        > Type ['/search'] to search in recipes names or ingredients. 
        > Type ['/del'], ['/delete'] or ['/rm'] 
            to enter the deleting by name mode."""
        print(help_menu)

    def exit_app(self):
        """Func that escapes the program, saves everything and shows how """
