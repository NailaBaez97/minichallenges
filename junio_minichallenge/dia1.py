#Inversión de una Cadena: Escribe un programa que invierte una cadena de caracteres dada por el usuario.

cadena_original = input("Ingrese la cadena de caracteres que deseas que se invierta: ")
cadena_invertida = ""

for letra in cadena_original:
    cadena_invertida = letra + cadena_invertida 
print("Esta es la cadena invertida",cadena_invertida)