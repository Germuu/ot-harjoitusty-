class Recipe:
    """
    Represents a recipe with its name, cooking time, ingredients, and the username of the creator.

    Attributes:
        name (str): The name of the recipe.
        cooking_time (int): The cooking time of the recipe in minutes.
        ingredients (str): The list of ingredients required for the recipe.
        username (str): The username of the creator of the recipe.
    """

    def __init__(self, name, cooking_time, ingredients, username):
        """
        Initializes a new Recipe object.

        Args:
            name (str): The name of the recipe.
            cooking_time (int): The cooking time of the recipe in minutes.
            ingredients (str): The list of ingredients required for the recipe.
            username (str): The username of the creator of the recipe.
        """
        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.username = username
