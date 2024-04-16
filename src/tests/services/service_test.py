import unittest
from entities.user import User
from services.service import UsernameExistsError, Service

class FakeUserRepository:
    def __init__(self, users=None):
        self.users = users or []

    def create(self, user):
        self.users.append(user)
        return user

    def find_all(self):
        return self.users
    
    def find_by_username(self, username):
        filter_users = filter(
            lambda user: user.username == username,
            self.users
        )
        filtered_list = list(filter_users)
        if len(filtered_list) > 0:
            return filtered_list[0] 
        else:
            return None


class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service(FakeUserRepository())
        self.user_aapeli = User('Aapeli', '1234')

    def test_create_user(self):
        username = self.user_aapeli.username
        password = self.user_aapeli.password
        self.service.create_user(username, password)
        users = self.service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_aapeli.username
        password = self.user_aapeli.password

        self.service.create_user(username, password)

        self.assertRaises(
            UsernameExistsError,
            lambda: self.service.create_user(username, '1234')
        )