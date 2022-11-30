from django.test import TestCase
from apps.users.models import User


class Hitman(TestCase):
    def register(self):
        response = self.client.post('/registro/',
                                    {
                                        'email': 'prueba@prueba.comm',
                                        "name":"prueba",
                                        "password":"password&/%&$",
                                        "description":"Es una prueba"
                                    })
        self.assertRedirects(response, '/login/')
        self.assertEqual(User.objects.filter(email="prueba@prueba.comm").count(), 1)
