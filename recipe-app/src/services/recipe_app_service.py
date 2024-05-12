import hashlib
from entities.recipe import Recipe
from entities.user import User
from repositories.recipe_repository import recipe_repository as default_recipe_repository
from repositories.user_repository import user_repository as default_user_repository


class RecipeAppService:
    """
    Service class for handling interactions with recipes and users.

    Args:
        recipe_repository: An instance of RecipeRepository for managing recipes.
        user_repository: An instance of UserRepository for managing users.
    """

    def __init__(self, recipe_repository=default_recipe_repository,
                 user_repository=default_user_repository):
        """
        Initializes a new RecipeAppService object.

        Args:
            recipe_repository: An instance of RecipeRepository for managing recipes.
            user_repository: An instance of UserRepository for managing users.
        """
        self._user = None
        self._recipe_repository = recipe_repository
        self._user_repository = user_repository

    def register_user(self, username, password):
        """
        Register a new user.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.

        Returns:
            User: The newly registered user object, or None if registration fails.
        """

        new_user = User(username, password)
        self._user_repository.add_user(new_user)
        return new_user

    def login(self, username, password):
        """
        Log in a user.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.

        Returns:
            User or None: The logged-in user object, or None if login fails.
        """
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
        """
        Get the currently logged-in user.

        Returns:
            User: The currently logged-in user object.
        """
        return self._user

    def logout(self):
        """Log out the currently logged-in user."""
        self._user = None

    def create_recipe(self, name, ingredients, time, username):
        """
        Create a new recipe.

        Args:
            name (str): The name of the recipe.
            ingredients (str): The ingredients of the recipe.
            time (int): The cooking time of the recipe.
            username (str): The username of the recipe creator.

        Returns:
            Recipe: The newly created recipe object.
        """
        existing_recipe = self._recipe_repository.find_by_name(name)
        if existing_recipe:
            print(f"A recipe with the name '{name}' already exists.")
            return None
        new_recipe = Recipe(name, ingredients, time, username)
        self._recipe_repository.create(new_recipe)
        return new_recipe

    def get_all_recipes(self):
        """
        Retrieve all recipes.

        Returns:
            list: A list of Recipe objects representing all recipes.
        """
        return self._recipe_repository.retrieve_all()

    def find_recipe_by_name(self, name):
        """
        Find a recipe by name.

        Args:
            name (str): The name of the recipe to find.

        Returns:
            Recipe or None: The found recipe object, or None if not found.
        """
        return self._recipe_repository.find_by_name(name)

    def fetch_recipes_by_user(self, username):
        """
        Fetch recipes by user.

        Args:
            username (str): The username of the user.

        Returns:
            list: A list of Recipe objects created by the specified user.
        """
        return self._recipe_repository.fetch_recipes_by_user(username)

    def delete_recipe(self, recipe_name):
        """
        Delete a recipe.

        Args:
            recipe_name (str): The name of the recipe to delete.
        """
        return self._recipe_repository.delete_by_name(recipe_name)

    def update_recipe(self, recipe, new_name, new_cooking_time, new_ingredients):
        """
        Update a recipe.

        Args:
            recipe (Recipe): The original recipe object to be updated.
            new_name (str): The new name of the recipe.
            new_cooking_time (int): The new cooking time of the recipe.
            new_ingredients (str): The new ingredients of the recipe.
        """
        existing_recipe = recipe
        if not existing_recipe:
            print(f"Recipe with name {recipe.name} not found.")
        self._recipe_repository.update_recipe(
            recipe, new_name, new_cooking_time, new_ingredients)

    def search_recipes_algorithm(self, name, ingredients, max_time, username):
        """
        Search recipes by specified criteria.

        Args:
            name (str): The name of the recipe.
            ingredients (str): The ingredients of the recipe.
            max_time (int): The maximum cooking time of the recipe.
            username (str): The username of the recipe creator.

        Returns:
            list: A list of Recipe objects matching the criteria.
        """
        if max_time:
            max_time = int(max_time)
        return self._recipe_repository.search_recipes(name, max_time, ingredients, username)

    def get_random_recipe(self):
        """
        Get a random recipe.

        Returns:
            Recipe: A random Recipe object.
        """
        current_user = self.get_current_user().username
        random_recipe = self._recipe_repository.get_random_recipe_for_user(
            current_user)
        return random_recipe

    def validate_recipe_input(self, name, ingredients, time):
        """
        Validate recipe input fields.

        Args:
            name (str): The name of the recipe.
            ingredients (str): The ingredients of the recipe.
            time (str): The cooking time of the recipe.

        Returns:
            tuple: A tuple containing a boolean and error message.
        """

        name = name.strip()
        ingredients = ingredients.strip()
        time = time.strip()

        if len(name) == 0 or len(ingredients) == 0 or len(time) == 0:
            return False, "All fields are required"

        if len(name) > 100:
            return False, "Recipe name must be 100 characters or less"

        if len(ingredients) > 100:
            return False, "Ingredients must be 100 characters or less"

        try:
            time = int(time)
            if time <= 0 or time > 600:
                raise ValueError
        except ValueError:
            return False, "Cooking time must positive and less than 600"

        return True, None

    def validate_registration(self, username, password):
        if self._user_repository.find_by_username(username):
            return False, "Username already in use"

        if not username or not password:
            return False, "Please enter both username and password"
        if len(username) < 4:
            return False, "Username must be at least 4 characters"
        if len(username) > 15:
            return False, "Username cannot be more than 15 characters"
        if len(password) < 5:
            return False, "Password must be at least 5 characters"

        return True, None


recipe_app_service = RecipeAppService()
