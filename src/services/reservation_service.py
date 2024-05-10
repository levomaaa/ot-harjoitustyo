from entities.reservation import Reservation
from repositories.reservation_repository import (
    reservation_repository as default_reservation_repository
)


class ReservationService:
    """Ajanvarausten sovelluslogiikasta vastaava luokka.
    """

    def __init__(
        self,
        reservation_repository=default_reservation_repository
    ):
        """Luokan konstruktori.

        Args:
            reservation_repository:
                Vapaaehtoinen, oletusarvoltaan ReservationRepository-olio.
                Olio, jolla on ReservationRepository-luokkaa vastaavat metodit.
        """

        self._reservation_repository = reservation_repository

    def create_reservation(self, username, date, hour):
        """Luo uuden ajanvarauksen.

        Args:
            username: Merkkijonoarvo, joka kuvastaa ajanvarauksen luovan käyttäjän käyttäjätunnusta.
            date: Merkkijonoarvo, joka kuvastaa päivämäärää, johon ajanvaraus luodaan.
            hour: Alkava tunti numerona, joka kuvaa luotavan ajanvarauksen alkavaa tuntia.

        Returns:
            Palauttaa ajanvarauksen Reservation-olion muodossa.
        """

        reservation = self._reservation_repository.create_reservation(
            Reservation(username, date, hour))

        return reservation

    def cancel_reservation(self, date, hour):
        """Peruuttaa ajanvarauksen.

        Args:
            date: Merkkijonoarvo, joka kuvastaa päivämäärää.
            hour: Numero, joka kuvastaa ajanvarauksen alkavaa tuntia.
        """

        self._reservation_repository.cancel_reservation(date, hour)

    def check_reservation(self, username, date):
        """Etsii onko käyttäjä jo tehnyt ajanvarauksen kyseiselle päivälle.

        Args:
            username: Merkkijonoarvo, joka kuvastaa käyttäjän käyttäjätunnusta.
            date: Merkkijonoarvo, joka kuvastaa päivämäärää.

        Returns:
            True: Jos käyttäjä on jo tehnyt ajanvarauksen kyseiselle päivälle.
            False: Jos käyttäjä ei ole tehnyt kyseiselle päivälle ajanvarausta.
        """
        return self._reservation_repository.check_reservation(username, date)

    def reservation_user(self, date, hour):
        """Etsii ajanvarauksen tehneen käyttäjän käyttäjänimen.

        Args:
            date: Merkkijonoarvo, joka kuvastaa päivämäärää.
            hour: Numero, joka kuvastaa ajanvarauksen alkavaa tuntia.

        Returns:
            Palauttaa ajanvarauksen tehneen käyttäjän käyttäjänimen.
        """
        username = ""
        reservation_username = self._reservation_repository.find_username(
            Reservation(username, date, hour))

        return reservation_username

    def get_reservations(self):
        """Etsii kaikki ajanvaraukset.

        Returns:
            Reservation-olioita sisältävä lista ajanvarauksista.
        """
        return self._reservation_repository.find_all()


reservation_service = ReservationService()
