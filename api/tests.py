from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Driver, Language, Truck, District, City


class LanguageTests(APITestCase):
    def test_create_language(self):
        """
        Ensure we can create a new driver.
        """
        url = reverse('language')
        data = {'name': 'French'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Language.objects.count(), 1)
        self.assertEqual(Language.objects.get().name, 'French')


class TruckTests(APITestCase):
    def test_create_truck(self):
        """
        Ensure we can create a new Truck.
        """
        url = reverse('truck')
        data = {'plateNumber': '200', 'registrationNumber': '400'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Truck.objects.count(), 1)
        self.assertEqual(Truck.objects.get().plateNumber, '200')
        self.assertEqual(Truck.objects.get().registrationNumber, '400')


class DriverTests(APITestCase):
    def test_create_driver(self):
        """
        Ensure we can create a new driver.
        """
        url = reverse('driver')
        Truck.objects.create(plateNumber='100', registrationNumber='500')
        Language.objects.create(name='Arabic')
        city = City.objects.create(name='Fes')
        District.objects.create(name='Narjis', city=city)
        data = {
            "name": "Youseef",
            "mobileNumber": "+212434243985",
            "email": "youssef@yemail.com",
            "city": 1,
            "district": 1,
            "aasignedTruck": 1,
            "created_at": "2023-03-16",
            "language": [1]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Driver.objects.count(), 1)
        self.assertEqual(Driver.objects.get().name, 'Youseef')
        self.assertEqual(Driver.objects.get().city.name, 'Fes')
        self.assertEqual(Driver.objects.get().district.name, 'Narjis')
        
