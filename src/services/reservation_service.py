from entities.reservation import Reservation
from repositories.reservation_repository import (
    reservation_repository as default_reservation_repository
)


class ReservationService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(
        self,
        reservation_repository=default_reservation_repository
    ):
        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            reservation_repository:
                Vapaaehtoinen, oletusarvoltaan ReservationRepository-olio.
                Olio, jolla on ReservationRepository-luokkaa vastaavat metodit.
        """
        self._reservation_repository = reservation_repository

    def create_reservation(self, username, date, hour):
        """Luo uuden ajanvarauksen.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            date: Merkkijonoarvo, joka kuvastaa päivämäärää.
            hour: Numero, joka kuvastaa ajanvarauksen alkavaa tuntia.

        Returns:
            Luo ajanvarauksen Reservation-olion muodossa.
        """

        reservation = self._reservation_repository.create_reservation(Reservation(username, date, hour))

        return reservation
    
    def reservation_user(self, date, hour):
        """Etsii ajanvarauksen tehneen käyttäjän nimen.

        Args:
            date: Merkkijonoarvo, joka kuvastaa päivämäärää.
            hour: Numero, joka kuvastaa ajanvarauksen alkavaa tuntia.

        Returns:
            Palauttaa ajanvarauksen tehneen käyttäjän nimen.
        """
        username = ""
        reservation = self._reservation_repository.find_username(Reservation(username, date, hour))
        
        return reservation
    
    def get_reservations(self):
        """Palauttaa listan kaikista ajanvarauksista.

        Returns:
            Reservation-oliota sisältävä lista ajanvarauksista.
        """
        return self._reservation_repository.find_all()
    
reservation_service = ReservationService()
