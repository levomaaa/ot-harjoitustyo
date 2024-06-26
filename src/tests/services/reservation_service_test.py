import unittest
from entities.reservation import Reservation
from services.reservation_service import ReservationService


class FakeReservationRepository:
    def __init__(self, reservations=None):
        self.reservations = reservations or []

    def create_reservation(self, reservation):
        self.reservations.append(reservation)

        return reservation

    def find_all(self):
        return self.reservations

    def find_username(self, reservation_obj):
        filter_reservations = filter(
            lambda reservation: reservation.hour == reservation_obj.hour and reservation.date == reservation_obj.date,
            self.reservations
        )
        filtered_list = list(filter_reservations)
        if len(filtered_list) > 0:
            return filtered_list[0].username
        else:
            return None

    def cancel_reservation(self, date, hour):
        reservations = filter(
            lambda reservation: reservation.date != date or reservation.hour != hour,
            self.reservations
        )

        self.reservations = list(reservations)

    def check_reservation(self, username, date):
        reservations = filter(
            lambda reservation: reservation.username == username or reservation.date == date,
            self.reservations
        )

        if len(list(reservations)) != 0:
            return True

        return False


class TestReservationService(unittest.TestCase):
    def setUp(self):
        self.reservation_service = ReservationService(
            FakeReservationRepository())
        self.reservation = Reservation('Aapeli', '2040-10-11', 12)

    def test_reservation_user(self):
        username = self.reservation.username
        date = self.reservation.date
        hour = self.reservation.hour

        self.reservation_service.create_reservation(username, date, hour)

        reservations = self.reservation_service.get_reservations()

        returned_username = self.reservation_service.reservation_user(
            date, hour)

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].username, returned_username)

    def test_cancel_reservation(self):
        username = self.reservation.username
        date = self.reservation.date
        hour = self.reservation.hour

        self.reservation_service.create_reservation(username, date, hour)

        self.reservation_service.cancel_reservation(date, hour)

        reservations = self.reservation_service.get_reservations()

        self.assertEqual(len(reservations), 0)

    def test_check_reservation(self):
        username = self.reservation.username
        date = self.reservation.date
        hour = self.reservation.hour

        self.reservation_service.create_reservation(username, date, hour)

        checked_reservation = self.reservation_service.check_reservation(
            username, date)

        self.assertEqual(checked_reservation, True)
