# Ordenamiento simple: Escribe una función que ordena una lista de 5 enteros utilizando cualquier método de ordenamiento que prefieras (por ejemplo, burbuja, inserción, selección).
def ordenarLista(lista):
    #burbuja
    for i in range(4):  
        for j in range(4 - i):  
            if lista[j] > lista[j + 1]:  
                lista_temporal = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = lista_temporal
    return lista

lista_original = [10, 70, 48, 98, 1]
print("Lista original:", lista_original)
lista_ordenada = ordenarLista(lista_original)
print("Lista ordenada:", lista_ordenada)
