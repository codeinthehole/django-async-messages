=====================
django-async-messages
=====================

Simple asynchronous messages for django.  

Questions
=========

What problem does this solve?
-----------------------------

Suppose a user instigates an expensive task that you are processing offline (eg
using Celery).  This library provides a simple mechanism for notifying the user
when the task is finished.

For instance, you might use Celery to generate a large report and then
use this library to notify the user that their report is ready to be downloaded.

How does it work?
-----------------

A cache is used to persist the messages, and middleware is used to pick these up
and add them to Django's messages.  All very simple.

Aren't there other libraries that do this?
------------------------------------------

Yes, there are - but they solve the problm in different ways:

* `django-offline-messages`_ - this provides an alternative storage backend that
  Django's messages framework can use.

* `django-notifications`_  

.. _`django-offline-messages`: https://github.com/dym/django-offline-messages
.. _`django-notifications`: https://github.com/jtauber/django-notification

Install
-------

From PyPI (stable)::

    pip install django-async-messages

From Github (unstable)::

    pip install
    git+git://github.com/codeinthehole/django-async-messages#egg=djang-async-messages

Add ``async_messages.middleware.AsyncMiddleware`` to your ``INSTALLED_APPS``.
Ensure it comes after ``django.contrib.messages.middleware.MessageMiddleware``.

You need to have a cache set up in you settings for this to work.  As usual,
memcache is the best choice.

Use
---

Send a message to a single user::

    >>> from async_messages import message_user
    >>> from django.contrib.auth.models import User
    >>> barry = User.objects.get(username='barry')
    >>> message_user(barry, "Barry, your report is ready") 

Send a message to lots of users::

    >>> from async_messages import message_users
    >>> staff = User.objects.filter(is_staff=True)
    >>> message_users(staff, "All budgets must be spent by the end of the day")

Specify message level::

    >>> from django.contrib.messages import constants
    >>> message_users(staff, "Boom!", constants.WARNING)
