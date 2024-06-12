#Tabla de Multiplicar: Escribe un programa que muestre la tabla de multiplicar de un número dado por el usuario.

numero_ingresado = input("Ingrese el numero a multiplicar")
numero = int(numero_ingresado)

for i in range(10):
    i=i+1
    resultado = numero * i
    print(numero,"x",i,"=",resultado)
    
