from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    return User(row["username"], row["password"]) if row else None


class UserRepository:
    """Luokka vastaa käyttäjiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden connection-olio
        """

        self._connection = connection

    def create(self, user):
        """Luo käyttäjän tietokantaan.

        Args:
            user: Luotava käyttäjä User-oliona.

        Returns:
            Tallennettu käyttäjä User-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into users (username, password) values (?, ?)",
            (user.username, user.password)
        )

        self._connection.commit()

        return user

    def delete_all(self):
        """Poistaa kaikki käyttäjät tietokannasta.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from users")

        self._connection.commit()

    def find_all(self):
        """Palauttaa kaikki käyttäjät listana.

        Returns:
            Palauttaa listan kaikista User-olioista.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from users")

        rows = cursor.fetchall()

        return list(map(get_user_by_row, rows))


user_repository = UserRepository(get_database_connection())
