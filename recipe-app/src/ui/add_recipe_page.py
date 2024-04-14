import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class AddRecipePage:
    def __init__(self, root, handle_save):
        self._root = root
        self._handle_save = handle_save
        self._frame = None
        self._name_entry = None
        self._ingredients_entry = None
        self._time_entry = None
        self._current_user = recipe_app_service.get_current_user()
        
        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def add(self):
        # Get the input values from the entry fields
        name = self._name_entry.get()
        ingredients = self._ingredients_entry.get()
        time = self._time_entry.get()

        # Check if any field is empty
        if not name or not ingredients or not time:
            messagebox.showerror("Error", "All fields are required")
            return

        # Try to convert time to integer
        try:
            time = int(time)
        except ValueError:
            messagebox.showerror("Error", "Cooking time must be a number")
            return

        # Call the service method to add the recipe
        new_recipe = recipe_app_service.create_recipe(name, time, ingredients, self._current_user.username)
        if new_recipe:
            messagebox.showinfo("Success", f"Recipe '{name}' added successfully")
            self._handle_save()  # Handle the successful addition
        else:
            messagebox.showerror("Error", f"Recipe '{name}' already exists")

    def initialize(self):
        self._frame = tk.Frame(master=self._root)

        name_label = tk.Label(self._frame, text="Name:")
        name_label.pack()
        self._name_entry = tk.Entry(self._frame)
        self._name_entry.pack()

        ingredients_label = tk.Label(self._frame, text="Ingredients:")
        ingredients_label.pack()
        self._ingredients_entry = tk.Entry(self._frame)
        self._ingredients_entry.pack()

        time_label = tk.Label(self._frame, text="Cooking Time:")
        time_label.pack()
        self._time_entry = tk.Entry(self._frame)
        self._time_entry.pack()

        add_button = tk.Button(self._frame, text="Add Recipe", command=self.add)
        add_button.pack()
