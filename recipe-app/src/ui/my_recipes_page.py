import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class MyRecipesPage:
    def __init__(self, root, handle_add, edit_recipe, handle_home_page, handle_refresh):
        self.root = root
        self._handle_add = handle_add
        self._handle_home_page = handle_home_page
        self._edit_recipe = edit_recipe
        self._handle_refresh = handle_refresh
        self._current_user = recipe_app_service.get_current_user()
        self._frame = None
        
        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self.root)

        label = tk.Label(self._frame, text="My Recipes")
        label.pack()

        add_button = tk.Button(self._frame, text="Add Recipe", command=self._handle_add)
        add_button.pack()

        # Scrollable frame to contain recipe entries
        scrollable_frame = tk.Frame(self._frame)
        scrollable_frame.pack(fill=tk.BOTH, expand=True)

        # Fetch recipes for the current user
        recipes = recipe_app_service.fetch_recipes_by_user(self._current_user.username)

        for recipe in recipes:
            recipe_frame = tk.Frame(scrollable_frame)
            recipe_frame.pack(fill=tk.X)

            # Display the recipe name
            recipe_label = tk.Label(recipe_frame, text=recipe.name)
            recipe_label.pack(side=tk.LEFT, padx=10, pady=5)

            # Create a delete button for each recipe
            delete_button = tk.Button(recipe_frame, text="X", command=lambda name=recipe.name: self.delete_recipe(name))
            delete_button.pack(side=tk.RIGHT, padx=10, pady=5)

        # Back button
        back_button = tk.Button(self._frame, text="Back", command=self._handle_home_page)
        back_button.pack(side=tk.BOTTOM)


    def delete_recipe(self, recipe_name):
        recipe_app_service.delete_recipe(recipe_name)
        self._handle_refresh()

