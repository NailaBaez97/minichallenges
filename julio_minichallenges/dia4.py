#Recorrido en amplitud (BFS): Implementa un recorrido BFS para un gráfico simple con 5 nodos.
from collections import deque

def bfs(nodo_inicial, grafo):

    visitados = {nodo: False for nodo in grafo}
    
    cola = deque([nodo_inicial])
    visitados[nodo_inicial] = True
    
    while cola:
        nodo_actual = cola.popleft()
        print(f"Nodo visitado: {nodo_actual}")
        
        for vecino in grafo[nodo_actual]:
            if not visitados[vecino]:
                visitados[vecino] = True
                cola.append(vecino)


grafo = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2],
    5: [3]
}

print("Recorrido BFS desde el nodo 1:")
bfs(1, grafo)
