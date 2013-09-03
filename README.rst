=====================
django-async-messages
=====================

Simple asynchronous messages for django.  Plays nicely with Celery.

Questions
=========

What problem does this solve?
-----------------------------

Suppose a user instigates an expensive task that you are processing offline (eg
using Celery).  This library provides a simple mechanism for notifying the user
when the task is finished, utilising Django's messaging framework.

What's an example?
------------------

You might use Celery to generate a large report and then employ this library to
notify the user that their report is ready to be downloaded.  The user will see
the message you've sent them when they make their next request after the message
is submitted.

How does it work?
-----------------

A cache is used to persist the messages, and middleware is used to pick these up
and submit them to `Django's messaging framework`_.  All very simple.

.. _`Django's messaging framework`: https://docs.djangoproject.com/en/dev/ref/contrib/messages/

Aren't there other libraries that do this?
------------------------------------------

Yes, there are - but they solve the problem in different ways:

* `django-offline-messages`_ - this provides an alternative storage backend that
  Django's messages framework can use.

* `django-notifications`_  

.. _`django-offline-messages`: https://github.com/dym/django-offline-messages
.. _`django-notifications`: https://github.com/jtauber/django-notification

What's good about this implementation?
--------------------------------------

* It's simple, fast and easy to use.  
* It works cohesively with existing Django cache and messages framework.  It
  will work no matter what cache backend your are using, and whatever storage
  backend is used for messages. 

What's bad?
-----------

* A user may miss the message if they navigating quickly between pages. But 
  this is a general problem of the Django messages framework.

Install
=======

From PyPI (stable)::

    pip install django-async-messages

From Github (unstable)::

    pip install git+git://github.com/codeinthehole/django-async-messages#egg=djang-async-messages

Add ``'async_messages.middleware.AsyncMiddleware'`` to your ``MIDDLEWARE_CLASSES``.
Ensure it comes after ``'django.contrib.messages.middleware.MessageMiddleware'``.

You need to have ``CACHES`` configured in you settings for this to work.  As usual,
memcache is the best choice.  Note that `local memory caching`_ is not suitable as
each process has its own private cache and a Celery task can't communicate with
the webserver process cache.

.. _`local memory caching`: https://docs.djangoproject.com/en/dev/topics/cache/#local-memory-caching

Use
===

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

Send multiple messages to a single user::

    >>> from async_messages import message_user
    >>> from django.contrib.auth.models import User
    >>> barry = User.objects.get(username='barry')
    >>> message_user(barry, "Barry, your report is queued up for processing") 
    >>> # do more awesome stuff
    >>> message_user(barry, "Barry, your report is ready") 

Alternative way to send a message to a single user, imitating the django.contrib.messages API::

    >>> from async_messages import messages
    >>> barry = User.objects.get(username='barry')
    >>> messages.debug(barry, "Barry was here")
    >>> messages.info(barry, "Hi, Barry")
    >>> messages.success(barry, "Barry, your report is ready")
    >>> messages.warning(barry, "Barry, you didn't lock your session")
    >>> messages.error(barry, "You are not Barry")

Contributing
============

Fork, clone and create a virtualenv.  Then run::

    make install

Run tests with::

    ./runtests.py

Please submit pull requests using 'develop' as the target branch.

License
=======

MIT_

.. _MIT: http://en.wikipedia.org/wiki/MIT_License

Changelog
=========

0.3
---
* Mimic ``django.contrib.messages`` API for sending a message to a user

0.2
---
* Added possibility to queue multiple messages

0.1.2
-----
* Altered dependency on Django to be only 1.2+

0.1.1
-----
* Altered middleware to use ``process_response``.
* Better docstrings

0.1
---
* Minimum viable product
