#Crear un Diccionario: Escribe un programa que crea un diccionario a partir de dos listas dadas:
# una de claves y otra de valores.
clave = input("Ingresar la clave: ")
valor = input("Ingresar el valor: ")
clave= clave.split(",")
valor = valor.split(",")
mi_diccionario = dict(zip(clave,valor))
print(mi_diccionario)
