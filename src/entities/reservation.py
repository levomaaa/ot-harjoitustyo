class Reservation:
    """Luokka kuvaa yksittäistä ajanvarausta.

    Attributes:
        username: Käyttäjätunnus merkkijonoarvona.
        date: Päivämäärä merkkijonoarvona.
        hour: Alkava tunti numerona.
    """

    def __init__(self, username, date, hour):
        """Luokan konstruktori, joka luo uuden ajanvarauksen kalenteriin.

        Args:
            username: Käyttäjätunnus merkkijonoarvona.
            date: Päivämäärä merkkijonoarvona.
            hour: Alkava tunti numerona.
        """

        self.username = username
        self.date = date
        self.hour = hour
