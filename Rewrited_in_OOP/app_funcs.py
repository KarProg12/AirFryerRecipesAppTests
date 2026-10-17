class Recipe:
    # Variable type annotation for better readability and insights
    name: str
    description: str
    ingredients: list[str]
    instructions: str

    def __init__(self, name, description, instructions, ingredients=None):
        """Define every recipe common attributes like:
        name, description, ingredients, instructions
        (and they should also be shown in this order)"""
        self.name = name
        self.description = description
        self.instructions = instructions
        # Assign to self.ingredients entered ingredients OR empty list if nothing was entered
        self.ingredients = ingredients or []

    def describe_recipe(self):
        describer = Describer()
        describer.display_recipe_formatted(self)


class Describer:
    """All recipes descriptions in one class"""

    def display_recipe_formatted(self, recipe: Recipe):
        print(
            f"________________________\nRECIPE_NAME: {recipe.name}\n========================"
            f"\nDESCRIPTION:\n  {recipe.description}\n------------------------"
            f"\nINGREDIENTS:"
        )
        for ingredient in recipe.ingredients:
            print(f"- {ingredient}")
        print(
            f"------------------------\nINSTRUCTIONS:\n  {
                recipe.instructions
            }\n------------------------"
        )


class RecipesManager:
    formatted_recipes: dict[str, Recipe]

    def __init__(self):
        self.formatted_recipes = {}

    def add_recipe_to_formatted(
        self, recipe_name: str, recipe_class_instance_name: Recipe
    ):
        """Requires to enter name of the instance of the class Recipe"""
        self.formatted_recipes[recipe_name] = recipe_class_instance_name

    def add_recipe(self):
        name_input = input("\n>>> Enter recipe name\n>>> ")
        description_input = input("\n>>> Enter recipe description\n>>> ")
        instructions_input = input("\n>>> Enter recipe instructions\n>>> ")
        ingredients_input = input("\n>>> Enter recipe ingredients\n>>> ")