import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class LoginPage:
    """
    Class representing the login page.

    Args:
        root: The root Tkinter window.
        handle_login: The function to handle the login process.
        handle_register_page: The function to handle switching to the registration page.
    """

    def __init__(self, root, handle_login, handle_register_page):
        """
        Initializes a new LoginPage object.

        Args:
            root: The root Tkinter window.
            handle_login: The function to handle the login process.
            handle_register_page: The function to handle switching to the registration page.
        """
        self._root = root
        self._handle_login = handle_login
        self._handle_register_page = handle_register_page
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        """Packs the login frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the login frame."""
        self._frame.destroy()

    def login(self):
        """
        Attempts to log in with the provided username and password.
        Displays appropriate messages based on the success of the login attempt.
        """
        username = self._username_entry.get()
        password = self._password_entry.get()

        # Call the login method from RecipeAppService
        user = recipe_app_service.login(username, password)

        # Check if the login was successful
        if user:
            self._handle_login()
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def _initialize(self):
        """
        Initializes the login frame with username, password entries, and login/register buttons.
        """
        self._frame = tk.Frame(master=self._root)

        username_label = tk.Label(self._frame, text="Username:")
        username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        password_label = tk.Label(self._frame, text="Password:")
        password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._login_button = tk.Button(
            self._frame, text="Login", command=self.login)
        self._login_button.pack()

        self._register_button = tk.Button(
            self._frame, text="Register", command=self._handle_register_page)
        self._register_button.pack()
