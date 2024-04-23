import tkinter as tk
from tkinter import constants


class RecipeDetailsPage:
    def __init__(self, root, recipe, go_back_callback):
        self._root = root
        self._recipe = recipe
        self._go_back_callback = go_back_callback
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self._root)

        # Recipe Name
        name_label = tk.Label(self._frame, text="Recipe Name:")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        name_value = tk.Label(self._frame, text=self._recipe.name)
        name_value.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        ingredients_label = tk.Label(self._frame, text="Ingredients:")
        ingredients_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ingredients_value = tk.Label(
            self._frame, text=self._recipe.ingredients)
        ingredients_value.grid(row=1, column=1, padx=5, pady=5)

        # Max Time
        time_label = tk.Label(self._frame, text="Max Time:")
        time_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        time_value = tk.Label(self._frame, text=str(self._recipe.cooking_time))
        time_value.grid(row=2, column=1, padx=5, pady=5)

        # Back Button
        back_button = tk.Button(self._frame, text="Back",
                                command=self._go_back_callback)
        back_button.grid(row=3, columnspan=2, padx=5, pady=5)
