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

    def __init__(self, root, handle_register):
        """
        Initializes a new RegistrationPage object.

        Args:
            root: The root Tkinter window.
            handle_register: The function to handle registration.
        """
        self._root = root
        self._handle_register = handle_register
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self.initialize()

    def pack(self):
        """Packs the registration frame into the root window."""
        self.frame.pack(fill=constants.X)

    def destroy(self):
        """Destroys the registration frame."""
        self.frame.destroy()

    def register(self):
        """Handles the registration process."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            recipe_app_service.register_user(username, password)
            messagebox.showinfo("Registration", "Registration successful")
            self._handle_register()
        except:
            messagebox.showerror("Registration Error", "Username taken")

    def initialize(self):
        """Initializes the registration frame."""
        self.frame = tk.Frame(master=self._root)

        self.username_label = tk.Label(self.frame, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.frame, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(
            self.frame, text="Register", command=self.register)
        self.register_button.pack()
