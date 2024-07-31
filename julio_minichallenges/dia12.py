#Figura y Círculo: Crea una clase base Figuracion un método imprimir una clase derivada Círculo que extiende Figura y sobre escribe el método imprimir.

class Figura:
    def imprimir(self):
        print("Esta es una figura.")

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def imprimir(self):
        print(f"Este es un círculo con radio: {self.radio}")


if __name__ == '__main__':
    figura = Figura()
    figura.imprimir()  

    circulo = Circulo(5)
    circulo.imprimir()  