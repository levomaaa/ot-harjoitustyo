import unittest
from repositories.user_repository import user_repository
from entities.user import User


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_aapeli = User('Aapeli', '1234', False)
        self.user_admin = User('admin', '4321', False)

    def test_create(self):
        user_repository.create(self.user_aapeli)

        users = user_repository.find_all()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_aapeli.username)
        self.assertEqual(users[0].password, self.user_aapeli.password)
        self.assertEqual(users[0].admin, self.user_aapeli.admin)

    def test_create_when_admin(self):
        user_repository.create(self.user_admin)

        users = user_repository.find_all()

        self.assertEqual(users[0].admin, True)

    def test_find_by_username(self):
        user_repository.create(self.user_aapeli)

        user = user_repository.find_by_username(self.user_aapeli.username)

        self.assertEqual(user.username, self.user_aapeli.username)

    def test_is_admin_false(self):
        user_repository.create(self.user_aapeli)

        boolean_admin = user_repository.is_admin(self.user_aapeli.username)

        self.assertEqual(boolean_admin, False)

    def test_is_admin_true(self):
        user_repository.create(self.user_admin)

        boolean_admin = user_repository.is_admin(self.user_admin.username)

        self.assertEqual(boolean_admin, True)

    def test_is_admin_none(self):
        boolean_admin = user_repository.is_admin(self.user_admin.username)

        self.assertEqual(boolean_admin, False)

    def test_make_admin(self):
        user_repository.create(self.user_aapeli)

        user_repository.make_admin(self.user_aapeli.username)

        current_user = user_repository.find_by_username(
            self.user_aapeli.username)

        self.assertEqual(current_user.admin, True)
