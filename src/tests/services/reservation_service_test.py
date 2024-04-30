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

    

class TestReservationService(unittest.TestCase):
    def setUp(self):
        self.reservation_service = ReservationService(FakeReservationRepository())
        self.reservation = Reservation('Aapeli', '2040-10-11', 12)

    def test_reservation_user(self):
        username = 'Ilari'
        date = '2020-10-11'
        hour = 10
        self.reservation_service.create_reservation(username, date, hour)

        reservations = self.reservation_service.get_reservations()
        returned_username = self.reservation_service.reservation_user(date, hour)

        self.assertEqual(len(reservations), 1)
        self.assertEqual(reservations[0].username, returned_username)
