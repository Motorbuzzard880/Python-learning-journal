﻿# En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex,
# depositan un número par de huevos. Imagina que tienes una lista de números enteros en la que cada número representa
# la cantidad de huevos puestos por un dinosaurio en el parque.

# Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

# Objetivo:
# Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total de los huevos
# que pertenecen a los dinosaurios carnívoros
# (es decir, la suma de todos los números pares en la lista).
# """

def contador_carnivoro(lista):
    huevo_carnivoros = 0
    for huevo in lista:
        if huevo % 2 == 0:
            huevo_carnivoros += huevo
    return huevo_carnivoros


lista = [3, 4, 7, 5, 8]
print(contador_carnivoro(lista))
