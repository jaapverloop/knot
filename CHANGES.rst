Knot Changelog
===============

Here you can see a list of changes between each release.


Version 0.4
-----------

2016-05-24: Feature release.

- Raise a ``KeyError`` exception instead of returning an optional default
  value in case a ``name`` is not found.


Version 0.3
-----------

2014-03-20: Feature release.

- Never cache the return value of ``add_factory`` and ``factory``. The decorator
  is implemented as a function instead of a method.

- Add a ``add_service`` method and the corresponding ``service`` decorator. Like
  a factory except it will always cache the return value.

- Add a ``add_provider`` method and the corresponding ``provider`` decorator.
  Set a cache strategy manually.

- Add a ``provide`` method for retrieving and keep ``__call__`` as a shortcut
  for convenience.

- Suppress exceptions raised from within ``is_cached``.


Version 0.2
-----------

2013-09-19: Feature release.

- Add the ability to check whether a cacheable factory is cached. The function
  ``cache_function`` is removed in favor of the ``FunctionCache`` class.


Version 0.1
-----------

2013-07-30: First release.
