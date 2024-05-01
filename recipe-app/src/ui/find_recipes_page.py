import tkinter as tk
from tkinter import messagebox
from services.recipe_app_service import recipe_app_service

class FindRecipesPage:
    """
    Class representing the Find Recipes page.

    Args:
        root: The root Tkinter window.
        handle_search: The function to handle searching for recipes.
        handle_homepage: The function to handle navigating back to the homepage.
    """

    def __init__(self, root, handle_search, handle_homepage):
        """
        Initializes a new FindRecipesPage object.

        Args:
            root: The root Tkinter window.
            handle_search: The function to handle searching for recipes.
            handle_homepage: The function to handle navigating back to the homepage.
        """
        self._root = root
        self._frame = None
        self._handle_search = handle_search
        self._handle_homepage = handle_homepage

        self.initialize()

    def pack(self):
        """Packs the find recipes frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the find recipes frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the find recipes frame with search criteria and buttons."""
        self._frame = tk.Frame(master=self._root)

        # Name
        name_label = tk.Label(self._frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = tk.Entry(self._frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        ingredients_label = tk.Label(self._frame, text="Ingredients:")
        ingredients_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.ingredients_entry = tk.Entry(self._frame)
        self.ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

        # Max Time
        time_label = tk.Label(self._frame, text="Max Time:")
        time_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self.max_time_entry = tk.Entry(self._frame)
        self.max_time_entry.grid(row=2, column=1, padx=5, pady=5)

        # Search Button
        search_button = tk.Button(
            self._frame, text="Search", command=self.display_search)
        search_button.grid(row=3, columnspan=2, padx=5, pady=5)

        # Random Button
        random_button = tk.Button(
            self._frame, text="Random", command=self.random_recipe)
        random_button.grid(row=4, columnspan=2, padx=5, pady=5)

        # Label to display random recipe
        self.random_recipe_label = tk.Label(self._frame, text="")
        self.random_recipe_label.grid(row=5, columnspan=2, padx=5, pady=5)

        # Button to go back to homepage
        homepage_button = tk.Button(
            self._frame, text="Homepage", command=self._handle_homepage)
        homepage_button.grid(row=6, columnspan=2, padx=5, pady=5)

    def display_search(self):
        """
        Collects search criteria from UI and triggers a search for recipes.
        """
        name = self.name_entry.get()
        ingredients = self.ingredients_entry.get()
        max_time = self.max_time_entry.get()
        username = recipe_app_service.get_current_user().username
        search_results = recipe_app_service.search_recipes_algorithm(
            name, ingredients, max_time, username)

        self._handle_search(search_results)

    def random_recipe(self):
        """
        Retrieves a random recipe and displays its name.
        """
        random_recipe = recipe_app_service.get_random_recipe()
        self.random_recipe_label.config(text=random_recipe.name)
