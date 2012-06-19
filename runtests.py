#!/usr/bin/env python
import sys
import os

from django.conf import settings, global_settings

if not settings.configured:
    settings.configure(
            DATABASES={
                'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    }
                },
            INSTALLED_APPS=[
                'django.contrib.auth',
                'django.contrib.admin',
                'django.contrib.contenttypes',
                'django.contrib.sessions',
                'django.contrib.sites',
                'async_messages',
                'tests',
                ],
            MIDDLEWARE_CLASSES=global_settings.MIDDLEWARE_CLASSES + (
                'async_messages.middleware.AsyncMiddleware',
                ),
            ROOT_URLCONF='tests.urls',
            DEBUG=False,
            SITE_ID=1,
        )

from django.test.simple import DjangoTestSuiteRunner


def run_tests():
    # Modify path
    parent = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, parent)

    # Run tests
    test_runner = DjangoTestSuiteRunner(verbosity=2)
    failures = test_runner.run_tests(['tests'])
    sys.exit(failures)

if __name__ == '__main__':
    run_tests()
