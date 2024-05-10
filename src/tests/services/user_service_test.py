import unittest
from entities.user import User
from services.user_service import UsernameExistsError, UserService, InvalidCredentialsError


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
    
    def make_admin(self,username):
        user = self.find_by_username(username)
        user.admin = True

    def is_admin(self,username):
        user = self.find_by_username(username)
        return user.admin



class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(FakeUserRepository())
        self.user_aapeli = User('Aapeli', '1234', False)

    def login_user(self, user):
        self.user_service.create_user(user.username, user.password, user.admin)
        self.user_service.login(user.username, user.password)

    def test_create_user(self):
        username = self.user_aapeli.username
        password = self.user_aapeli.password
        admin = self.user_aapeli.admin

        self.user_service.create_user(username, password, admin)
        users = self.user_service.get_users()

        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, username)

    def test_create_user_with_existing_username(self):
        username = self.user_aapeli.username
        password = self.user_aapeli.password
        admin = self.user_aapeli.admin

        self.user_service.create_user(username, password, admin)

        self.assertRaises(
            UsernameExistsError,
            lambda: self.user_service.create_user(username, password, admin)
        )

    def test_login_with_valid_credentials(self):
        self.user_service.create_user(
            self.user_aapeli.username,
            self.user_aapeli.password,
            self.user_aapeli.admin
        )

        user = self.user_service.login(
            self.user_aapeli.username,
            self.user_aapeli.password
        )

        self.assertEqual(user.username, self.user_aapeli.username)

    def test_login_with_invalid_credentials(self):
        self.assertRaises(
            InvalidCredentialsError,
            lambda: self.user_service.login('Messi', '#10')
        )

    def test_logout(self):
        self.login_user(self.user_aapeli)

        self.user_service.logout()

        self.assertEqual(self.user_service._user, None)

    def test_get_current_user(self):
        self.login_user(self.user_aapeli)

        current_user = self.user_service.get_current_user()

        self.assertEqual(current_user.username, self.user_aapeli.username)

    def test_make_admin(self):
        self.user_service.create_user(
            self.user_aapeli.username,
            self.user_aapeli.password,
            self.user_aapeli.admin
        )

        self.user_service.make_admin(self.user_aapeli.username)

        current_user = self.user_service.get_users()

        self.assertEqual(current_user[0].admin, True)

    def test_is_admin_false(self): 
        self.user_service.create_user(
            self.user_aapeli.username,
            self.user_aapeli.password,
            self.user_aapeli.admin
        )
        
        boolean = self.user_service.is_admin(self.user_aapeli.username)

        self.assertEqual(boolean, False)
    
    def test_is_admin_true(self): 
        self.user_service.create_user(
            self.user_aapeli.username,
            self.user_aapeli.password,
            self.user_aapeli.admin
        )
        
        self.user_service.make_admin(self.user_aapeli.username)
        
        boolean = self.user_service.is_admin(self.user_aapeli.username)

        self.assertEqual(boolean, True)
