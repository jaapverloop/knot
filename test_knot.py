#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import knot


class TestContainer(unittest.TestCase):
    def test_returns_value(self):
        c = knot.Container({'value': 'foobar'})

        self.assertEqual(c('value'), 'foobar')

    def test_calls_factory(self):
        c = knot.Container()

        def foo(container):
            return 'bar'

        c.add_factory(foo, 'foo')

        self.assertEqual(c('foo'), 'bar')

    def test_returns_default(self):
        c = knot.Container()

        self.assertEqual(c('foo', 'bar'), 'bar')
        self.assertEqual(c('foo', lambda c: 'baz'), 'baz')

    def test_uses_name_callable(self):
        c = knot.Container()

        def foo(container):
            return 'bar'

        c.add_factory(foo)

        self.assertEqual(c('foo'), 'bar')

    def test_caches_factory(self):
        c = knot.Container()

        def foobar(container):
            return {}

        c.add_factory(foobar, 'foobar', True)

        self.assertFalse(c.is_cached('foobar'))
        dict1 = c('foobar')
        dict2 = c('foobar')
        self.assertTrue(c.is_cached('foobar'))

        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        assert dict1 is dict2

    def test_decorates_factory(self):
        c = knot.Container()

        @c.factory()
        def foo(container):
            return 'bar'

        self.assertEqual(c('foo'), 'bar')


if __name__ == '__main__':
    unittest.main()
