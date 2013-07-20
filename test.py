#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import knot


class TestContainer(unittest.TestCase):
    def test_throws_exception_with_unknown_key(self):
        c = knot.Container()

        self.assertRaises(KeyError, lambda: c['unknown'])

    def test_wrapper_looks_like_service(self):
        c = knot.Container()

        @c.service('service')
        def service(container):
            """Docstring."""
            pass

        self.assertEqual(c['service'].__name__, 'service')
        self.assertEqual(c['service'].__doc__, 'Docstring.')

    def test_returns_if_value(self):
        c = knot.Container({'value': 'foobar'})

        self.assertEqual(c('value'), 'foobar')

    def test_calls_if_service(self):
        c = knot.Container()

        @c.service('service')
        def service(container):
            return 'foobar'

        self.assertEqual(c('service'), 'foobar')

    def test_shares_service(self):
        c = knot.Container()

        @c.service('service', True)
        def service(container):
            return {}

        dict1 = c('service')
        dict2 = c('service')

        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        assert dict1 is dict2


if __name__ == '__main__':
    unittest.main()
