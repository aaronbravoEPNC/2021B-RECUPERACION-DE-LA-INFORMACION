# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 20:05:06 2022

@author: Aaron
"""


relevantes = int(input("Numero de documentos relevantes:\n"))

previos = int(input("Numero de documentos relevantes previos:\n"))

posteriores = int(input("Numero de dcocumentos relevantes posteriores:\n"))

print('Su Tasa de Cobertura es: ', posteriores/previos)

print("Su tasa de novedad es: ", (relevantes-posteriores)/relevantes)
