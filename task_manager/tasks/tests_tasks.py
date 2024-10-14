from django.test import TestCase
from django.urls import reverse
from task_manager.tasks.models import Tasks
from django.core.exceptions import ObjectDoesNotExist


class TasksPageTest(TestCase):
    fixtures = ["users.json"]

    def test_view_url(self):
        self.client.login(username='tester1', password='123')
        response = self.client.get('/tasks/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('tasks'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        response = self.client.get(reverse('tasks'))
        self.assertRedirects(response, reverse('login'))


class TaskPageTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def test_view_url(self):
        self.client.login(username='tester1', password='123')
        response = self.client.get('/tasks/1/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('task', kwargs={'pk': 1}))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        response = self.client.get(reverse('task', kwargs={'pk': 1}))
        self.assertRedirects(response, reverse('login'))


class CreateTaskPageTest(TestCase):
    fixtures = ["users.json", "statuses.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/tasks/create/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('task_create'))
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        response = self.client.get(reverse('task_create'))
        self.assertRedirects(response, reverse('login'))

    def test_create_task(self):
        credentials = {
            "name": "task1",
            "status": 1
        }
        response = self.client.post(
            reverse('task_create'), credentials, follow=True)
        self.assertRedirects(response, reverse('tasks'))
        task = Tasks.objects.get(name='task1')
        self.assertEqual(str(task), 'task1')
        self.assertEqual(task.author.id, 1)


class EditTaskPageTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/tasks/1/update/')
        self.assertEqual(response.status_code, 200)
        url = reverse('task_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('task_update', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_task_update(self):
        credentials = {
            "name": "task4",
            "description": "",
            "executor": 1,
            "status": 1,
        }
        url = reverse('task_update', kwargs={'pk': 1})
        response = self.client.post(url, credentials, follow=True)
        self.assertRedirects(response, reverse('tasks'))
        task = Tasks.objects.get(id=1)
        self.assertEqual(str(task), 'task4')
        with self.assertRaises(ObjectDoesNotExist):
            Tasks.objects.get(name='task1')


class DeleteTaskPageTest(TestCase):
    fixtures = ["users.json", "statuses.json", "tasks.json"]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_view_url(self):
        response = self.client.get('/tasks/1/delete/')
        self.assertEqual(response.status_code, 200)
        url = reverse('task_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_no_auth(self):
        self.client.logout()
        url = reverse('task_delete', kwargs={'pk': 1})
        response = self.client.get(url)
        self.assertRedirects(response, reverse('login'))

    def test_task_delete(self):
        url = reverse('task_delete', kwargs={'pk': 1})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('tasks'))
        with self.assertRaises(ObjectDoesNotExist):
            Tasks.objects.get(name='task1')

    def test_task_not_delete_if_not_autor(self):
        self.client.logout()
        self.client.login(username='tester2', password='123')
        url = reverse('task_delete', kwargs={'pk': 1})
        response = self.client.post(url, {}, follow=True)
        self.assertRedirects(response, reverse('tasks'))
        task = Tasks.objects.get(name='task1')
        self.assertEqual(str(task), 'task1')


class TaskFilteTest(TestCase):
    fixtures = [
        "users.json",
        "labels.json",
        "tasks.json",
        "statuses.json",
        "labelstasks.json"
    ]

    def setUp(self):
        self.client.login(username='tester1', password='123')

    def test_without_filter(self):
        response = self.client.get(reverse('tasks'))
        self.assertContains(response, "task1", status_code=200)
        self.assertContains(response, "task2", status_code=200)
        self.assertContains(response, "task3", status_code=200)

    def test_status_filter(self):
        args = {
            'status': '2'
        }
        response = self.client.get(reverse('tasks'), args)
        self.assertNotContains(response, "task1", status_code=200)
        self.assertNotContains(response, "task2", status_code=200)
        self.assertContains(response, "task3", status_code=200)

    def test_executor_filter(self):
        args = {
            'executor': '1'
        }
        response = self.client.get(reverse('tasks'), args)
        self.assertContains(response, "task1", status_code=200)
        self.assertContains(response, "task2", status_code=200)
        self.assertNotContains(response, "task3", status_code=200)

    def test_label_filter(self):
        args = {
            'label': '1'
        }
        response = self.client.get(reverse('tasks'), args)
        self.assertContains(response, "task1", status_code=200)
        self.assertNotContains(response, "task2", status_code=200)
        self.assertNotContains(response, "task3", status_code=200)

    def test_self_tasks_filter(self):
        args = {
            'self_tasks': 'on'
        }
        response = self.client.get(reverse('tasks'), args)
        self.assertContains(response, "task1", status_code=200)
        self.assertContains(response, "task2", status_code=200)
        self.assertNotContains(response, "task3", status_code=200)
