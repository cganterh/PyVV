#!/usr/bin/python
# -*- coding: utf-8 -*-
import unittest
from mock import patch

from app import buscar_archivo_por_extension


class TestBuscar(unittest.TestCase):

    def test_buscar_archivo_por_extension(self):


        self.assertEqual(
            'test.txt',
            buscar_archivo_por_extension('txt')
        )
