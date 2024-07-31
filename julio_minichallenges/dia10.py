#Eliminar duplicados: Implementa una función que elimina los elementos duplicados de una lista de 10 enteros.

lista = [1,2,2,3,4,4,5,5,6,7,8,8,9,10,10]

conjunto = set(lista)

lista = list(conjunto)

print(lista) 