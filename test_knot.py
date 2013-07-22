#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import knot


class TestContainer(unittest.TestCase):
    def test_wrapper_looks_like_factory(self):
        c = knot.Container()

        @c.factory('factory')
        def factory(container):
            """Docstring."""
            pass

        self.assertEqual(c['factory'].__name__, 'factory')
        self.assertEqual(c['factory'].__doc__, 'Docstring.')

    def test_returns_if_value(self):
        c = knot.Container({'value': 'foobar'})

        self.assertEqual(c('value'), 'foobar')

    def test_calls_if_factory(self):
        c = knot.Container()

        @c.factory('factory')
        def factory(container):
            return 'foobar'

        self.assertEqual(c('factory'), 'foobar')

    def test_returns_default_with_unknown_key(self):
        c = knot.Container()

        self.assertEqual(c('factory', 'foobar'), 'foobar')
        self.assertEqual(c('factory', lambda c: 'foobar'), 'foobar')

    def test_shares_factory(self):
        c = knot.Container()

        @c.factory('factory', True)
        def factory(container):
            return {}

        dict1 = c('factory')
        dict2 = c('factory')

        assert isinstance(dict1, dict)
        assert isinstance(dict2, dict)
        assert dict1 is dict2


if __name__ == '__main__':
    unittest.main()
