import tkinter as tk
from tkinter import ttk, messagebox, constants
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
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

    def destroy(self):
        """Destroys the home page frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the home page frame with welcome message and buttons."""
        self._frame = tk.Frame(master=self._root)

        # Apply the theme to the frame
        self._frame["bg"] = "#1E1E1E"  # Background color

        label = tk.Label(self._frame, text=f"Welcome! {self._current_user.username}", bg="#1E1E1E", fg="white")
        label.grid(row=0, column=0, columnspan=2, pady=10)

        # Apply the theme to the buttons
        button_style = ttk.Style()
        button_style.configure("Dark.TButton", foreground="white", background="#444444")

        my_recipes_button = ttk.Button(self._frame, text="My Recipes", style="Dark.TButton", command=self._handle_my_recipes)
        my_recipes_button.grid(row=1, column=0, padx=10, pady=5)

        find_recipes_button = ttk.Button(self._frame, text="Find Recipes", style="Dark.TButton", command=self._handle_find_recipes)
        find_recipes_button.grid(row=1, column=1, padx=10, pady=5)

        logout_button = ttk.Button(self._frame, text="Logout", style="Dark.TButton", command=self._handle_logout)
        logout_button.grid(row=2, column=0, columnspan=2, pady=5)
