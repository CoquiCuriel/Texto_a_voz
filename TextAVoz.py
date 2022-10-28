# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 10:20:56 2022

@author: Coqui
"""

from gtts import gTTS

print("**********"*5)
convertir = input("Que texto desea convertir a voz??")


s = gTTS(convertir, lang = 'es-us')

print("**********"*5)
nombre = input("Ingrese un nombre para el archivo de audio: ")


s.save(nombre+'.mp3')
print("**********"*5)
print("Archivo de audio generado correctamente con el nombre: ", nombre)
print("**********"*5)