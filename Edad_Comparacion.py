# Edad de 2 personas
"""
Escribir un Programa que solicite al usuario la edad de 2 
personas, y diga cuál es mayor. Ejemplo:

- La Primera persona es mayor!

Si la edad de ambos es igual se muestra el siguiente mensaje:

- Ambos tienen la misma edad!
"""

persona_1 = int(input("Ingrese la edad de la primer persona: "))
persona_2 = int(input("Ingrese la edad de la segunda persona: "))

if persona_1 == persona_2:
    print("Ambos tienen la misma edad! ")
elif persona_1 > persona_2:
    print("La primera persona es mayor")
else:
    print("La segunda persona es mayor")        