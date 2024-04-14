import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class HomePage:
    def __init__(self, root, handle_my_recipes, handle_find_recipes, handle_logout ):
        self.root = root
        self._current_view = None
        self._handle_my_recipes = handle_my_recipes
        self._handle_find_recipes = None
        self._handle_logout = handle_logout
        self._current_user = recipe_app_service.get_current_user()
        self._frame = None
    
        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self.root)

        label = tk.Label(self._frame, text=(f"Welcome! {self._current_user.username}"))
        label.pack()

        my_recipes_button = tk.Button(self._frame, text="My Recipes", command=self._handle_my_recipes)
        my_recipes_button.pack()

        find_recipes_button = tk.Button(self._frame, text="Find Recipes", command=self._handle_find_recipes)
        find_recipes_button.pack()

        logout_button = tk.Button(self._frame, text="Logout", command=self._handle_logout)
        logout_button.pack()


 


        