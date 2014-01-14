'''
Created on 13/01/2014

@author: Rams
@mail: angelruiz21@gmail.com
'''
import urllib2
import json

url = "http://library.originalhacker.org/api/biblioteca/articulo/autor/2"
lee_url = urllib2.urlopen(url)
datos = json.load(lee_url)

for datos in datos:
	print "Titulo: %s"%(datos["titulo"])
	print "Autor: %s"%(datos["autor"])
	print "Seccion: %s"%(datos["seccion"])
	print "Revista: %s"%(datos["revista"])
	print "----------------------"


