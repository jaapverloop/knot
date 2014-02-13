#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from mock import MagicMock
from knot import Container, factory, service, provider


class TestContainer(unittest.TestCase):
    def test_returns_return_value_provider(self):
        c = Container()

        def foo(container):
            return 'bar'

        c.add_provider(foo, False)

        self.assertEqual(c.provide('foo'), 'bar')

    def test_returns_value(self):
        c = Container({'value': 'foobar'})

        self.assertEqual(c.provide('value'), 'foobar')

    def test_returns_default(self):
        c = Container()

        self.assertEqual(c.provide('foo', 'bar'), 'bar')

    def test_caches_return_value_provider(self):
        c = Container()

        def foobar(container):
            return {}

        c.add_provider(foobar, True)

        self.assertFalse(c.is_cached('foobar'))
        dict1 = c.provide('foobar')
        dict2 = c.provide('foobar')
        self.assertTrue(c.is_cached('foobar'))

        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        assert dict1 is dict2

    def test_uses_alternative_name(self):
        c = Container()

        def foobar(container):
            return 'foobar'

        c.add_provider(foobar, False, 'alternative')

        self.assertEqual(c.provide('alternative'), 'foobar')

    def test_registers_factory_with_decorator(self):
        c = Container()
        c.add_factory = MagicMock()

        @factory(c)
        def foo(container):
            pass

        c.add_factory.assert_called_with(foo, None)

        @factory(c, 'alternative')
        def bar(container):
            pass

        c.add_factory.assert_called_with(bar, 'alternative')

    def test_registers_service_with_decorator(self):
        c = Container()
        c.add_service = MagicMock()

        @service(c)
        def foo(container):
            pass

        c.add_service.assert_called_with(foo, None)

        @service(c, 'alternative')
        def bar(container):
            pass

        c.add_service.assert_called_with(bar, 'alternative')

    def test_registers_provider_with_decorator(self):
        c = Container()
        c.add_provider = MagicMock()

        @provider(c, False)
        def foo(container):
            pass

        c.add_provider.assert_called_with(foo, False, None)

        @provider(c, True, 'alternative')
        def bar(container):
            pass

        c.add_provider.assert_called_with(bar, True, 'alternative')


if __name__ == '__main__':
    unittest.main()
