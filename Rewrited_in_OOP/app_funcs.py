class Recipe:
    def __init__(self, name, description, instructions, ingredients=None):
        """Define every recipe common attributes like:
        name, description, ingredients, instructions (and they should also be shown in this order)"""
        self.name = name
        self.description = description
        self.instructions = instructions
        # Assign to self.ingredients entered ingredients OR empty list if nothing was entered
        self.ingredients = ingredients or []

    def _display_formatted(self):
        print(f"________________________\nRECIPE_NAME: {self.name}\n========================"
              f"\nDESCRIPTION:\n  {self.description}\n------------------------"
              f"\nINGREDIENTS:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"------------------------\nINSTRUCTIONS:\n  {self.instructions}\n------------------------")

bulka_z_maslem = Recipe("Bułka z masłem", "Szybkie śniadanie", "Kup bułkę, pokrój ją i posmaruj masłem",
                   ["bułka", "masło"])
bulka_z_maslem._display_formatted()

bulka_z_dzemem = Recipe("Bułka z dżemem", "Drugie szybkie śniadanie",
                        "Kup bułkę i dżem (jeśli go nie masz) i posmaruj masłem a potem dżemem",
                        ["bułka", "masło", "dżem"])
bulka_z_dzemem._display_formatted()