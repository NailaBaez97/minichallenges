#Camino más corto: Dado un grafo pequeño con 5 nudos y 6 aristas, escribe una función que encuentre el camino más corto entre dos nudos especificados usando cualquier método que prefieras.

def distancia_manhattan(nodo1, nodo2):
    
    return abs(nodo1[0] - nodo2[0]) + abs(nodo1[1] - nodo2[1])

def obtener_nodo_con_menor_costo(nodos, costos):
    nodo_menor_costo = None
    menor_costo = float('inf')
    for nodo in nodos:
        if costos[nodo] < menor_costo:
            nodo_menor_costo = nodo
            menor_costo = costos[nodo]
    return nodo_menor_costo

def a_estrella(grafo, nodo_inicio, nodo_objetivo):
    costo_acumulado = {nodo: float('inf') for nodo in grafo}
    distancia_estimada = {nodo: float('inf') for nodo in grafo}
    costo_acumulado[nodo_inicio] = 0
    distancia_estimada[nodo_inicio] = distancia_manhattan(nodo_inicio, nodo_objetivo)
    
    while True:
        nodo_actual = obtener_nodo_con_menor_costo([nodo for nodo in grafo if not costo_acumulado[nodo] == float('inf')], distancia_estimada)
        
        if nodo_actual is None:
            break
        
      
        if nodo_actual == nodo_objetivo:
            camino = []
            while nodo_actual in grafo:
                camino.append(nodo_actual)
                nodo_actual = grafo[nodo_actual][1]
            camino.append(nodo_actual)
            return camino
        
        costo_acumulado[nodo_actual] = float('inf')
        
    
        for vecino in grafo[nodo_actual]:
            nuevo_costo = costo_acumulado[nodo_actual] + grafo[nodo_actual][vecino]
            if nuevo_costo < costo_acumulado[vecino]:
                costo_acumulado[vecino] = nuevo_costo
                distancia_estimada[vecino] = nuevo_costo + distancia_manhattan(vecino, nodo_objetivo)
    
    return None  


grafo = {
    (1, 2): {(2, 3): 5, (3, 4): 8},
    (2, 3): {(1, 2): 5, (3, 4): 4, (4, 5): 7},
    (3, 4): {(1, 2): 8, (2, 3): 4, (5, 6): 3},
    (4, 5): {(2, 3): 7, (5, 6): 6},
    (5, 6): {(3, 4): 3, (4, 5): 6}
}

inicio = (1, 2)
objetivo = (5, 6)

camino_mas_corto = a_estrella(grafo, inicio, objetivo)
print("Camino más corto encontrado:", camino_mas_corto)
