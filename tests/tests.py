from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import User
from django.contrib.messages import constants, set_level

from async_messages import message_user, message_users, messages


class MiddlewareTests(TestCase):

    def setUp(self):
        username, password = 'david', 'password'
        self.user = User.objects.create_user(username, "django-async@test.com", password)
        self.client = Client()
        self.client.login(username=username, password=password)

    def test_message_appears_for_user(self):
        message_user(self.user, "Hello")
        response = self.client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(1, len((msgs)))
        self.assertEqual('Hello', str((msgs)[0]))

    def test_message_appears_all_users(self):
        message_users(User.objects.all(), "Hello")
        response = self.client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(1, len((msgs)))
        self.assertEqual('Hello', str((msgs)[0]))

    def test_message_queue(self):
        message_user(self.user, "First Message")
        message_user(self.user, "Second Message")
        response = self.client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(2, len((msgs)))
        self.assertEqual('Second Message', str((msgs)[1]))


class AnonynousUserTests(TestCase):
    def test_anonymous(self):
        client = Client()
        response = client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(0, len((msgs)))


class TestMessagesApi(TestCase):
    def setUp(self):
        username, password = 'david', 'password'
        self.user = User.objects.create_user(username, "django-async@test.com", password)
        self.client = Client()
        self.client.login(username=username, password=password)

    def assertMessageOk(self, level):
        response = self.client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(1, len((msgs)))
        self.assertEqual('Hello', str((msgs)[0]))

    def test_info(self):
        messages.info(self.user, "Hello")
        self.assertMessageOk(constants.INFO)

    def test_success(self):
        messages.success(self.user, "Hello")
        self.assertMessageOk(constants.SUCCESS)

    def test_warning(self):
        messages.warning(self.user, "Hello")
        self.assertMessageOk(constants.WARNING)

    def test_error(self):
        messages.error(self.user, "Hello")
        self.assertMessageOk(constants.ERROR)

    def test_debug(self):
        messages.debug(self.user, "Hello")
        # 0 messages because by default django.contrib.messages ignore DEBUG
        # messages (this can be changed using set_level)
        response = self.client.get('/')
        msgs = list(response.context['messages'])
        self.assertEqual(0, len((msgs)))
