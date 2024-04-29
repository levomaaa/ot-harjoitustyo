from database_connection import get_database_connection



class ReservationRepository:
    """Luokka vastaa ajanvarauksiin liittyvistä tietokantaoperaatioista.
    """

    def __init__(self, connection):
        """Luokan konstruktori.

        Args:
            connection: Tietokantayhteyden connection-olio
        """

        self._connection = connection
    
    def create_reservation(self, reservation):
        """Luo ajanvarauksen tietokantaan.

        Args:
            reservation: Luotava ajanvaraus Reservation-oliona.

        Returns:
            Tallennettu ajanvaraus Reservation-oliona.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "insert into reservations (username, date, hour) values (?, ?, ?)",
            (reservation.username, reservation.date, reservation.hour)
        )

        self._connection.commit()

        return reservation
    
reservation_repository = ReservationRepository(get_database_connection())
