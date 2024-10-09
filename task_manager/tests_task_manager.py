from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_view_url(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class LoginTest(TestCase):
    fixtures = ["users.json"]

    def test_view_url(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        credentials = {
            'username': 'tester1',
            'password': '123'
        }
        response = self.client.post(
            reverse('login'), credentials, follow=True)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertRedirects(response, reverse('home'))


class LogoutTest(TestCase):
    def test_view_url(self):
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)
