# Programa para generar un número aleatorio en Python
import random
# La función input() captura un datos desde el teclado.
# como si fuera una cadena de texto (string)
a= input("Límite inferior:")
b= input("Límite Superior:")

#Convertir a y b a enteros
a= int(a)
b= int(b)
respuesta= random.randint(a,b)
print(respuesta)