import tkinter as tk
from tkinter import messagebox


class SearchResultsPage:
    """
    Class representing the search results page.

    Args:
        root: The root Tkinter window.
        search_results: The list of recipes to display as search results.
        handle_recipe_details: The function to handle clicks on recipe details.
        handle_back: The function to handle going back to the previous page.
    """

    def __init__(self, root, search_results, handle_recipe_details, handle_back):
        """
        Initializes a new SearchResultsPage object.

        Args:
            root: The root Tkinter window.
            search_results: The list of recipes to display as search results.
            handle_recipe_details: The function to handle clicks on recipe details.
            handle_back: The function to handle going back to the previous page.
        """
        self._root = root
        self._search_results = search_results
        self._handle_recipe_details = handle_recipe_details
        self._handle_back = handle_back
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the search results frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the search results frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the search results frame and displays search results."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        if not self._search_results:
            no_results_label = tk.Label(self._frame, text="No recipes found", bg="#1E1E1E", fg="white")
            no_results_label.grid(row=0, column=0, pady=5)

        back_button = tk.Button(self._frame, text="Back", command=self._handle_back, bg="#444444", fg="white")
        back_button.grid(row=1, column=0, pady=5)

        if self._search_results:
            for i, recipe in enumerate(self._search_results):
                recipe_frame = tk.Frame(
                    self._frame, borderwidth=2, relief="solid", bg="white")
                recipe_frame.grid(row=i + 2, column=0,
                                  sticky="ew", padx=5, pady=5)

                recipe_frame.bind("<Enter>", lambda event,
                                  frame=recipe_frame: self._on_enter(frame))
                recipe_frame.bind("<Leave>", lambda event,
                                  frame=recipe_frame: self._on_leave(frame))
                recipe_frame.bind("<Button-1>", lambda event, r=recipe,
                                  frame=recipe_frame: self._handle_recipe_click(r))

                # Recipe name
                name_label = tk.Label(
                    recipe_frame, text=f"Name: {recipe.name}", bg="white")
                name_label.pack(anchor="w")

                # Recipe ingredients
                ingredients_label = tk.Label(
                    recipe_frame, text=f"Ingredients: {recipe.ingredients}", bg="white")
                ingredients_label.pack(anchor="w")

                # Recipe max time
                time_label = tk.Label(
                    recipe_frame, text=f"Max Time: {recipe.cooking_time}", bg="white")
                time_label.pack(anchor="w")

    def _handle_recipe_click(self, recipe):
        """
        Handles the click event on a recipe frame.

        Args:
            recipe: The recipe object associated with the clicked frame.
        """
        self._handle_recipe_details(recipe)

    def _on_enter(self, frame):
        """
        Changes background color when mouse enters a recipe frame.

        Args:
            frame: The recipe frame where the mouse entered.
        """
        frame.config(bg="lightgrey")

    def _on_leave(self, frame):
        """
        Changes background color back to white when mouse leaves a recipe frame.

        Args:
            frame: The recipe frame where the mouse left.
        """
        frame.config(bg="white")
