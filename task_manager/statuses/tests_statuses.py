from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse
from task_manager.statuses.models import Statuses


class StatusesPageTest(TestCase):
    fixtures = ["users.json"]

    def test_view_url(self):
        self.client.login(username='tester1', password='123')
        response = self.client.get('/statuses/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        response = self.client.get(reverse('statuses'))
        self.assertRedirects(response, reverse('login'))


class CreateStatusPageTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/statuses/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('status_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('status_create'))
        self.assertRedirects(response, reverse('login'))

    def test_create_status(self):
        credentials = {
            "name": "status1",
        }
        response = self.client.post(
            reverse('status_create'), credentials, follow=True)
        self.assertRedirects(response, reverse('statuses'))
        status = Statuses.objects.get(name='status1')
        self.assertEqual(str(status), 'status1')


class EditStatusPageTest(TestCase):
    fixtures = ["users.json", "statuses.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/statuses/1/update/')
        self.assertEqual(response.status_code, 200)
        url = reverse('status_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('status_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_status_update(self):
        credentials = {
            "name": "status4"
        }
        url = reverse('status_update', kwargs={'pk': 1})
        response = self.client.post(url, credentials, follow=True)
        self.assertRedirects(response, reverse('statuses'))
        status = Statuses.objects.get(id=1)
        self.assertEqual(str(status), 'status4')
        with self.assertRaises(ObjectDoesNotExist):
            Statuses.objects.get(name='status1')


class DeleteStatusPageTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/statuses/1/delete/')
        self.assertEqual(response.status_code, 200)
        url = reverse('status_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('status_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_used_status_not_deleted(self):
        url = reverse('status_delete', kwargs={'pk': 1})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('statuses'))
        status = Statuses.objects.get(id=1)
        self.assertEqual(str(status), 'status1')

    def test_status_delete(self):
        url = reverse('status_delete', kwargs={'pk': 3})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('statuses'))
        with self.assertRaises(ObjectDoesNotExist):
            Statuses.objects.get(id=3)
