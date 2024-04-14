import hashlib
from entities.recipe import Recipe
from entities.user import User


from repositories.recipe_repository import (
    recipe_repository as default_recipe_repository
)

from repositories.user_repository import (
    user_repository as default_user_repository
)


class RecipeAppService:
    def __init__(
        self,
        recipe_repository=default_recipe_repository,
        user_repository=default_user_repository
    ):
        self._user = None
        self._recipe_repository = recipe_repository
        self._user_repository = user_repository

    def register_user(self, username, password):

        existing_user = self._user_repository.find_by_username(username)
        if existing_user:
            print(f"Username {username} already in use")
        else:
            new_user = User(username, password)
            self._user_repository.add_user(new_user)

        return new_user

    def login(self, username, password):
        user = self._user_repository.find_by_username(username)
        if user:
            if user.password == hashlib.sha256(password.encode()).hexdigest():
                self._user = user
            else:
                print("Incorrect password")
                return None
        else:
            print("User not found")
            return None

        return user
    
    def get_current_user(self):
        return self._user 

    def logout(self):
        self._user = None
    


    def create_recipe(self, name, ingredients, time):
        # Check if a recipe with the same name already exists
        existing_recipe = self._recipe_repository.find_by_name(name)
        if existing_recipe:
            print(f"A recipe with the name '{name}' already exists.")
            return None

        new_recipe = Recipe(name, ingredients, time)
        self._recipe_repository.create(new_recipe)

        return new_recipe

    def get_all_recipes(self):
        return self._recipe_repository.retrieve_all()

    def find_recipe_by_name(self, name):
        return self._recipe_repository.find_by_name(name)

    def find_recipes_by_cooking_time(self, max_cooking_time):
        return self._recipe_repository.find_by_cooking_time(max_cooking_time)

    def find_recipes_by_ingredients(self, ingredients):
        return self._recipe_repository.find_by_ingredients(ingredients)

    def fetch_recipes_by_user(self, user_id):
        return self._recipe_repository.fetch_recipes_by_user(user_id)
    
    def delete_recipe(self, recipe_name):
        # Check if the user is logged in
        if not self._user:
            print("User is not logged in.")
            return False

        # Check if the recipe exists
        existing_recipe = self._recipe_repository.find_by_name(recipe_name)
        if not existing_recipe:
            print(f"Recipe with name '{recipe_name}' not found.")
            return False

        # Check if the recipe belongs to the logged-in user
        if existing_recipe.user_id != self._user.id:
            print(f"Recipe '{recipe_name}' does not belong to the current user.")
            return False

        # Delete the recipe
        self._recipe_repository.delete_by_name(recipe_name)
        print(f"Recipe '{recipe_name}' deleted successfully.")
        return True    


recipe_app_service = RecipeAppService()
