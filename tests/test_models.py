from django.test import TestCase
from restaurant.models import Menu, Booking
from decimal import Decimal
from django.utils import timezone

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")

class BookingTests(TestCase):
    def test_create_booking(self):
        booking = Booking.objects.create(
            name="Test User",
            no_of_guests=4,
            booking_date=timezone.now()
        )
        self.assertEqual(booking.name, "Test User")
        self.assertEqual(booking.no_of_guests, 4) 