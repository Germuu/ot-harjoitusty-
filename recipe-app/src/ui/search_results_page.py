import tkinter as tk
from tkinter import messagebox
from services.recipe_app_service import recipe_app_service


class SearchResultsPage:
    def __init__(self, root, search_results):
        self._root = root
        self._frame = None
        self._search_results = search_results

        self.initialize()

    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self._root)

        # Display search results
        for i, recipe in enumerate(self._search_results):
            recipe_frame = tk.Frame(self._frame, borderwidth=2, relief="solid")
            recipe_frame.grid(row=i, column=0, sticky="ew", padx=5, pady=5)

            # Recipe name
            name_label = tk.Label(recipe_frame, text=f"Name: {recipe.name}")
            name_label.pack(anchor="w")

            # Recipe ingredients
            ingredients_label = tk.Label(
                recipe_frame, text=f"Ingredients: {recipe.ingredients}")
            ingredients_label.pack(anchor="w")

            # Recipe max time
            time_label = tk.Label(
                recipe_frame, text=f"Max Time: {recipe.cooking_time}")
            time_label.pack(anchor="w")
