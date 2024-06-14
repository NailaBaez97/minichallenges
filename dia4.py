#Ordenar Lista: Escribe un programa que ordene una lista de números dada por el usuario en orden ascendente.

#PRIMERA SOLUCION

lista_usuario = input("Ingrese una lista de numeros al azar separados por comas: ")
lista_usuario= lista_usuario.split(",")
lista_usuario = [int(x)for x in lista_usuario]
lista_usuario.sort()
print("La lista ordenada es: ",lista_usuario)

#SEGUNDA SOLUCION
cadena_numeros = input("Ingrese una lista de numeros separadas por comas")
lista_numeros = []
numero_actual = ""
for caracter in cadena_numeros:
    if caracter == ",":
        lista_numeros.append(int(numero_actual))
        numero_actual= ""
    else:
        numero_actual += caracter
    if numero_actual:
        lista_numeros.append(int(numero_actual))

    for i in range(len(lista_numeros )- 1):
        for j in range(len(lista_numeros) -i -1):
            if lista_numeros[j] > lista_numeros[j+1]:
                lista_numeros[j],lista_numeros[j+1] = lista_numeros[j+1],lista_numeros[j]

print("Lista ordenada: ",lista_numeros)


