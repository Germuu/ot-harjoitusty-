import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class LoginPage:
    def __init__(self, root, handle_login, handle_register_page):
        self._root = root
        self._handle_login = handle_login
        self._handle_register_page = handle_register_page
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def login(self):
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

# Generated code begins
    def _initialize(self):
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
# Generated code ends
