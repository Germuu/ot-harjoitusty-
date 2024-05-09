import tkinter as tk
from tkinter import ttk, messagebox
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
        self._frame.grid(row=0, column=0, sticky="nsew")
        self._root.grid_rowconfigure(0, weight=1)
        self._root.grid_columnconfigure(0, weight=1)

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

    def _validate_password(self):
        """
        Validates the password entry.
        Changes the style of the login button based on the length of the password.
        """
        password = self._password_entry.get()
        if len(password) >= 4:
            self._login_button.configure(style="Green.TButton")
        else:
            self._login_button.configure(style="Dark.TButton")

    def _initialize(self):
        """
        Initializes the login frame with username, password entries, and login/register buttons.
        """
        self._frame = tk.Frame(master=self._root)

        # Apply the theme to the frame
        self._frame["bg"] = "#1E1E1E"  # Background color

        username_label = tk.Label(
            self._frame, text="Username:", bg="#1E1E1E", fg="white")
        username_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self._username_entry = tk.Entry(self._frame)
        self._username_entry.grid(row=0, column=1, padx=10, pady=5)

        password_label = tk.Label(
            self._frame, text="Password:", bg="#1E1E1E", fg="white")
        password_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.grid(row=1, column=1, padx=10, pady=5)
        # Validate password entry when typing
        self._password_entry.bind(
            '<KeyRelease>', lambda event: self._validate_password())

        # Create a style for the login button
        self._root.style = ttk.Style()
        self._root.style.configure(
            "Green.TButton", foreground="black", background="green")

        self._login_button = ttk.Button(
            self._frame, text="Login", style="Dark.TButton", command=self.login)
        self._login_button.grid(row=2, column=0, columnspan=2, pady=10)

        register_button = ttk.Button(
            self._frame, text="Register", style="Dark.TButton", command=self._handle_register_page)
        register_button.grid(row=3, column=0, columnspan=2, pady=5)
