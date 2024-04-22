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

    def create_recipe(self, name, ingredients, time, username):
        # Check if a recipe with the same name already exists
        existing_recipe = self._recipe_repository.find_by_name(name)
        if existing_recipe:
            print(f"A recipe with the name '{name}' already exists.")
            return None

        new_recipe = Recipe(name, ingredients, time, username)
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

    def fetch_recipes_by_user(self, username):
        return self._recipe_repository.fetch_recipes_by_user(username)

    def delete_recipe(self, recipe_name):
        return self._recipe_repository.delete_by_name(recipe_name)
    

    def update_recipe(self, old_name, new_name, new_cooking_time, new_ingredients):
        # Check if the recipe exists
        existing_recipe = self._recipe_repository.find_by_name(old_name)
        if not existing_recipe:
            print(f"Recipe with name {old_name} not found.")
            return None

        # Update the recipe
        self._recipe_repository.update_recipe(
            old_name, new_name, new_cooking_time, new_ingredients)


recipe_app_service = RecipeAppService()
