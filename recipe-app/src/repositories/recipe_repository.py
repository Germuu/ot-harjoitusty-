from entities.recipe import Recipe
from database_connection import get_database_connection


class RecipeRepository:
    def __init__(self, connection):
        self._connection = connection

    def create(self, recipe):
        query = "INSERT INTO recipes \
                (name, cooking_time, ingredients, username) VALUES (?, ?, ?, ?)"
        self._connection.execute(
            query, (recipe.name, recipe.cooking_time, recipe.ingredients, recipe.username))
        self._connection.commit()

    def retrieve_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes")
        rows = cursor.fetchall()
        return [Recipe(row["name"],
                       row["cooking_time"],
                       row["ingredients"],
                       row["username"])
                for row in rows]

    def find_by_name(self, name):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM recipes WHERE name = ?", (name,))
        row = cursor.fetchone()
        return Recipe(row["name"],
                      row["cooking_time"],
                      row["ingredients"], row["username"]) if row else None

    def delete_all(self):
        query = "DELETE FROM recipes"
        self._connection.execute(query)
        self._connection.commit()

    def find_by_cooking_time(self, max_cooking_time):
        cursor = self._connection.cursor()
        cursor.execute(
            "SELECT * FROM recipes WHERE cooking_time <= ?", (max_cooking_time,))
        rows = cursor.fetchall()
        return [Recipe(row["name"],
                       row["cooking_time"],
                       row["ingredients"],
                       row["username"]) for row in rows]

    def fetch_recipes_by_user(self, username):
        cursor = self._connection.cursor()

        cursor.execute(
            "SELECT * FROM recipes WHERE username = ?",
            (username,)
        )

        rows = cursor.fetchall()

        return [Recipe(row["name"],
                       row["cooking_time"],
                       row["ingredients"],
                       row["username"]) for row in rows]

    def delete_by_name(self, name):
        query = "DELETE FROM recipes WHERE name = ?"
        self._connection.execute(query, (name,))
        self._connection.commit()

    def update_recipe(self, recipe, new_name, new_cooking_time, new_ingredients):
        query = "UPDATE recipes SET name=?, cooking_time=?, ingredients=? WHERE name=?"
        self._connection.execute(
            query, (new_name, new_cooking_time, new_ingredients, recipe.name))
        self._connection.commit()

    def get_random_recipe_for_user(self, user):
        query = "SELECT * FROM recipes WHERE username = ? ORDER BY RANDOM() LIMIT 1"
        cursor = self._connection.cursor()
        cursor.execute(query, (user,))
        row = cursor.fetchone()

        if row:
            return Recipe(row["name"], row["cooking_time"], row["ingredients"], row["username"])

        return None


recipe_repository = RecipeRepository(get_database_connection())
