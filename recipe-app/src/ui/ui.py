import tkinter as tk
from ui.login_page import LoginPage
from ui.register_page import RegistrationPage


class UI:

    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_login_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

    def _show_login_view(self):
        self._hide_current_view()

        self._current_view = LoginPage(
            self._root,
            self._show_login_view,
            self._show_create_user_view
        )

        self._current_view.pack()

    def _show_create_user_view(self):
        self._hide_current_view()

        self._current_view = RegistrationPage(
            self._root,
            self._redirect_to_login,  # Pass the registration handler here
            self._show_login_view
        )

        self._current_view.pack()

    def _redirect_to_login(self):
        self._show_login_view()  # Show login page after successful registration


if __name__ == "__main__":
    root = tk.Tk()
    ui = UI(root)
    ui.start()
    root.mainloop()
