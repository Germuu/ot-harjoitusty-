import tkinter as tk
from tkinter import messagebox
from services.recipe_app_service import RecipeAppService

#Generated code begins
class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Recipe App Login")

        self.recipe_service = RecipeAppService()

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack()

        self.register_button = tk.Button(root, text="Register", command=self.open_registration)
        self.register_button.pack()
#Generated code ends

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Call the login method from RecipeAppService
        user = self.recipe_service.login(username, password)

        # Check if the login was successful
        if user:
            messagebox.showinfo("Login", "Login successful")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

    def open_registration(self):
        # Create a new window for registration
        registration_window = tk.Toplevel(self.root)
        registration_window.title("Recipe App Registration")

        # Create registration page UI
        registration_page = RegistrationPage(registration_window, self.recipe_service)

class RegistrationPage:
    def __init__(self, root, recipe_service):
        self.root = root
        self.recipe_service = recipe_service

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(root)
        self.username_entry.pack()

        self.password_label = tk.Label(root, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()

        self.register_button = tk.Button(root, text="Register", command=self.register)
        self.register_button.pack()

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Call the register_user method from RecipeAppService
        try:
            new_user = self.recipe_service.register_user(username, password)
            messagebox.showinfo("Registration", "Registration successful")
        except UsernameTakenError as e:
            messagebox.showerror("Registration Error", str(e))

# Create main Tkinter window
root = tk.Tk()
app = LoginPage(root)

# Run the Tkinter event loop
root.mainloop()
