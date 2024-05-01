import tkinter as tk
from ui.login_page import LoginPage
from ui.register_page import RegistrationPage
from ui.home_page import HomePage
from ui.my_recipes_page import MyRecipesPage
from ui.add_recipe_page import AddRecipePage
from ui.edit_recipe_page import EditRecipe
from ui.find_recipes_page import FindRecipesPage
from ui.search_results_page import SearchResultsPage
from ui.recipe_details_page import RecipeDetailsPage


class UI:
    """
    Class representing the main user interface.

    Args:
        root: The root Tkinter window.
    """

    def __init__(self, root):
        """
        Initializes a new UI object.

        Args:
            root: The root Tkinter window.
        """
        self._root = root
        self._current_view = None

    def start(self):
        """Starts the user interface by displaying the login view."""
        self._show_login_view()

    def _hide_current_view(self):
        """Hides the current view."""
        if self._current_view:
            self._current_view.destroy()

    def _show_login_view(self):
        """Displays the login view."""
        self._hide_current_view()
        self._current_view = LoginPage(
            self._root,
            self._show_home_view,
            self._show_create_user_view,
        )
        self._current_view.pack()

    def _show_create_user_view(self):
        """Displays the user registration view."""
        self._hide_current_view()
        self._current_view = RegistrationPage(
            self._root,
            self._show_login_view  # Pass the registration handler here
        )
        self._current_view.pack()

    def _show_home_view(self):
        """Displays the home view."""
        self._hide_current_view()
        self._current_view = HomePage(
            self._root,
            self._show_my_recipes_view,
            self._show_find_recipes_view,
            self._show_login_view
        )
        self._current_view.pack()

    def _show_my_recipes_view(self):
        """Displays the 'My Recipes' view."""
        self._hide_current_view()
        self._current_view = MyRecipesPage(
            self._root,
            self._show_add_recipe_view,
            self._show_edit_recipe_view,
            self._show_home_view,
            self._show_my_recipes_view
        )
        self._current_view.pack()

    def _show_add_recipe_view(self):
        """Displays the 'Add Recipe' view."""
        self._hide_current_view()
        self._current_view = AddRecipePage(
            self._root,
            self._show_my_recipes_view
        )
        self._current_view.pack()

    def _show_find_recipes_view(self):
        """Displays the 'Find Recipes' view."""
        self._hide_current_view()
        self._current_view = FindRecipesPage(
            self._root,
            self._show_results_view,
            self._show_home_view
        )
        self._current_view.pack()

    def _show_results_view(self, results):
        """Displays the search results view."""
        self._hide_current_view()
        self._current_view = SearchResultsPage(
            self._root,
            results,
            self._show_recipe_details_view
        )
        self._current_view.pack()

    def _show_recipe_details_view(self, recipe):
        """Displays the recipe details view."""
        self._hide_current_view()
        self._current_view = RecipeDetailsPage(
            self._root,
            recipe,
            self._show_find_recipes_view  # Pass the function to go back to search results
        )
        self._current_view.pack()

    def _show_edit_recipe_view(self, recipe):
        """Displays the 'Edit Recipe' view."""
        self._hide_current_view()
        self._current_view = EditRecipe(
            self._root,
            self._show_my_recipes_view,
            recipe
        )
        self._current_view.pack()


if __name__ == "__main__":
    root = tk.Tk()
    ui = UI(root)
    ui.start()
    root.mainloop()
