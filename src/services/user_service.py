from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass


class InvalidCredentialsError(Exception):
    pass


class UserService:
    """Käyttäjien sovelluslogiikasta vastaava luokka.
    """

    def __init__(
        self,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori.

        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._user_repository = user_repository

    def get_users(self):
        """Etsii kaikki käyttäjät.

        Returns:
            User-oliota sisältävä lista käyttäjistä.
        """
        return self._user_repository.find_all()

    def create_user(self, username, password, admin):
        """Luo uuden käyttäjän.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            admin: Boolean arvo, joka kertoo onko käyttäjällä admin-rooli.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, jos käyttäjätunnus on jo käytössä.

        Returns:
            Palauttaa käyttäjän User-oliona.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password, admin))

        return user

    def login(self, username, password):
        """Kirjaa käyttäjän sisään sovellukseen.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
        Returns:
            Kirjaa käyttäjän sisään User-olion muodossa.
        Raises:
            InvalidCredentialsError:
                Virhe, jos käyttäjätunnus ja salasana eivät täsmää.
        """

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise InvalidCredentialsError("Invalid username or password")

        self._user = user

        return user

    def logout(self):
        """Kirjaa käyttäjän ulos järjestelmästä.
        """

        self._user = None

    def get_current_user(self):
        """Etsii sisään kirjautunen käyttäjän.

        Returns:
            Kirjautunut käyttäjä User-oliona.
        """

        return self._user

    def make_admin(self, username):
        """Antaa User-oliolle admin roolin.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
        """

        self._user_repository.make_admin(username)

    def is_admin(self, username):
        """Tarkistaa onko käyttäjällä admin-rooli.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.

        Returns:
            True: Jos käyttäjällä on admin-rooli.
            False: Jos käyttäjällä ei ole admin-roolia.
        """

        return self._user_repository.is_admin(username)


user_service = UserService()
