#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest

from app import retorna_numeros


class TestRe(unittest.TestCase):

    def test_retorna_numero_int(self):
        numeros = "un 10 y un 20"
        self.assertEqual(
            ['10', '20'],
            retorna_numeros(numeros)
        )

    def test_retorna_numero_negativo(self):
        numeros = "un -10 y un -20"
        self.assertEqual(
            ['-10', '-20'],
            retorna_numeros(numeros)
        )

    def test_retorna_numero_float(self):
        numeros = "un -10.3 y un -20."
        self.assertEqual(
            ['-10.3', '-20.'],
            retorna_numeros(numeros)
        )
