import unittest
from repositories.reservation_repository import reservation_repository
from entities.reservation import Reservation


class TestReservationRepository(unittest.TestCase):
    def setUp(self):
        reservation_repository.delete_all()
        self.reservation = Reservation('Aapeli', '2024-05-01', 7)

    def test_create_reservation(self):
        reservation_repository.create_reservation(self.reservation)

        reservations = reservation_repository.find_all()

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].username, self.reservation.username)
        self.assertEqual(reservations[0].date, self.reservation.date)
        self.assertEqual(reservations[0].hour, self.reservation.hour)

    def test_find_username_if_exists(self):
        reservation_repository.create_reservation(self.reservation)

        username = reservation_repository.find_username(self.reservation)

        reservations = reservation_repository.find_all()

        self.assertEqual(username, reservations[0].username)

    def test_find_username_if_not_exist(self):
        username = reservation_repository.find_username(self.reservation)

        self.assertEqual(username, None)

    def test_cancel_reservation(self):
        reservation_repository.create_reservation(self.reservation)

        reservation_repository.cancel_reservation(
            self.reservation.date, self.reservation.hour)

        reservations = reservation_repository.find_all()

        self.assertEqual(len(reservations), 0)

    def test_check_reservation_not_none(self):
        reservation_repository.create_reservation(self.reservation)

        checked_reservation = reservation_repository.check_reservation(
            self.reservation.username, self.reservation.date)

        self.assertEqual(checked_reservation, True)

    def test_check_reservation_none(self):
        checked_reservation = reservation_repository.check_reservation(
            self.reservation.username, self.reservation.date)

        self.assertEqual(checked_reservation, False)
