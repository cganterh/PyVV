#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


cadena = "didddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddsadsjdsahdsadhak"


def buscar_archivo_por_extension(ext):


    for file_name in os.listdir('.'):
        if file_name.endswith(ext):
            return file_name
