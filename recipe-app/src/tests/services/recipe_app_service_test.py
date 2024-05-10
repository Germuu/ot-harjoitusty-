import unittest
from entities.recipe import Recipe
from entities.user import User
from repositories.user_repository import user_repository
from repositories.recipe_repository import recipe_repository
from services.recipe_app_service import recipe_app_service


class TestRecipeAppService(unittest.TestCase):
    def setUp(self):
        user_repository.clear()
        recipe_repository.delete_all()
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

    def test_create_recipe_not_exists(self):
        test_recipe = recipe_app_service.create_recipe("pasta", "cheese, penne", 15, "admin")
        self.assertEqual(test_recipe.name, "pasta")
    
    def test_create_recipe_exists(self):
        recipe_app_service.create_recipe("pasta", "cheese, penne", 15, "admin")
        fail_recipe = recipe_app_service.create_recipe("pasta", "minced meat", 35, "admin")
        self.assertEqual(fail_recipe, None)
