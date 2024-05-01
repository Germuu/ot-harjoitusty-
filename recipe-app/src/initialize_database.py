from database_connection import get_database_connection

def drop_tables(connection):
    """
    Delete database tables

    Args:
        connection: Database connection object.
    """
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS recipes;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS users;
    ''')

    connection.commit()


def create_tables(connection):
    """
    Create tables in the database 

    Args:
        connection: Database connection object.
    """
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            cooking_time INTEGER NOT NULL,
            ingredients TEXT NOT NULL,
            username TEXT,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')

    connection.commit()


def initialize_database():
    """
    Initialize the database by dropping existing tables and creating new ones.
    """
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)


if __name__ == "__main__":
    initialize_database()
