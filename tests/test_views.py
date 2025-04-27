from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu, Booking
from decimal import Decimal
from django.utils import timezone

class MenuViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu_item = Menu.objects.create(
            title="Test Item",
            price=Decimal("10.99"),
            inventory=5
        )

    def test_getall(self):
        # Get all menu items
        url = reverse('menu-items')
        response = self.client.get(url)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        # Check if the serialized data is correct
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.menu_item.title)
        self.assertEqual(Decimal(response.data[0]['price']), self.menu_item.price)
        self.assertEqual(response.data[0]['inventory'], self.menu_item.inventory)