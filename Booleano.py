# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 16:56:41 2022

@author: Aaron
"""

import docx
import string
import numpy as np


from nltk.stem import PorterStemmer
ps = PorterStemmer()
from nltk.corpus import stopwords
sw = set(stopwords.words('spanish'))
#"C:/Users/jere1/Documents/docs/D1.docx"

def procesado_terminos(valor,cadena):
    if(valor == 0):
        parrafo = cadena
    else:
        
        doc = docx.Document(cadena)
        parrafo = doc.paragraphs[0].text
    
    
    parrafo = parrafo.lower()
    parrafo = parrafo.translate(str.maketrans('', '', string.punctuation))
    
    def limpiar_acentos(arreglo):
        texto = " ".join(arreglo)
        acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u'}
        for acen in acentos:
            if acen in texto:
                texto = texto.replace(acen, acentos[acen])
    
        arreglo=texto.split()
        return arreglo  
    
    
    lp = parrafo.split()
    
    a = list()
    for word in lp: 
        if word not in sw:
            a.append(word)
            
    b = list()
    for word in a: 
        b.append(ps.stem(word))
            
    b = list(set(limpiar_acentos(b)))
    
    return b

def armarIndice():
    dicc = {}
    l1 = procesado_terminos(1, "C:/Users/Aaron/Desktop/d1.docx")
    for i in l1:
        dicc[i] = []
    l2 = procesado_terminos(1, "C:/Users/Aaron/Desktop/d2.docx")
    for i in l2:
        dicc[i] = []
    l3 = procesado_terminos(1, "C:/Users/Aaron/Desktop/d3.docx")
    for i in l3:
        dicc[i] = []
    l4 = procesado_terminos(1, "C:/Users/Aaron/Desktop/d4.docx")
    for i in l4:
        dicc[i] = []
        
    for i in l1:
        dicc[i].append("d1")
    for i in l2:
        dicc[i].append("d2")
    for i in l3:
        dicc[i].append("d3")
    for i in l4:
        dicc[i].append("d4")

        
    return dicc

def procesarAnd(q1, q2):
    documentos1 = []
    documentos2 = []
    l1 = procesado_terminos(0, q1)
    for i in l1:
        for j in range(len(armarIndice()[i])):
            documentos1.append(armarIndice()[i][j])
            
    
    l2 = procesado_terminos(0, q2)
    for i in l2:
        for j in range(len(armarIndice()[i])):
            documentos2.append(armarIndice()[i][j])
            

    return(set(documentos1)&set(documentos2))
            

def procesarOr(q1, q2):
    documentos1 = []
    documentos2 = []
    l1 = procesado_terminos(0, q1)
    for i in l1:
        for j in range(len(armarIndice()[i])):
            documentos1.append(armarIndice()[i][j])
            
    
    l2 = procesado_terminos(0, q2)
    for i in l2:
        for j in range(len(armarIndice()[i])):
            documentos2.append(armarIndice()[i][j])
            

    return(set(documentos1)|set(documentos2))

            
            
print("casa y coche", procesarAnd("casa", "coche"))
print("casa o coche", procesarOr("casa", "coche"))
    
            
print("barco y perro", procesarAnd("barco", "perro"))
print("perro o gato", procesarOr("perro", "gato"))



