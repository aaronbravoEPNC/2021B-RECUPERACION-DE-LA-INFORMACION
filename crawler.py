# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 17:53:54 2022

@author: Aaron
"""

import re
import requests


def obtenerContenidoPagina(url):
    r = requests.get(url)
    texto_html = r.text
    texto_html = re.sub("\s+", " ", texto_html)
    return texto_html
    
def extraerLinksProductos(contenido):
    regex_url_productos = re.compile(r'<article class="product_pod">.*?<h3>*?<a href="(.*?)"')
    resultados = re.findall(regex_url_productos, contenido)
    links = ["https://books.toscrape.com/catalogue/" + x for x in resultados]
    return links

def extraerTodosLinksProductos(): 
    todosUrlProductos = []       
    for page in range(1, 51):
        url = "https://books.toscrape.com/catalogue/page-{}.html".format(page)
        print("Crawling", url)
        contenido = obtenerContenidoPagina(url)
        links = extraerLinksProductos(contenido)
        todosUrlProductos.extend(links)
        
    return todosUrlProductos

def obtenerDetallesProducto(url):
    contenido = obtenerContenidoPagina(url)
    
    regex_titulo = re.compile(r'<h1>(.*?)</h1>')
    result = re.findall(regex_titulo, contenido)
    titulo = result[0]
    
    regex_detalle_producto = re.compile(r'<table class="table table-striped">(.*?)</table>')
    result = re.findall(regex_detalle_producto, contenido)
    detalle = result[0]
    
    regex_upc = re.compile(r'<th>UPC</th>\s*<td>(.*?)</td>')
    result = re.findall(regex_upc, detalle)
    upc = result[0]
    
    regex_precio = re.compile(r'<th>Price \(incl. tax\)</th\s*><td>(.*?)</td>')
    result = re.findall(regex_precio, detalle)
    precio = result[0]
    print("Titulo:", titulo, "UPC:", upc, "Precio:", precio)
    
    


    
if __name__ == "__main__":
    todosUrlProductos = extraerTodosLinksProductos()
    for url in todosUrlProductos:
        try:
            obtenerDetallesProducto(url)
        except:
            print("No se pudo realizaar la accion en", url)
                

        
    
    
    
    
    