import tkinter as tk
from tkinter import messagebox, constants
from services.recipe_app_service import recipe_app_service


class RegistrationPage:
    def __init__(self, root,  handle_register):
        self._root = root
        self._handle_register = handle_register
        self._frame = None
        self._username_entry = None
        self._password_entry = None

        self.initialize()

    def pack(self):
        self.frame.pack(fill=constants.X)

    def destroy(self):
        self.frame.destroy()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()


        try:
            recipe_app_service.register_user(username, password)
            messagebox.showinfo("Registration", "Registration successful")
            self._handle_register()
        except:
            print(recipe_app_service.register_user(username, password))
            messagebox.showerror("Registration Error", "Username taken")

    def initialize(self):
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
