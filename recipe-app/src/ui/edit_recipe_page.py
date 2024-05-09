import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class EditRecipe:
    """
    Class representing the Edit Recipe page.

    Args:
        root: The root Tkinter window.
        handle_save: The function to handle saving changes to the recipe.
        recipe_to_edit: The recipe object to edit.
    """

    def __init__(self, root, handle_save, recipe_to_edit):
        """
        Initializes a new EditRecipe object.

        Args:
            root: The root Tkinter window.
            handle_save: The function to handle saving changes to the recipe.
            recipe_to_edit: The recipe object to edit.
        """
        self._root = root
        self._handle_save = handle_save
        self._recipe_to_edit = recipe_to_edit
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the edit recipe frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the edit recipe frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the edit recipe frame with entry fields and save button."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        # Name
        name_label = tk.Label(self._frame, text="Name:",
                              bg="#1E1E1E", fg="white")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self._name_entry = tk.Entry(self._frame)
        self._name_entry.insert(0, self._recipe_to_edit.name)
        self._name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        ingredients_label = tk.Label(
            self._frame, text="Ingredients:", bg="#1E1E1E", fg="white")
        ingredients_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self._ingredients_entry = tk.Entry(self._frame)
        self._ingredients_entry.insert(0, self._recipe_to_edit.ingredients)
        self._ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

        # Max Time
        time_label = tk.Label(self._frame, text="Max Time:",
                              bg="#1E1E1E", fg="white")
        time_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self._max_time_entry = tk.Entry(self._frame)
        self._max_time_entry.insert(0, str(self._recipe_to_edit.cooking_time))
        self._max_time_entry.grid(row=2, column=1, padx=5, pady=5)

        # Save Button
        save_button = tk.Button(self._frame, text="Save",
                                command=self.edit, bg="#444444", fg="white")
        save_button.grid(row=3, columnspan=2, padx=5, pady=5)

    def edit(self):
        """
        Saves the changes made to the recipe and notifies the user.
        """
        # Get the new values from the entry fields
        new_name = self._name_entry.get().strip()
        new_ingredients = self._ingredients_entry.get().strip()
        new_max_time = self._max_time_entry.get().strip()

        # Validate input
        validation_result, error_message = recipe_app_service.validate_recipe_input(
            new_name, new_ingredients, new_max_time)
        if not validation_result:
            messagebox.showerror("Error", error_message)
            return

        # Call the service method to update the recipe
        recipe_app_service.update_recipe(
            self._recipe_to_edit, new_name, new_max_time, new_ingredients)

        # Show a success message
        messagebox.showinfo("Success", "Recipe updated successfully")

        # Call the handle_save method to refresh the view or navigate back
        self._handle_save()
