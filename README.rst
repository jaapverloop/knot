Knot
****

.. image:: https://badge.fury.io/py/knot.png
  :target: http://badge.fury.io/py/knot

.. image:: https://travis-ci.org/jaapverloop/knot.png?branch=master
  :target: https://travis-ci.org/jaapverloop/knot

Knot is a simple dependency container for Python.


Inspiration
===========
Pimple (http://pimple.sensiolabs.org/)


Example
=======

.. code-block:: python

    from knot import Container, service, factory

    c = Container({
      'host': 'localhost',
      'port': '6379',
    })

    @service(c)
    def connection(c):
        connection = Connection(c['host'], c['port'])
        return connection

    @factory(c)
    def worker(c):
        worker = Worker(c.provide('connection'))
        return worker

    worker1 = c.provide('worker')
    worker2 = c.provide('worker')


Installation
============

Install Knot with the following command:

.. code-block:: console

  $ pip install knot


Tests
=====

To run the tests, install **pytest** first:

.. code-block:: console

  $ pip install pytest

Then, run the tests with the following command:

.. code-block:: console

  $ make test


License
=======

MIT, see **LICENSE** for more details.
