# -*- coding: utf-8 -*-

"""
knot
~~~~

Knot is a simple dependency container for Python.

:copyright: (c) 2013 by Jaap Verloop.
:license: MIT, see LICENSE for more details.

"""

from functools import wraps


class Container(dict):
    """The :class:`Container` object acts as a central registry for factories
    and arbitrary data like configuration settings.

    This class is implemented as a subclass of ``dict``. All standard
    dictionary methods are available without any modifications.
    """

    def __call__(self, key, default=None):
        """Gets the value registered with ``key`` and determines whether the
        value is a factory or not. The ``default`` is used if ``key`` is
        unknown.

        The value or ``default`` is interpreted as a factory if it's callable.
        The factory is called with a single argument, the current
        :class:`Container`. Returns the response of a factory or the value
        itself in case it's not callable.

        :param key: The identifier of the factory or value.
        :param default: The default value.
        """
        factory = super(Container, self).get(key, default)
        return factory(self) if callable(factory) else factory

    def factory(self, key, share=False):
        """Registers a factory on the container. This method is intented to be
        used as a decorator. A factory should accept the container as the only
        argument.

        Usage::

            from knot import Container

            c = Container()

            @c.factory('app')
            def app(c, True):
                from somewhere import App
                app = App()

                return app

        :param key: The identifier of the factory.
        :param share: Whether the first response should be shared.
        """
        def decorator(factory):
            @wraps(factory)
            def wrapper(container):
                if not share:
                    return factory(container)

                if '_' not in wrapper.__dict__:
                    wrapper._ = factory(container)

                return wrapper._

            self[key] = wrapper
            return wrapper

        return decorator
