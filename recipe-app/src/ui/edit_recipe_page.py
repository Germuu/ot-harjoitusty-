import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class EditRecipe:
    def __init__(self, root, handle_save, recipe_to_edit):
        self._root = root
        self._handle_save = handle_save
        self._recipe_to_edit = recipe_to_edit
        self._frame = None

        self.initialize()

    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self._root)

        # Name
        name_label = tk.Label(self._frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self._name_entry = tk.Entry(self._frame)
        self._name_entry.insert(0, self._recipe_to_edit.name)
        self._name_entry.grid(row=0, column=1, padx=5, pady=5)

        # Ingredients
        ingredients_label = tk.Label(self._frame, text="Ingredients:")
        ingredients_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self._ingredients_entry = tk.Entry(self._frame)
        self._ingredients_entry.insert(0, self._recipe_to_edit.ingredients)
        self._ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

        # Max Time
        time_label = tk.Label(self._frame, text="Max Time:")
        time_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
        self._max_time_entry = tk.Entry(self._frame)
        self._max_time_entry.insert(0, str(self._recipe_to_edit.cooking_time))
        self._max_time_entry.grid(row=2, column=1, padx=5, pady=5)

        # Save Button
        save_button = tk.Button(self._frame, text="Save", command=self.edit)
        save_button.grid(row=3, columnspan=2, padx=5, pady=5)
    
    def edit(self):
        # Get the new values from the entry fields
        new_name = self._name_entry.get()
        new_ingredients = self._ingredients_entry.get()
        new_max_time = int(self._max_time_entry.get())  # Convert to int

        # Call the service method to update the recipe
        recipe_app_service.update_recipe(self._recipe_to_edit.name, new_name, new_max_time, new_ingredients)

        # Show a success message
        messagebox.showinfo("Success", "Recipe updated successfully")

        # Call the handle_save method to refresh the view or navigate back
        self._handle_save()


