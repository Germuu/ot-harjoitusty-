import tkinter as tk
from services.recipe_app_service import recipe_app_service

class MyRecipesPage:
    """
    Class representing the My Recipes page.

    Args:
        root: The root Tkinter window.
        handle_add: The function to handle adding a recipe.
        edit_recipe: The function to handle editing a recipe.
        handle_home_page: The function to handle going back to the home page.
        handle_refresh: The function to handle refreshing the page.
    """

    def __init__(self, root, handle_add, edit_recipe, handle_home_page, handle_refresh):
        """
        Initializes a new MyRecipesPage object.

        Args:
            root: The root Tkinter window.
            handle_add: The function to handle adding a recipe.
            edit_recipe: The function to handle editing a recipe.
            handle_home_page: The function to handle going back to the home page.
            handle_refresh: The function to handle refreshing the page.
        """
        self._root = root
        self._handle_add = handle_add
        self._handle_home_page = handle_home_page
        self._edit_recipe = edit_recipe
        self._handle_refresh = handle_refresh
        self._current_user = recipe_app_service.get_current_user()
        self._frame = None

        self.initialize()

    def pack(self):
        """Packs the My Recipes frame into the root window."""
        self._frame.pack(fill=tk.BOTH, expand=True)

    def destroy(self):
        """Destroys the My Recipes frame."""
        self._frame.destroy()

    def initialize(self):
        """Initializes the My Recipes frame."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")
        self._frame.pack(fill=tk.BOTH, expand=True)  # Make frame fill the window

        label = tk.Label(self._frame, text="My Recipes",
                         bg="#1E1E1E", fg="white", font=("Helvetica", 20))  
        label.pack(pady=20)  

        add_button = tk.Button(
            self._frame, text="Add Recipe", command=self._handle_add, bg="#444444", fg="white", font=("Helvetica", 14))  # Increase font size
        add_button.pack(pady=10)  

       
        scrollable_frame = tk.Frame(self._frame, bg="#1E1E1E")
        scrollable_frame.pack(fill=tk.BOTH, expand=True)

        
        recipes = recipe_app_service.fetch_recipes_by_user(
            self._current_user.username)
        
        #generated code starts
        for recipe in recipes:
            recipe_frame = tk.Frame(scrollable_frame, bg="#1E1E1E")
            recipe_frame.pack(fill=tk.X, padx=20, pady=10)  

           
            recipe_label = tk.Button(recipe_frame, text=recipe.name, bg="#1E1E1E", fg="white",
                                     command=lambda name=recipe.name: self._edit_recipe(recipe))
            recipe_label.pack(side=tk.LEFT, padx=10)  
            recipe_label.config(font=("Helvetica", 12))  

            
            delete_button = tk.Button(
                recipe_frame, text="X", command=lambda name=recipe.name: self.delete_recipe(name), bg="#444444", fg="white")
            delete_button.pack(side=tk.RIGHT, padx=10)  
            delete_button.config(font=("Helvetica", 12))  
        #generated code ends
        
        back_button = tk.Button(self._frame, text="Back",
                                command=self._handle_home_page, bg="#444444", fg="white", font=("Helvetica", 14))  # Increase font size
        back_button.pack(side=tk.BOTTOM, pady=20)  # Add padding

    def delete_recipe(self, recipe_name):
        """
        Deletes the specified recipe.
        Args:
            recipe_name: The name of the recipe to delete.
        """
        recipe_app_service.delete_recipe(recipe_name)
        self._handle_refresh()


