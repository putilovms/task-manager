from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist


class UsersPageTest(TestCase):
    def test_view_url(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)


class RegistrationPageTest(TestCase):
    def test_view_url(self):
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('user_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        credentials = {
            "username": "tester3",
            "first_name": "Пётр",
            "last_name": "Петров",
            'password1': '123',
            'password2': '123',
        }
        response = self.client.post(
            reverse('user_create'), credentials, follow=True)
        self.assertRedirects(response, reverse('login'))
        user = User.objects.get(username='tester3')
        self.assertEqual(str(user), 'tester3')


class EditPageTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/users/1/update/')
        self.assertEqual(response.status_code, 200)
        url = reverse('user_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_perm(self):
        response = self.client.get('/users/2/update/')
        self.assertEqual(response.status_code, 302)
        url = reverse('user_update', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update(self):
        credentials = {
            "username": "tester4",
            "first_name": "Егор",
            "last_name": "Егоров",
            'password1': '123',
            'password2': '123',
        }
        url = reverse('user_update', kwargs={'pk': 1})
        response = self.client.post(url, credentials, follow=True)
        self.assertRedirects(response, reverse('users'))
        user = User.objects.get(id=1)
        self.assertEqual(str(user), 'tester4')
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username='tester1')


class DeletePageTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/users/1/delete/')
        self.assertEqual(response.status_code, 200)
        url = reverse('user_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_perm(self):
        url = reverse('user_delete', kwargs={'pk': 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_used_user_not_delete(self):
        url = reverse('user_delete', kwargs={'pk': 1})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('users'))
        status = User.objects.get(id=1)
        self.assertEqual(str(status), 'tester1')

    def test_delete(self):
        self.client.logout()
        self.client.login(username='tester3', password='123')
        url = reverse('user_delete', kwargs={'pk': 3})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('users'))
        with self.assertRaises(ObjectDoesNotExist):
            User.objects.get(username='tester3')
