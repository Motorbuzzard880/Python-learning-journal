﻿

from os import system
if system("clear") != 0: system("cls")

import re



texto = """En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lentejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda.
El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta, y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza, que así ensillaba el rocín como tomaba la podadera.
Frisaba la edad de nuestro hidalgo con los cincuenta años; era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de Quijada, o Quesada, que en esto hay alguna diferencia en los autores que deste caso escriben; aunque por conjeturas verosímiles se deja entender que se llamaba Quejana. Pero esto importa poco a nuestro cuento; basta que en la narración dél no se salga un punto de la verdad.
Es, pues, de saber que este sobredicho hidalgo, los ratos que estaba ocioso (que eran los más del año), se daba a leer libros de caballerías con tanta afición y gusto, que olvidó casi de todo punto el ejercicio de la caza, y aun la administración de su hacienda; y llegó a tanto su curiosidad y desatino en esto, que vendió muchas hanegas de tierra de sembradura para comprar libros de caballerías en que leer, y así, llevó a su casa todos cuantos pudo haber dellos.
De tanto leer estos libros, se le secó el cerebro de modo que vino a perder el juicio. Llenósele la fantasía de todo aquello que leía en los libros, así de encantamentos como de pendencias, batallas, desafíos, heridas, requiebros, amores, tormentas y disparates imposibles; y asentósele de tal modo en la imaginación que era verdad toda aquella máquina de aquellas soñadas invenciones que leía, que para él no había otra historia más cierta en el mundo."""

pattern = "hidalgo"

resultado = re.search(pattern, texto)

if resultado:
    print(f"He encontrado la palabra: {resultado.group()}")
else:
    print("No he encontrado la palabra")

ocurrencias = re.findall(pattern, texto)
print(f"La palabra aparece {len(ocurrencias)} veces.")


#Tambien podria hacer una busqueda que no distinga mayúsculas/minúsculas

# resultado = re.search(pattern, texto, re.IGNORECASE) 



# EJERCICIO 01
# Encuentra la primera ocurrencia de la palabra "IA" en el siguiente texto
# e indica en que posición empieza y termina la coincidencia.

text = "Todo el mundo dice que la IA nos va a quitar el trabajo. Pero solo hace falta ver cómo la puede cagar con las Regex para ir con cuidado"
pattern = "IA"

resultado = re.search(pattern, text)
if resultado:
	print(f"Posición de 'IA': inicio= {resultado.start()}, fin= {resultado.end()}")
else:
	print("No se encontró el patrón 'IA' en el texto.")



# -----------------------

### EJERCICIO 02 Encontrar todas las coincidencias de un patrón
# .findall() devuelve una lista con todas las coincidencias

text = "Me gusta Python. Python es lo máximo. Aunque Python no es tan difícil, ojo con Python"
pattern = "Python"

matches = re.findall(pattern, text)
print(f"La palabra {pattern} aparece {len(matches)} en el texto")


# EJERCICIO 03
# Encuentra todas las ocurrencias de la palabra "midu" en el siguiente texto e indica en que posición empieza y termina cada coincidencia y cuantas veces se encontró.

text = "Este es el curso de Python de midudev. ¡Suscríbete a midudev si te gusta este contenido! midu"
pattern = "midu"

ocurrencia = re.finditer(pattern, text)

for match in ocurrencia:
    print(f'{match.group()} encontrado en {match.start()}-{match.end()}')



# EJERCICIO 04
# Encuentra todas las ocurrencias de la palabra "python" en el siguiente texto, sin distinguir entre mayúsculas y minúsculas.
text = "Este es el curso de Python de midudev. ¡Suscríbete a python si te gusta este contenido! PYTHON"

pattern = "Python"

palabra= re.findall(pattern, text, re.IGNORECASE)
print(palabra)



# EJERCICIO 05:
# Tenemos una lista de archivos, necesitamos saber los nombres de los ficheros con extension .txt:

text = "file1.txt file2.pdf midu-of.webp secret.txt"
pattern = r"\b\w+\.txt\b"

# r"\b\w+\.txt\b" significa:
# \b: Límite de palabra (asegura que estamos al inicio de un nombre de archivo)
# \w+: Uno o más caracteres de palabra (letras, números o guiones bajos)
# \.txt: La extensión .txt (el punto se escapa con )
# \b: Otro límite de palabra (asegura que .txt está al final)

matches = re.finditer(pattern, text)
for match in matches:
    print(match.group())


# Ejercicio 06:
# ¿Cuantas palabras tienen de 0 a más "a" y después una b?

texto = "b ab aab aaab zyb abb ba a abc bb"
palabras_cumplen = re.findall(r'\ba*b\b', texto)
cantidad = len(palabras_cumplen)
print("Palabras que cumplen el patrón:", palabras_cumplen)
print("Total de palabras validas", cantidad)


# Ejercicio 07: Haz opcional que aparezca un +34 en el siguiente texto
phone = "+34 688999999"
pattern = r'^((\+|00)34)([ -]?\d{6,9})$'
matches = re.findall(pattern, phone)
print(matches)