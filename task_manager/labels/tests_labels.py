from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse
from task_manager.labels.models import Labels


class LabelsPageTest(TestCase):
    fixtures = ["users.json"]

    def test_view_url(self):
        self.client.login(username='tester1', password='123')
        response = self.client.get('/labels/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        response = self.client.get(reverse('labels'))
        self.assertRedirects(response, reverse('login'))


class CreateLabelPageTest(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/labels/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('label_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('label_create'))
        self.assertRedirects(response, reverse('login'))

    def test_create_label(self):
        credentials = {
            "name": "label1",
        }
        response = self.client.post(
            reverse('label_create'), credentials, follow=True)
        self.assertRedirects(response, reverse('labels'))
        label = Labels.objects.get(name='label1')
        self.assertEqual(str(label), 'label1')


class EditLabelPageTest(TestCase):
    fixtures = ["users.json", "labels.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/labels/1/update/')
        self.assertEqual(response.status_code, 200)
        url = reverse('label_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('label_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_label_update(self):
        credentials = {
            "name": "label3"
        }
        url = reverse('label_update', kwargs={'pk': 1})
        response = self.client.post(url, credentials, follow=True)
        self.assertRedirects(response, reverse('labels'))
        label = Labels.objects.get(id=1)
        self.assertEqual(str(label), 'label3')
        with self.assertRaises(ObjectDoesNotExist):
            Labels.objects.get(name='label1')


class DeleteLabelPageTest(TestCase):
    fixtures = [
        "users.json",
        "labels.json",
        "tasks.json",
        "statuses.json",
        "labelstasks.json"
    ]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/labels/1/delete/')
        self.assertEqual(response.status_code, 200)
        url = reverse('label_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('label_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_used_label_not_deleted(self):
        url = reverse('label_delete', kwargs={'pk': 1})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('labels'))
        label = Labels.objects.get(id=1)
        self.assertEqual(str(label), 'label1')

    def test_label_delete(self):
        url = reverse('label_delete', kwargs={'pk': 2})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('labels'))
        with self.assertRaises(ObjectDoesNotExist):
            Labels.objects.get(id=2)
