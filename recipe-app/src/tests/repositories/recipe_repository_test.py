import unittest
from repositories.recipe_repository import recipe_repository
from entities.recipe import Recipe


class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        self.test_recipe1 = Recipe(
            "chicken pasta", 30, "parmesan, chicken, tomatos, basil", "admin")
        self.test_recipe2 = Recipe(
            "fajitas", 25, "salad, salsa, tomatos, meat", "admin")

    def test_create(self):
        recipe_repository.create(self.test_recipe1)
        all_recipes = recipe_repository.retrieve_all()
        self.assertEqual(all_recipes[0].name, "chicken pasta")

    def test_find_by_name(self):
        recipe_repository.create(self.test_recipe1)
        recipe = recipe_repository.find_by_name("chicken pasta")
        self.assertEqual(recipe.cooking_time, 30)

    def test_fetch_recipes_by_user(self):
        recipe_repository.create(self.test_recipe2)
        recipe_repository.create(self.test_recipe1)
        recipes = recipe_repository.fetch_recipes_by_user("admin")
        lista = [recipe.name for recipe in recipes]
        self.assertEqual(lista, ["fajitas", "chicken pasta"])
