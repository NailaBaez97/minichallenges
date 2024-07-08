# Generador de Contraseñas Seguras: Escribe un programa que genere una contraseña segura de longitud variable
# (entre 8 y 16 caracteres) que incluya letras mayúsculas, minúsculas, números y símbolos.
# Importar modulos necesarios
import random
import string

# Solicitar longitud de contrasenhas
longitud = int(input("Ingrese la longitud deseada para su contrasenha (Entre 8 y 16): "))

# Validar la longitud de la contrasenha
if longitud < 8 or longitud > 16:
    print("ERROR: La longitud debe tener entre 8 y 16 caracteres")
else:
    # Definir los caracteres posibles (string.ascii es un modulo de python para definir conjuntos de caracteres)
    mayusculas = string.ascii_uppercase
    minusculas = string.ascii_lowercase
    numeros = string.digits
    simbolos = string.punctuation

    # Generar la contrasenha
    password = []
    for i in range(longitud):
        tipo_caracter = random.choice([mayusculas, minusculas, numeros, simbolos])
        caracter = random.choice(tipo_caracter)
        password.append(caracter)

    # Mezclar los caracteres para mayor seguridad
    random.shuffle(password)

    #convertir la lista es cadena
    contraseña_final = ''.join(password)

    # Mostrar la contrasenha generada
    print("La contrasenha es: ", contraseña_final)
