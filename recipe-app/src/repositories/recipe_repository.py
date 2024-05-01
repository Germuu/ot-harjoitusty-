from entities.recipe import Recipe
from database_connection import get_database_connection

class RecipeRepository:
    """
    Repository for interacting with the recipes table in the database.

    Args:
        connection: Database connection object.
    """

    def __init__(self, connection):
        """
        Initializes a new RecipeRepository object.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def create(self, recipe):
        """
        Insert a new recipe into the recipes table.

        Args:
            recipe (Recipe): The recipe object to be inserted.
        """
        query = "INSERT INTO recipes (name, cooking_time, ingredients, username) VALUES (?, ?, ?, ?)"
        self._connection.execute(
            query, (recipe.name, recipe.cooking_time, recipe.ingredients, recipe.username))
        self._connection.commit()

    def retrieve_all(self):
        """
        Retrieve all recipes from the recipes table.

        Returns:
            list: A list of Recipe objects representing all recipes in the database.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes")
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"]) for row in rows]

    def find_by_name(self, name):
        """
        Retrieve a recipe from the recipes table by name.

        Args:
            name (str): The name of the recipe to retrieve.

        Returns:
            Recipe or None: The Recipe object representing the found recipe, or None if not found.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes WHERE name = ?", (name,))
        row = cursor.fetchone()
        return Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"]) if row else None

    def delete_all(self):
        """
        Delete all recipes from the recipes table.
        """
        query = "DELETE FROM recipes"
        self._connection.execute(query)
        self._connection.commit()

    def find_by_cooking_time(self, max_cooking_time):
        """
        Retrieve recipes from the recipes table with cooking times less than or equal to the specified maximum cooking time.

        Args:
            max_cooking_time (int): The maximum cooking time in minutes.

        Returns:
            list: A list of Recipe objects representing recipes with cooking times less than or equal to the specified maximum cooking time.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes WHERE cooking_time <= ?", (max_cooking_time,))
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"]) for row in rows]

    def fetch_recipes_by_user(self, username):
        """
        Retrieve recipes from the recipes table by the specified username.

        Args:
            username (str): The username of the user whose recipes to retrieve.

        Returns:
            list: A list of Recipe objects representing recipes created by the specified user.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes WHERE username = ?", (username,))
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"]) for row in rows]

    def delete_by_name(self, name):
        """
        Delete a recipe from the recipes table by name.

        Args:
            name (str): The name of the recipe to delete.
        """
        query = "DELETE FROM recipes WHERE name = ?"
        self._connection.execute(query, (name,))
        self._connection.commit()

    def update_recipe(self, recipe, new_name, new_cooking_time, new_ingredients):
        """
        Update a recipe in the recipes table.

        Args:
            recipe (Recipe): The original recipe object to be updated.
            new_name (str): The new name of the recipe.
            new_cooking_time (int): The new cooking time of the recipe in minutes.
            new_ingredients (str): The new list of ingredients for the recipe.
        """
        query = "UPDATE recipes SET name=?, cooking_time=?, ingredients=? WHERE name=?"
        self._connection.execute(
            query, (new_name, new_cooking_time, new_ingredients, recipe.name))
        self._connection.commit()

    def get_random_recipe_for_user(self, user):
        """
        Retrieve a random recipe created by the specified user.

        Args:
            user (str): The username of the user.

        Returns:
            Recipe or None: A random Recipe object created by the specified user, or None if no recipe is found.
        """
        query = "SELECT * FROM recipes WHERE username = ? ORDER BY RANDOM() LIMIT 1"
        cursor = self._connection.cursor()
        cursor.execute(query, (user,))
        row = cursor.fetchone()
        if row:
            return Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"])
        return None

    def search_recipes(self, name, max_time, ingredients, username):
        """
        Search for recipes in the recipes table based on the specified criteria.

        Args:
            name (str): The name or partial name of the recipe to search for.
            max_time (int): The maximum cooking time in minutes.
            ingredients (str): The ingredients or partial ingredients of the recipe to search for.
            username (str): The username of the user who created the recipes.

        Returns:
            list: A list of Recipe objects representing recipes matching the search criteria.
        """
        query = "SELECT * FROM recipes WHERE name LIKE ? AND cooking_time <= ? AND ingredients LIKE ? AND username = ?"
        cursor = self._connection.cursor()
        cursor.execute(query, (f"%{name}%", max_time, f"%{ingredients}%", username))
        rows = cursor.fetchall()
        return [Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"]) for row in rows]

# Instantiate RecipeRepository with database connection
recipe_repository = RecipeRepository(get_database_connection())
