class Recipe:
    # Variable type annotation for better readability and insights
    name: str
    description: str
    instructions: str
    ingredients: list[str]

    def __init__(self, name, description, instructions, ingredients=None):
        """Define every recipe common attributes like:
        name, description, ingredients, instructions (and they should also be shown in this order)"""
        self.name = name
        self.description = description
        self.instructions = instructions
        # Assign to self.ingredients entered ingredients OR empty list if nothing was entered
        self.ingredients = ingredients or []

    def display_formatted(self):
        print(f"________________________\nRECIPE_NAME: {self.name}\n========================"
              f"\nDESCRIPTION:\n  {self.description}\n------------------------"
              f"\nINGREDIENTS:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"------------------------\nINSTRUCTIONS:\n  {self.instructions}\n------------------------")