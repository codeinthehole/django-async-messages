from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User

from async_messages import message_user, message_users


class MiddlewareTests(TestCase):

    def setUp(self):
        username, password = 'david', 'password'
        self.user = User.objects.create_user(username, "django-async@test.com", password)
        self.client = Client()
        self.client.login(username=username, password=password)
    
    def test_message_appears_for_user(self):
        message_user(self.user, "Hello")
        response = self.client.get('/')
        messages = list(response.context['messages'])
        self.assertEqual(1, len(messages))
        self.assertEqual('Hello', str(messages[0]))

    def test_message_appears_all_users(self):
        message_users(User.objects.all(), "Hello")
        response = self.client.get('/')
        messages = list(response.context['messages'])
        self.assertEqual(1, len(messages))
        self.assertEqual('Hello', str(messages[0]))

class AnonynousUserTests(TestCase):
    def test_anonymous(self):
        client = Client()
        response = self.client.get('/')
        messages = list(response.context['messages'])
        self.assertEqual(0, len(messages))
