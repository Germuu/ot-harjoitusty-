from entities.recipe import Recipe
from entities.user import User
import hashlib

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

    def logout(self):
        self._user = None


recipe_service = RecipeAppService()
