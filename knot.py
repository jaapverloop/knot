# -*- coding: utf-8 -*-

"""
knot
~~~~

Knot is a simple dependency container for Python.

:copyright: (c) 2014 by Jaap Verloop.
:license: MIT, see LICENSE for more details.

"""

from functools import update_wrapper


def factory(container, name=None, cache=False):
    """A decorator to register a factory on the container.
    For more information see :meth:`Container.add_factory`.
    """
    def decorator(factory):
        container.add_factory(factory, name)

    return decorator


def service(container, name=None):
    """A decorator to register a service on a container.
    For more information see :meth:`Container.add_service`.
    """
    def decorator(service):
        container.add_service(service, name)

    return decorator


def provider(container, cache, name=None):
    """A decorator to register a provider on a container.
    For more information see :meth:`Container.add_provider`.
    """
    def decorator(provider):
        container.add_provider(provider, cache, name)

    return decorator


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
    """The :class:`Container` object acts as a central registry for providers
    and configuration settings.

    This class is implemented as a subclass of ``dict``. All standard
    dictionary methods are available without any modifications.
    """

    def provide(self, name, default=None):
        """Gets the value registered with ``name`` and determines whether the
        value is a provider or not. The ``default`` is used if ``name`` is
        unknown.

        The registered value is interpreted as a provider if it's callable. The
        provider is called with a single argument, the current
        :class:`Container` object. Returns the return value of a provider or
        the value itself in case it's not callable.

        :param name: the name of the provider or value.
        :param default: the default value.
        """
        rv = super(Container, self).get(name)
        return rv(self) if callable(rv) else rv or default

    def add_factory(self, factory, name=None):
        """Registers a factory on the container. A factory is a provider with
        the ``cache`` argument set to ``False``.
        For more information see :meth:`add_provider`.
        """
        self.add_provider(factory, False, name)

    def add_service(self, service, name=None):
        """Registers a service on the container. A service is a provider with
        the ``cache`` argument set to ``False``.
        For more information see :meth:`add_provider`.
        """
        self.add_provider(service, True, name)

    def add_provider(self, provider, cache, name=None):
        """Registers a provider on the container.

        :param provider:
            Anything that's callable and expects exactly one argument, the
            :class:`Container` object.
        :param cache:
            Whether to cache the return value of the provider.
        :param name:
            Name of the provider.
            Default: name of the callable.
        """
        self[name or provider.__name__] = FunctionCache(provider) if cache else provider

    def is_cached(self, name):
        """Determines if the return value is cached. Always returns false if
        the registered value is not an instance of :class:`FunctionCache`.

        :param name:
            The name of the provider.
        """
        try:
            cached = super(Container, self).get(name).cached
        except AttributeError:
            cached = False

        return cached
