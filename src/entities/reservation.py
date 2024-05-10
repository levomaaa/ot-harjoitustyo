class Reservation:
    """Luokka kuvaa yksittäistä ajanvarausta.

    Attributes:
        username: Käyttäjätunnus merkkijonoarvona, joka kuvaa ajanvarauksen tekijää.
        date: Päivämäärä merkkijonoarvona, joka kuvaa päivämäärää, johon ajanvaraus tehdään.
        hour: Alkava tunti numerona, joka kuvaa luotavan ajanvarauksen alkavaa tuntia.
    """

    def __init__(self, username, date, hour):
        """Luokan konstruktori, joka luo uuden ajanvarauksen kalenteriin.

        Args:
            username: Käyttäjätunnus merkkijonoarvona, joka kuvaa ajanvarauksen tekijää.
            date: Päivämäärä merkkijonoarvona, joka kuvaa päivämäärää, johon ajanvaraus tehdään.
            hour: Alkava tunti numerona, joka kuvaa luotavan ajanvarauksen alkavaa tuntia.
        """

        self.username = username
        self.date = date
        self.hour = hour
