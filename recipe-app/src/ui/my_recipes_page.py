import tkinter as tk
from tkinter import ttk, messagebox, constants
from services.recipe_app_service import recipe_app_service


class MyRecipesPage:
    """
    Class representing the My Recipes page.

    Args:
        root: The root Tkinter window.
        handle_add: The function to handle adding a recipe.
        edit_recipe: The function to handle editing a recipe.
        handle_home_page: The function to handle going back to the home page.
        handle_refresh: The function to handle refreshing the page.
    """

    def __init__(self, root, handle_add, edit_recipe, handle_home_page, handle_refresh):
        """
        Initializes a new MyRecipesPage object.

        Args:
            root: The root Tkinter window.
            handle_add: The function to handle adding a recipe.
            edit_recipe: The function to handle editing a recipe.
            handle_home_page: The function to handle going back to the home page.
            handle_refresh: The function to handle refreshing the page.
        """
        self._root = root
        self._handle_add = handle_add
        self._handle_home_page = handle_home_page
        self._edit_recipe = edit_recipe
        self._handle_refresh = handle_refresh
        self._current_user = recipe_app_service.get_current_user()
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the My Recipes frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the My Recipes frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the My Recipes frame."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        label = tk.Label(self._frame, text="My Recipes", bg="#1E1E1E", fg="white")
        label.pack()

        add_button = tk.Button(
            self._frame, text="Add Recipe", command=self._handle_add, bg="#444444", fg="white")
        add_button.pack()

        # Scrollable frame to contain recipe entries
        scrollable_frame = tk.Frame(self._frame, bg="#1E1E1E")
        scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Fetch recipes for the current user
        recipes = recipe_app_service.fetch_recipes_by_user(
            self._current_user.username)

        for recipe in recipes:
            recipe_frame = tk.Frame(scrollable_frame, bg="#1E1E1E")
            recipe_frame.pack(fill=tk.X)

            # Display the recipe name
            recipe_label = tk.Button(recipe_frame, text=recipe.name, bg="#1E1E1E", fg="white",
                                     command=lambda name=recipe.name: self._edit_recipe(recipe))
            recipe_label.pack(side=tk.LEFT, padx=10, pady=5)

            # Create a delete button for each recipe
            delete_button = tk.Button(
                recipe_frame, text="X", command=lambda name=recipe.name: self.delete_recipe(name), bg="#444444", fg="white")
            delete_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Back button
        back_button = tk.Button(self._frame, text="Back",
                                command=self._handle_home_page, bg="#444444", fg="white")
        back_button.pack(side=tk.BOTTOM)
    
    def delete_recipe(self, recipe_name):
        """
        Deletes the specified recipe.
        Args:
            recipe_name: The name of the recipe to delete.
        """
        recipe_app_service.delete_recipe(recipe_name)
        self._handle_refresh()
