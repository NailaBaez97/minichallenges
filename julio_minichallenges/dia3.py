#Recorrido en profundidad (DFS): Implementa un recorrido DFS para un gráfico simple con 5 nodos.
def dfs(nodo, visitados, grafo):
    visitados[nodo] = True
    print(f"Nodo visitado: {nodo}")
    
    
    for vecino in grafo[nodo]:
        if not visitados[vecino]:
            
            dfs(vecino, visitados, grafo)


grafo = {
    1: [2, 3],
    2: [1, 3, 4],
    3: [1, 2, 5],
    4: [2],
    5: [3]
}

visitados = {nodo: False for nodo in grafo}

dfs(1, visitados, grafo)
