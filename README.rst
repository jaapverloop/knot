Knot
****

.. image:: https://badge.fury.io/py/knot.png
  :target: http://badge.fury.io/py/knot

.. image:: https://travis-ci.org/jaapverloop/knot.png?branch=master
  :target: https://travis-ci.org/jaapverloop/knot

Knot is a small do-it-yourself (DIY) dependency container for Python.


Getting started
===============

Unlike other existing implementations, knot does not make use of introspection.
Therefore, dependencies are manually defined in a straight forward manner. The
container acts as a central registry for providers and configuration settings.


Configuration settings
----------------------

The container is just an ordinary dictionary with some additional methods. As a
result, it is very easy to assign or retrieve data from it. Probably the most
common way to assign configuration settings is passing a dict to the
constructor.

.. code-block:: python

    from knot import Container

    c = Container({'host': 'localhost', 'port': 6379})

Obviously it is also possible to add configuration settings to an existing
container.

.. code-block:: python

    c = Container()
    c['host'] = 'localhost'
    c['port'] = 6379


Providers
---------

A provider creates and returns a particular value or object. It has the ability
to utilize an injected container to retrieve the necessary configuration
settings and dependencies.

The container expects a provider to adhere to the following rules:

1. It must be callable.
2. It must accept the container as the only argument.
3. It must return anything except ``None``.

Assigning a provider to a container is easy.

.. code-block:: python

    def connection(c):
        from redis import Redis
        return Redis(host=c['host'], port=c['port'])

    c.add_provider(connection, True)

It is also possible to use a decorator.

.. code-block:: python

    from knot import provider

    @provider(c, True)
    def connection(c):
        from redis import Redis
        return Redis(host=c['host'], port=c['port'])

The second argument in ``c.add_provider(connection, True)`` and in
``@provider(c, True)`` indicates whether or not the return value of a provider
must be cached.

Retrieve what you have defined.

.. code-block:: python

    conn = c.provide('connection')

For convenience, you can also use the shortcut.

.. code-block:: python

    conn = c('connection')


Services
--------

A service is just a provider with the **cache** argument set to ``True``.
Basically this means the return value is created only once.

.. code-block:: python

    def connection(c):
        from redis import Redis
        return Redis(host=c['host'], port=c['port'])

    c.add_service(connection)

Or with a decorator.

.. code-block:: python

    from knot import service

    @service(c)
    def connection(c):
        from redis import Redis
        return Redis(host=c['host'], port=c['port'])

    conn1 = c('connection')
    conn2 = c('connection')

    print conn1 is conn2 # True


Factories
---------

A factory is just a provider with the **cache** argument set to ``False``.
Basically this means the return value is created on every call.

.. code-block:: python

    def urgent_job(c):
        from somewhere import Job
        connection = c('connection')
        return Job(connection=connection, queue='urgent')

    c.add_factory(urgent_job)

    job1 = c('urgent_job')
    job1.enqueue('send_activation_mail', username='johndoe')

    job2 = c('urgent_job')
    job2.enqueue('send_activation_mail', username='janedoe')

    print job1 is job2 # False

Or with a decorator.

.. code-block:: python

    from knot import @factory

    @factory(c)
    def urgent_job(c):
        from somewhere import Job
        connection = c('connection')
        return Job(connection=connection, queue='urgent')


Installation
============

Install Knot with the following command:

.. code-block:: console

  $ pip install knot


Tests
=====

To run the tests, install **tox** first:

.. code-block:: console

  $ pip install tox

Then, run the tests with the following command:

.. code-block:: console

  $ tox


Inspiration
===========

Pimple (http://pimple.sensiolabs.org/)


License
=======

MIT, see **LICENSE** for more details.
