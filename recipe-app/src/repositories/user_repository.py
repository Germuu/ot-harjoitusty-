import hashlib
from entities.user import User
from database_connection import get_database_connection


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def add_user(self, user):
        hashed_password = hashlib.sha256(user.password.encode()).hexdigest()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        self._connection.execute(query, (user.username, hashed_password))
        self._connection.commit()
        return user

    def retrieve_all(self):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users")
        rows = cursor.fetchall()
        return [User(row["username"], row["password"]) for row in rows]

    def find_by_username(self, username):
        cursor = self._connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        row = cursor.fetchone()
        return User(row["username"], row["password"]) if row else None

    def clear(self):
        query = "DELETE FROM users"
        self._connection.execute(query)
        self._connection.commit()
       


user_repository = UserRepository(get_database_connection())

