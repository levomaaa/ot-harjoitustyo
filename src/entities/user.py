class User:
    """Luokka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: Käyttäjätunnus merkkijonoarvona.
        password: Salasana merkkijonoarvona.
    """

    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Käyttäjätunnus merkkijonoarvona.
            password: Salasana merkkijonoarvona.
        """

        self.username = username
        self.password = password
        