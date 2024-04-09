import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.clear()
        self.test_user1 = User("admin", "1234")
        self.test_user2 = User("Joe",   "4321")
    
    def test_adding(self):
        user_repository.add_user(self.test_user1)
        all_users = user_repository.retrieve_all()

        self.assertEqual(all_users[0].username, "admin")





