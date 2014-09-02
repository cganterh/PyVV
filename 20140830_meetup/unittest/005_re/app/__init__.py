#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


def retorna_numeros(linea):
    return re.findall(r'-?\d+\.?\d*', linea)
