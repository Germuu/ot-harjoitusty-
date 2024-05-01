import tkinter as tk
from tkinter import constants

class RecipeDetailsPage:
    """
    Class representing the recipe details page.

    Args:
        root: The root Tkinter window.
        recipe: The recipe object to display details of.
        go_back_callback: The function to handle going back to the previous page.
    """

    def __init__(self, root, recipe, go_back_callback):
        """
        Initializes a new RecipeDetailsPage object.

        Args:
            root: The root Tkinter window.
            recipe: The recipe object to display details of.
            go_back_callback: The function to handle going back to the previous page.
        """
        self._root = root
        self._recipe = recipe
        self._go_back_callback = go_back_callback
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the recipe details frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the recipe details frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the recipe details frame."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        # Recipe Name
        name_label = tk.Label(self._frame, text="Recipe Name:", bg="#1E1E1E", fg="white")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        name_value = tk.Label(self._frame, text=self._recipe.name, bg="#1E1E1E", fg="white")
        name_value.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        ingredients_label = tk.Label(self._frame, text="Ingredients:", bg="#1E1E1E", fg="white")
        ingredients_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        ingredients_text = tk.Text(self._frame, wrap="word", height=10, width=40)
        ingredients_text.insert(tk.END, self._recipe.ingredients)
        ingredients_text.configure(state="disabled")
        ingredients_text.grid(row=1, column=1, padx=5, pady=5)

        # Max Time
        time_label = tk.Label(self._frame, text="Max Time:", bg="#1E1E1E", fg="white")
        time_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        time_value = tk.Label(self._frame, text=str(self._recipe.cooking_time), bg="#1E1E1E", fg="white")
        time_value.grid(row=2, column=1, padx=5, pady=5)

        # Back Button
        back_button = tk.Button(self._frame, text="Back", command=self._go_back_callback, bg="#444444", fg="white")
        back_button.grid(row=3, columnspan=2, padx=5, pady=5, sticky="ew")
