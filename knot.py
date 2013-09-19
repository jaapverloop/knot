# -*- coding: utf-8 -*-

"""
knot
~~~~

Knot is a simple dependency container for Python.

:copyright: (c) 2013 by Jaap Verloop.
:license: MIT, see LICENSE for more details.

"""

from functools import update_wrapper


class FunctionCache(object):
    """The :class:`FunctionCache` object wraps a function and ensures it's
    called only once by caching the return value.
    """

    def __init__(self, f):
        """Redirects function calls to :meth:`__call__`."""
        self._f = f
        self._cache = None
        update_wrapper(self, f)

    def __call__(self, *args, **kwargs):
        """Returns the return value of the real function. First it will attempt
        to return from cache before calling the real function.
        """
        if not self.cached:
            self._cache = self._f(*args, **kwargs)
        return self._cache

    @property
    def cached(self):
        """Indicates whether the real function is called and cached."""
        return self._cache is not None


class Container(dict):
    """The :class:`Container` object acts as a central registry for factories
    and arbitrary data like configuration settings.

    This class is implemented as a subclass of ``dict``. All standard
    dictionary methods are available without any modifications.
    """

    def __call__(self, name, default=None):
        """Gets the value registered with ``name`` and determines whether the
        value is a factory or not. The ``default`` is used if ``name`` is
        unknown.

        The value or ``default`` is interpreted as a factory if it's callable.
        The factory is called with a single argument, the current
        :class:`Container` object. Returns the return value of a factory or
        the value itself in case it's not callable.

        :param name: the name of the factory or value.
        :param default: the default value.
        """
        factory = super(Container, self).get(name, default)
        return factory(self) if callable(factory) else factory

    def factory(self, name=None, cache=False):
        """A decorator to register a factory on the container. For more
        information see :meth:`add_factory` which does basically the same
        thing.

        Example::

            from knot import Container

            c = Container()

            @c.factory(cache=True)
            def app(c):
                from somewhere import App
                app = App()

                return app
        """
        def decorator(f):
            self.add_factory(f, name, cache)
            return f

        return decorator

    def add_factory(self, f, name=None, cache=False):
        """Registers a factory on the container. A factory is a callable and
        takes exactly one argument, the :class:`Container` object.

        Example::

            from knot import Container

            c = Container()

            def app(c):
                from somewhere import App
                app = App()

                return app

            c.add_factory(app, cache=True)

        :param name: optional name of the factory, otherwise the name of the
                     callable will be used.
        :param cache: whether to cache the return value of the factory,
                      defaults to false.
        """
        self[name or f.__name__] = FunctionCache(f) if cache else f

    def is_cached(self, name):
        """Determines if the return value of a factory is cached.

        :param name: name of the factory
        """
        return super(Container, self).get(name).cached
