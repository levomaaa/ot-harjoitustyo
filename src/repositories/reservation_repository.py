from database_connection import get_database_connection
from entities.reservation import Reservation

def get_reservation_by_row(row):
    return Reservation(row["username"], row["date"], row["hour"]) if row else None


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
    
    def find_username(self, reservation):
        
        
        cursor = self._connection.cursor()

        cursor.execute(
            "select username from reservations where date = ? and hour = ?",
            (reservation.date, reservation.hour)
        )

        row = cursor.fetchone()
        if row is None:
            return None
        else:
            username = row["username"]
            return username
    
    def delete_all(self):
        """Poistaa kaikki ajanvaraukset tietokannasta.
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from reservations")

        self._connection.commit()

    def find_all(self):
        """Palauttaa kaikki ajanvaraukset listana.

        Returns:
            Palauttaa listan kaikista Reservation-olioista.
        """

        cursor = self._connection.cursor()

        cursor.execute("select * from reservations")

        rows = cursor.fetchall()

        return list(map(get_reservation_by_row, rows))
    
reservation_repository = ReservationRepository(get_database_connection())
