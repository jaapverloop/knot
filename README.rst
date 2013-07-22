Knot
====

.. image:: https://travis-ci.org/jaapverloop/knot.png?branch=master
  :target: https://travis-ci.org/jaapverloop/knot

Lightweight dependency container without magic.


Built with a lot of inspiration from ``Pimple`` (http://pimple.sensiolabs.org/)


Status
------
Consider this project a work in progress.


Usage
-----

.. code-block:: python

    from knot import Container

    c = Container({'host': 'localhost', 'port': 6379, 'db': 0})

    @c.factory('redis', True)
    def redis(c):
        from redis import Redis

        client = Redis(host=c['host'], port=c['port'], db=c['db'])
        return client

    @c.factory('stats', True)
    def stats(c):
        from somewhere import Counter

        counter = Counter(c('redis'))
        return counter


    c('stats').incr('reads')


Tests
-----

.. code-block:: console

  $ pip install -r requirements-dev.txt
  $ make run-tests


TODO
----

- Register at PyPi
- Documentation


License
-------

MIT, see ``LICENSE`` for more details.
