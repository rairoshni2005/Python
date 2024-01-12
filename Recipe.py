class Ingredient:
    def __init__(self, name):
        self.name = name

class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class User:
    def __init__(self, username):
        self.username = username
        self.saved_recipes = []

    def add_saved_recipe(self, recipe):
        self.saved_recipes.append(recipe)

# RecipeManager class to manage recipes and users
class RecipeManager:
    def __init__(self):
        self.recipes = []
        self.users = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_by_ingredient(self, ingredient_name):
        # Search for recipes containing a specific ingredient
        matching_recipes = []
        for recipe in self.recipes:
            if any(ingredient.name.lower() == ingredient_name.lower() for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

    def add_user(self, user):
        self.users.append(user)

# Example usage:
# Create ingredients
ingredient1 = Ingredient(name="Chicken")
ingredient2 = Ingredient(name="Rice")
ingredient3 = Ingredient(name="Tomato")

# Create recipes
recipe1 = Recipe(name="Chicken Curry", ingredients=[ingredient1, ingredient2, ingredient3], instructions="Cook and enjoy!")
recipe2 = Recipe(name="Vegetable Stir-Fry", ingredients=[ingredient2, ingredient3], instructions="Stir-fry and serve.")

# Create users
user1 = User(username="JohnDoe")
user2 = User(username="JaneSmith")

# Create a RecipeManager and add recipes
recipe_manager = RecipeManager()
recipe_manager.add_recipe(recipe1)
recipe_manager.add_recipe(recipe2)

# Add users to RecipeManager
recipe_manager.add_user(user1)
recipe_manager.add_user(user2)

# User saves a recipe
user1.add_saved_recipe(recipe1)

# Search for recipes by ingredient
ingredient_to_search = "Tomato"
matching_recipes = recipe_manager.search_by_ingredient(ingredient_to_search)

# Display matching recipes
print(f"Recipes containing {ingredient_to_search}:")
for recipe in matching_recipes:
    print(f"- {recipe.name}")

# Display saved recipes for a user
print(f"\n{user1.username}'s saved recipes:")
for saved_recipe in user1.saved_recipes:
    print(f"- {saved_recipe.name}")
