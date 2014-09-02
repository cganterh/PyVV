#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from calc import suma


class TestOperacion(unittest.TestCase):

    def test_suma(self):

        self.assertEqual(5, suma(3, 2))

if __name__ == '__main__':
    unittest.main()
