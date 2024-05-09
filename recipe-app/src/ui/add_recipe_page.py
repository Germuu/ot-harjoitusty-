import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class AddRecipePage:
    """
    Class representing the Add Recipe page.

    Args:
        root: The root Tkinter window.
        handle_save: The function to handle saving the recipe.
        handle_back: The function to handle going back to the previous page.
    """

    def __init__(self, root, handle_save, handle_back):
        """
        Initializes a new AddRecipePage object.

        Args:
            root: The root Tkinter window.
            handle_save: The function to handle saving the recipe.
            handle_back: The function to handle going back to the previous page.
        """
        self._root = root
        self._handle_save = handle_save
        self._handle_back = handle_back
        self._frame = None
        self._name_entry = None
        self._ingredients_entry = None
        self._time_entry = None
        self._current_user = recipe_app_service.get_current_user()

        self.initialize()

    def pack(self):
        """Packs the add recipe frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the add recipe frame."""
        self._frame.destroy()

    def add(self):
        """
        Adds a new recipe with the input values and notifies the user of the outcome.
        """

        name = self._name_entry.get().strip()
        ingredients = self._ingredients_entry.get().strip()
        time = self._time_entry.get().strip()

        validation_result, error_message = recipe_app_service.validate_recipe_input(
            name, ingredients, time)
        if not validation_result:
            messagebox.showerror("Error", error_message)
            return

        new_recipe = recipe_app_service.create_recipe(
            name, time, ingredients, self._current_user.username)
        if new_recipe:
            messagebox.showinfo(
                "Success", f"Recipe '{name}' added successfully")
            self._handle_save()
        else:
            messagebox.showerror("Error", f"Recipe '{name}' already exists")

    def initialize(self):
        """Initializes the add recipe frame with entry fields and add button."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        name_label = tk.Label(self._frame, text="Name:",
                              bg="#1E1E1E", fg="white")
        name_label.pack()
        self._name_entry = tk.Entry(self._frame)
        self._name_entry.pack()

        ingredients_label = tk.Label(
            self._frame, text="Ingredients:", bg="#1E1E1E", fg="white")
        ingredients_label.pack()
        self._ingredients_entry = tk.Entry(self._frame)
        self._ingredients_entry.pack()

        time_label = tk.Label(
            self._frame, text="Cooking time in minutes:", bg="#1E1E1E", fg="white")
        time_label.pack()
        self._time_entry = tk.Entry(self._frame)
        self._time_entry.pack()

        add_button = tk.Button(
            self._frame, text="Add Recipe", command=self.add, bg="#444444", fg="white")
        add_button.pack()

        back_button = tk.Button(
            self._frame, text="Back", command=self._handle_back, bg="#444444", fg="white")
        back_button.pack()
