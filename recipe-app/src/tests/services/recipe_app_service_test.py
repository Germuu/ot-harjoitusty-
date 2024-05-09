import unittest
from entities.recipe import Recipe
from entities.user import User
from repositories.user_repository import user_repository
from services.recipe_app_service import recipe_app_service


class TestRecipeAppService(unittest.TestCase):
    def setUp(self):
        user_repository.clear()
        self.test_username = "admin"
        self.test_password = "1234"
        self.user = recipe_app_service.register_user(
            self.test_username, self.test_password)

    def test_register_user(self):
        self.assertEqual(self.user.username, "admin")

    def test_login_succesful(self):
        user = recipe_app_service.login(self.test_username, self.test_password)
        self.assertEqual(
            user.username, user_repository.retrieve_all()[0].username)

    def test_login_wrong_password(self):
        user = recipe_app_service.login(self.test_username, "wrong password")
        self.assertEqual(user, None)

    def test_login_username_not_exists(self):
        user = recipe_app_service.login("not exists", self.test_password)
        self.assertEqual(user, None)

    def test_get_current_user(self):
        recipe_app_service.login(self.test_username, self.test_password)
        user = recipe_app_service.get_current_user()
        self.assertEqual(
            user.username, user_repository.retrieve_all()[0].username)

    def test_logout(self):
        recipe_app_service.login(self.test_username, self.test_password)
        recipe_app_service.logout()
        self.assertEqual(recipe_app_service.get_current_user(), None)

    def test_create_recipe(self):
        pass
