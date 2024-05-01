class User:
    """
    Represents a user with a username and password.

    Attributes:
        username (str): The username of the user.
        password (str): The password of the user.
    """

    def __init__(self, username, password):
        """
        Initializes a new User object.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self.username = username
        self.password = password
