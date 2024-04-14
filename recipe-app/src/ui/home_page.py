import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class HomePage:
    def __init__(self, root, handle_home_page, handle_my_recipes, handle_find_recipes ):
        self.root = root
        self._current_view = None
        self._handle_home_page = handle_home_page
        self._handle_my_recipes = handle_my_recipes
        self._handle_find_recipes = handle_find_recipes
        self._frame = None
        
        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self.root)

        label = tk.Label(self._frame, text="Welcome!")
        label.pack()

        my_recipes_button = tk.Button(self._frame, text="My Recipes", command=self._handle_my_recipes)
        my_recipes_button.pack()

        find_recipes_button = tk.Button(self._frame, text="Find Recipes", command=self._handle_find_recipes)
        find_recipes_button.pack()

        logout_button = tk.Button(self._frame, text="Logout", command=self._handle_home_page)
        logout_button.pack()


 


        