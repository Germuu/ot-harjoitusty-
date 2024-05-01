import hashlib
from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    """
    Repository for interacting with the users table in the database.

    Args:
        connection: Database connection object.
    """

    def __init__(self, connection):
        """
        Initializes a new UserRepository object.

        Args:
            connection: Database connection object.
        """
        self._connection = connection

    def add_user(self, user):
        """
        Add a new user to the users table.

        Args:
            user (User): The user object to be added.

        Returns:
            User: The added user object.
        """
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self._connection.execute(query, (user.username, hashed_password))
        self._connection.commit()
        return user

    def retrieve_all(self):
        """
        Retrieve all users from the users table.

        Returns:
            list: A list of User objects representing all users in the database.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        """
        Retrieve a user from the users table by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User or None: The User object representing the found user, or None if not found.
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def clear(self):
        """
        Delete all users from the users table.
        """
        query = "DELETE FROM users"
        self._connection.execute(query)
        self._connection.commit()


user_repository = UserRepository(get_database_connection())
