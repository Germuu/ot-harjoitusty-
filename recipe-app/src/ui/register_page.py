import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class RegistrationPage:
    """
    Class representing the registration page.

    Args:
        root: The root Tkinter window.
        handle_register: The function to handle registration.
    """

    def __init__(self, root, handle_register, handle_back):
        """
        Initializes a new RegistrationPage object.

        Args:
            root: The root Tkinter window.
            handle_register: The function to handle registration.
            handle_back: The function to handle going back to the previous page.
        """
        self._root = root
        self._handle_register = handle_register
        self._handle_back = handle_back
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self.initialize()

    def pack(self):
        """Packs the registration frame into the root window."""
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the registration frame."""
        self._frame.destroy()

    def register(self):
        """Handles the registration process."""
        username = self._username_entry.get()
        password = self._password_entry.get()

        try:
            recipe_app_service.register_user(username, password)
            messagebox.showinfo("Registration", "Registration successful")
            self._handle_register()
        except:
            messagebox.showerror("Registration Error", "Username taken")

    def initialize(self):
        """Initializes the registration frame."""
        self._frame = tk.Frame(master=self._root, bg="#1E1E1E")

        self._username_label = tk.Label(self._frame, text="Username:", bg="#1E1E1E", fg="white")
        self._username_label.pack()
        self._username_entry = tk.Entry(self._frame)
        self._username_entry.pack()

        self._password_label = tk.Label(self._frame, text="Password:", bg="#1E1E1E", fg="white")
        self._password_label.pack()
        self._password_entry = tk.Entry(self._frame, show="*")
        self._password_entry.pack()

        self._register_button = tk.Button(
            self._frame, text="Register", command=self.register, bg="#444444", fg="white")
        self._register_button.pack()

        self._back_button = tk.Button(
            self._frame, text="Back", command=self._handle_back, bg="#444444", fg="white")
        self._back_button.pack()
