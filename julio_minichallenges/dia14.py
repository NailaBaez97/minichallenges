#Polimorfismo: Crea una clase base Animal con un método hacer Sonido y una clase derivada Perro que sobre scribe 
# este método.

class Animal():
    def sonido(self, sonido):
        self.sonido = sonido
class perro(Animal):
    def hacer_sonido(self):
        return "guau guau"
    
def HacerSonidoAnimal(animal):
    print(animal.hacer_sonido())

mi_perro = perro()
HacerSonidoAnimal(mi_perro)


