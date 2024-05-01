import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class HomePage:
    """
    Class representing the home page.

    Args:
        root: The root Tkinter window.
        handle_my_recipes: The function to handle navigating to the My Recipes page.
        handle_find_recipes: The function to handle navigating to the Find Recipes page.
        handle_logout: The function to handle the logout process.
    """

    def __init__(self, root, handle_my_recipes, handle_find_recipes, handle_logout):
        """
        Initializes a new HomePage object.

        Args:
            root: The root Tkinter window.
            handle_my_recipes: The function to handle navigating to the My Recipes page.
            handle_find_recipes: The function to handle navigating to the Find Recipes page.
            handle_logout: The function to handle the logout process.
        """
        self._root = root
        self._current_view = None
        self._handle_my_recipes = handle_my_recipes
        self._handle_find_recipes = handle_find_recipes
        self._handle_logout = handle_logout
        self._current_user = recipe_app_service.get_current_user()
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the home page frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the home page frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the home page frame with welcome message and buttons."""
        self._frame = tk.Frame(master=self._root)

        label = tk.Label(self._frame, text=(
            f"Welcome! {self._current_user.username}"))
        label.pack()

        my_recipes_button = tk.Button(
            self._frame, text="My Recipes", command=self._handle_my_recipes)
        my_recipes_button.pack()

        find_recipes_button = tk.Button(
            self._frame, text="Find Recipes", command=self._handle_find_recipes)
        find_recipes_button.pack()

        logout_button = tk.Button(
            self._frame, text="Logout", command=self._handle_logout)
        logout_button.pack()
