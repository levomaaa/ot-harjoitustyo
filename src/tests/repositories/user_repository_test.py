import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_aapeli = User('Aapeli', '1234')

    def test_create(self):
        user_repository.create(self.user_aapeli)
        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_aapeli.username)
        self.assertEqual(users[0].password, self.user_aapeli.password)