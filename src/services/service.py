from entities.user import User

from repositories.user_repository import (
    user_repository as default_user_repository
)


class UsernameExistsError(Exception):
    pass

class InvalidCredentialsError(Exception):
    pass


class Service:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(
        self,
        user_repository=default_user_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            user_repository:
                Vapaaehtoinen, oletusarvoltaan UserRepository-olio.
                Olio, jolla on UserRepository-luokkaa vastaavat metodit.
        """
        self._user = None
        self._user_repository = user_repository

    def get_users(self):
        """Palauttaa listan kaikista käyttäjistä.

        Returns:
            User-oliota sisältä lista käyttäjistä.
        """
        return self._user_repository.find_all()

    def create_user(self, username, password, login=True):
        """Luo uuden käyttäjän ja kirjaa sen sisään.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvastaa käyttäjän salasanaa.
            login:
                Oletusarvo True.
                Boolean-arvo, joka kertoo kirjataanko käyttäjä sisään onnistuneen luonnin jälkeen.

        Raises:
            UsernameExistsError: Virhe, joka tapahtuu, jos käyttäjätunnus on jo käytössä.

        Returns:
            Luo käyttäjän User-olion muodossa.
        """

        existing_user = self._user_repository.find_by_username(username)

        if existing_user:
            raise UsernameExistsError(f"Username {username} already exists")

        user = self._user_repository.create(User(username, password))

        if login:
            self._user = user

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


service = Service()
