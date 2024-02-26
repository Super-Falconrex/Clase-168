# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 08:44:40 2024

@author: anyta
"""

class percy_jackson:
    def __init__(self, Nombre, Personajes, Resumen, Calificación):
        self.id_nombre = Nombre
        self.id_personajes = Personajes
        self.id_resumen = Resumen
        self.id_cal = Calificación
        
    def añadirDatos(self):
        print("Nombre: " + self.id_nombre)
        print("Personajes: " + self.id_personajes)
        print("Resumen: " + self.id_resumen)
        print("Calificación: " + self.id_cal)
        
crearObjeto = percy_jackson("Percy Jackson", "Percy, Annabeth, Quirón, Sr.D, Grover, Thalía, Dioses-Griegos.", "Percy es un semidiós hijo de poseidón que, como todos los demás, padece de dislexia y TDHA, lo que no sabe es que una profecía lo involucra en una decisión que puede destruír el olipo o salvarlo, así es como comienza la travesía de este semidiós junto con su amigo grover, un sátiro y annabeth, hija de atenea.", "8/10")
crearObjeto.añadirDatos()