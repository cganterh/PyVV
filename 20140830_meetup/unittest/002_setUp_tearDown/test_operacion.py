#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest

from calc import suma
from calc import resta


class TestOperacion(unittest.TestCase):

    def setUp(self):
        self.a = 3
        self.b = 2

    def test_suma(self):
        self.assertEqual(5, suma(self.a, self.b))

    def test_resta(self):
        self.assertEqual(1, resta(self.a, self.b))

if __name__ == '__main__':
    unittest.main()
