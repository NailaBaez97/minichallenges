#Contar Vocales: Escribe un programa que cuente el número de vocales en una cadena dada.
# definir variable donde se va cargar la cantidad de vocales "voc" y poner 0
voc = 0
# definir que el usuario ingrese una palabra
palabra_ingresada = input("Ingrese una palabra ")
# definimos nuestro contador "c" y va recorrer la "palabra_ingresada"
for c in palabra_ingresada:
    # si en la posiciones que esta el contador "c" es igual a una vocal 
    if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
        voc = voc + 1

    if c == 'á' or c == 'é' or c == 'í' or c =='ó' or c == 'ú' or c == 'Á' or c == 'É' or c == 'Í' or c =='Ó' or c == 'Ú':
        voc = voc + 1

# imprimimos resultadoss
print("La cantidad de Vocales son: ",voc)