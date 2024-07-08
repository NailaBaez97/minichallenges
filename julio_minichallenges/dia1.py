#Búsqueda en lista ordenada: Implementa una función de búsqueda binaria que determine si un número está en una lista ordenada de 10 elementos.
def buscar_numero(lista, numero):

    inicio = 0
    final = len(lista) - 1

    while inicio <= final:
        mitad = (inicio + final) // 2
        if lista[mitad] == numero:
            return f"Número encontrado en la posición {mitad}"
        elif lista[mitad] > numero:
            final = mitad - 1
        else:
            inicio = mitad + 1
    return "Número no encontrado"

lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_a_buscar = 10

resultado = buscar_numero(lista_ordenada, numero_a_buscar)
print(resultado)
