#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import knot


class TestContainer(unittest.TestCase):
    def test_returns_value(self):
        c = knot.Container({'value': 'foobar'})

        self.assertEqual(c('value'), 'foobar')

    def test_returns_return_value_provider(self):
        c = knot.Container()

        def foo(container):
            return 'bar'

        c.add_provider(foo, False)

        self.assertEqual(c('foo'), 'bar')

    def test_returns_default(self):
        c = knot.Container()

        self.assertEqual(c('foo', 'bar'), 'bar')
        self.assertEqual(c('foo', lambda c: 'baz'), 'baz')

    def test_uses_name_callable(self):
        c = knot.Container()

        def foo(container):
            return 'bar'

        c.add_provider(foo, False)

        self.assertEqual(c('foo'), 'bar')

    def test_caches_return_value_provider(self):
        c = knot.Container()

        def foobar(container):
            return {}

        c.add_provider(foobar, True)

        self.assertFalse(c.is_cached('foobar'))
        dict1 = c('foobar')
        dict2 = c('foobar')
        self.assertTrue(c.is_cached('foobar'))

        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        assert dict1 is dict2

    def test_registers_factory_with_decorator(self):
        c = knot.Container()

        @knot.factory(c)
        def foo(container):
            return 'bar'

        self.assertEqual(c('foo'), 'bar')

    def test_registers_service_with_decorator(self):
        c = knot.Container()

        @knot.service(c)
        def foo(container):
            return 'bar'

        self.assertEqual(c('foo'), 'bar')

    def test_registers_provider_with_decorator(self):
        c = knot.Container()

        @knot.provider(c, False)
        def foo(container):
            return 'bar'

        self.assertEqual(c('foo'), 'bar')


if __name__ == '__main__':
    unittest.main()
