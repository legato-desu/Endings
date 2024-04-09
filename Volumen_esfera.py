# Volumen de una esfera
"""
Crea un programa para calcular el 
volumen de una esfera a partir del radio dado
"""

from math import pi

r = float(input('Ingrese el radio de la esfera: '))

# La variable 'r' almacena el numero para hacer la operacion y adquirir en una nueva variable 'volumen' el resultado de el radio de la esfera

volumen = 4/3 * pi * r ** 3

print('El volumen de la esfera es {} unidades cubicas. '.format(volumen))