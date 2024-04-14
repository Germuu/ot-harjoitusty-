import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service

class MyRecipesPage:
    def __init__(self, root, handle_home_page):
        self.root = root
        self._handle_home_page = handle_home_page
        self._frame = None
        
        self.initialize()
    
    def pack(self):
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        self._frame.destroy()

    def initialize(self):
        self._frame = tk.Frame(master=self.root)

        label = tk.Label(self._frame, text="My Recipes")
        label.pack()

        # Define UI elements for displaying recipes
        # Add buttons, labels, or other widgets as needed

        back_button = tk.Button(self._frame, text="Back", command=self._handle_home_page)
        back_button.pack(side=tk.BOTTOM)
