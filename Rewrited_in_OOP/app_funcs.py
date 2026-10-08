class Recipe:
    def __init__(self, name, description, instructions, ingredients=None):
        """Define every recipe common attributes like:
        name, description, ingredients, instructions (and they should also be shown in this order)"""
        self.name = name
        self.description = description
        self.instructions = instructions
        # Assign to self.ingredients entered ingredients OR empty list if nothing was entered
        self.ingredients = ingredients or []


