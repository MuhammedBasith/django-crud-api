from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Drink

class DrinkTests(APITestCase):

    def setUp(self):
        self.drink = Drink.objects.create(name="Coca Cola", description="A refreshing soft drink")

    def test_get_drinks(self):
        url = reverse('drink_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()['drinks']), 1)

    def test_create_drink(self):
        url = reverse('drink_list')
        data = {'name': 'Pepsi', 'description': 'Another refreshing soft drink'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Drink.objects.count(), 2)
        self.assertEqual(Drink.objects.get(id=2).name, 'Pepsi')

    def test_update_drink(self):
        url = reverse('drink_detail', args=[self.drink.id])
        data = {'name': 'Fanta', 'description': 'A citrus-flavored soft drink'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.drink.refresh_from_db()
        self.assertEqual(self.drink.name, 'Fanta')

    def test_delete_drink(self):
        url = reverse('drink_detail', args=[self.drink.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Drink.objects.count(), 0)
