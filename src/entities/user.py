class User:
    """Luokka kuvaa yksittäistä käyttäjää.

    Attributes:
        username: Käyttäjätunnus merkkijonoarvona.
        password: Salasana merkkijonoarvona.
    """

    def __init__(self, username, password, admin):
        """Luokan konstruktori, joka luo uuden käyttäjän.

        Args:
            username: Käyttäjätunnus merkkijonoarvona.
            password: Salasana merkkijonoarvona.
            admin: Admin-rooli boolean arvona.
        """

        self.username = username
        self.password = password
        self.admin = admin

        if username == "admin":
            self.admin = True
