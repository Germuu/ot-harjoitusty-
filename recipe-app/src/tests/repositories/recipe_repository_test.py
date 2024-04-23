import unittest
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe


class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        recipe_repository.delete_all()
        self.test_recipe1 = Recipe("chicken pasta",30 ,"parmesan, chicken, tomatos, basil", "admin")

    def test_adding(self):
        recipe_repository.create(self.test_recipe1)
        all_recipes = recipe_repository.retrieve_all()
        self.assertEqual(all_recipes[0].name, "chicken pasta")
    



