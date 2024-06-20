#Juego de Piedra, Papel o Tijeras: Escribe un programa que permita al usuario jugar piedra, papel o tijeras 
#contra la computadora.

import random

#SOLUCION 1
print("Bienvenido a la primera solucion")
#definir las opciones posibles
eleccion_computadora = ""
eleccion_usuario = ""
def solucion_uno():
    opciones1= ["piedra" , "papel" , "tijera"]
#solicitar entrada al usuario
    eleccion_usuario = input("Ingrese su eleccion (Piedra, Papel o Tijera)")
#Generar eleccion de la computadora 
    eleccion_computadora = random.choice(opciones1)
#Comparar elecciones y determinar el ganador 
    if eleccion_usuario == eleccion_computadora:
        print("Es un empate")
    elif ((eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or 
            (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or 
            (eleccion_usuario == "tijeras" and eleccion_computadora == "papel")):
        print("Ganaste")
    else:
        print("La Computadora Gana")
    #Mostrar eleccion y resultado
    print(f"El usuario eligio {eleccion_usuario} y la computadora {eleccion_computadora}")
solucion_uno()


#SOLUCION 2
print("Bienvenido a la segunda solucion")

def solucion_dos():
    turnou = 0
    turnoc = 0
    #definir las opciones posibles
    opciones2 = ["piedra","papel","tijera"]


    for turnou in range(3):
        #solicitar entrada al usuario
        eleccion_usuario = input("Ingrese su opcion(Piedra, Papel o Tijera): ").lower()
        #Generar eleccion de la computadora 
        eleccion_computadora = random.choice(opciones2)
        print(f"La computadora eligio: {eleccion_computadora}")
        #Comparar elecciones y determinar el ganador 
        if ((eleccion_usuario == "piedra" and eleccion_computadora == "tijera") or 
            (eleccion_usuario == "papel" and eleccion_computadora == "piedra") or 
            (eleccion_usuario == "tijera" and eleccion_computadora == "papel")):
            print("Ganaste este turno")
            turnou +=1   
    
        elif (turnou < turnoc):
            print("Gano este turno la computadora")
            turnoc = turnoc + 1
        else:
            print("Es un empate")
    #Mostrar eleccion y resultado
    print(f"Victoras del usuario  {turnou} victorias de la computadora {turnoc}")
solucion_dos()
