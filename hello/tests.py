from django.test import TestCase
from django.urls import reverse

class HelloViewTests(TestCase):
    def test_index_view_status_code(self):
        """
        Teszteli, hogy a 'hello.urls'-ben 'index'-nek nevezett
        főoldali nézet 200-as (OK) státuszkódot ad-e vissza.
        """
        url = reverse('index') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)