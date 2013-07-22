# -*- coding: utf-8 -*-

"""
knot
~~~~

Lightweight dependency container without magic.

:copyright: (c) 2013 by Jaap Verloop.
:license: MIT, see LICENSE for more details.

"""

from functools import wraps


class Container(dict):
    def __call__(self, key, default=None):
        factory = super(Container, self).get(key, default)
        return factory(self) if callable(factory) else factory

    def factory(self, key, share=False):
        def decorator(f):
            @wraps(f)
            def wrapper(container):
                if not share:
                    return f(container)

                if '_' not in wrapper.__dict__:
                    wrapper._ = f(container)

                return wrapper._

            self[key] = wrapper
            return wrapper

        return decorator
