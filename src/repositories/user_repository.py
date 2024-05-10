from entities.user import User
from database_connection import get_database_connection


def get_user_by_row(row):
    """ Etsii käyttäjän annetun rivin tiedoilla.

    Args:
        row: Tietokantaoperaation palauttama rivi tietoa.

    Returns: 
        Rivin tiedot User-oliona.
    """
    return User(row["username"], row["password"], row["admin"]) if row else None


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
        if user.username == "admin":
            cursor.execute(
                "insert into users (username, password, admin) values (?, ?, True)",
                (user.username, user.password)
            )
        else:
            cursor.execute(
                "insert into users (username, password, admin) values (?, ?, False)",
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

    def find_by_username(self, username):
        """Palauttaa käyttäjän käyttäjätunnuksen perusteella tietokannasta.

        Args:
            username: Käyttäjätunnus, jonka perusteella käyttäjä palautetaan.

        Returns:
            Palauttaa User-olion, jos käyttäjätunnuksen omistava käyttäjä on tietokannassa.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select * from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()

        return get_user_by_row(row)

    def is_admin(self, username):
        """Tarkistaa tietokannasta, onko käyttäjällä admin-rooli.

        Args:
            username: Käyttäjätunnus, jonka rooli tarkastetaan.

        Returns:
            True: Jos käyttäjällä on admin-rooli.
            False: Jos käyttäjällä ei ole admin-roolia.
        """
        cursor = self._connection.cursor()

        cursor.execute(
            "select admin from users where username = ?",
            (username,)
        )

        row = cursor.fetchone()
        if row is not None:
            return bool(row[0])

        return False

    def make_admin(self, username):
        """Antaa käyttäjälle tietokantaan admin-roolin.

        Args:
            username: Käyttäjätunnus, jonka perusteella käyttäjälle annetaan admin-rooli.
        """

        cursor = self._connection.cursor()

        cursor.execute("update users set admin = True where username = ?",
                       (username,)
                       )

        self._connection.commit()


user_repository = UserRepository(get_database_connection())
