from django.test import TestCase
from .models import Task

class TaskModelTest(TestCase):

    def setUp(self):
        self.task = Task.objects.create(
            title='Test Task',
            description='This is a test task.',
            completed=False,
            due_date='2023-12-31',
            city='Test City'
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertEqual(self.task.description, 'This is a test task.')
        self.assertFalse(self.task.completed)
        self.assertEqual(str(self.task), 'Test Task')

    def test_task_completed(self):
        self.task.completed = True
        self.task.save()
        self.assertTrue(self.task.completed)

    def test_task_due_date(self):
        self.assertEqual(self.task.due_date.strftime('%Y-%m-%d'), '2023-12-31')

    def test_task_city(self):
        self.assertEqual(self.task.city, 'Test City')