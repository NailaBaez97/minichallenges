#Piloto de eventos (Priority Queue): Implementa una cola de prioridad utilizando una lista para insertar y eliminar 5 elementos.
class PriorityQueue:
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def vacia(self):
        return len(self.queue) == 0

    def insertar(self, lista):
        self.queue.append(lista)

    def eliminar(self):
        try:
            prioridad_maxima = 0
            for i in range(len(self.queue)):
                if self.queue[i] > self.queue[prioridad_maxima]:
                    prioridad_maxima = i
            item = self.queue[prioridad_maxima]
            del self.queue[prioridad_maxima]
            return item
        except IndexError:
            print()
            exit()
if __name__ == '__main__':
    mi_prioridad_queue= PriorityQueue()
    
    mi_prioridad_queue.insertar(4)
    mi_prioridad_queue.insertar(2)
    mi_prioridad_queue.insertar(5)
    mi_prioridad_queue.insertar(1)
    mi_prioridad_queue.insertar(3)
    
    print("Cola después de insertar 5 elementos:")
    print(mi_prioridad_queue)

   
    print("\nEliminando elementos en orden de prioridad:")
    while not mi_prioridad_queue.is_empty():
        print("Elemento eliminado:",mi_prioridad_queue.delete())
        print("Cola actual:", mi_prioridad_queue)
